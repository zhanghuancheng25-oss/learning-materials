"""Educational RR experiment; not a reproduction of any paper's figures."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
METHODS = ["wr", "rr", "so", "ig", "rr_fixed"]
CONFIG = dict(n=64, d=2, data_seed=20261117, sampling_seeds=list(range(10)),
              kappas=[1, 100], batch_sizes=[1, 8, 64], eta_multipliers=[0.05, 0.2, 0.8],
              epochs=20, checkpoints=[1, 5, 20], methods=METHODS)


def batches(method, n, b, rng, so_order):
    if method == "wr":
        return rng.integers(n, size=(n // b, b))
    if method == "rr":
        return rng.permutation(n).reshape(-1, b)
    if method == "so":
        return so_order.reshape(-1, b)
    if method == "ig":
        return np.arange(n).reshape(-1, b)
    if method == "rr_fixed":
        return np.arange(n).reshape(-1, b)[rng.permutation(n // b)]
    raise ValueError(method)


def run(method, centers, h, b, eta, seed, epochs):
    n = len(centers)
    optimum = centers.mean(axis=0)
    x = optimum + 3.0
    rng = np.random.default_rng(seed)
    so_order = rng.permutation(n) if method == "so" else None
    gap = lambda z: float(0.5 * np.sum(h * (z - optimum) ** 2))
    history = [gap(x)]
    avg = np.zeros_like(x)
    count = 0
    for _ in range(epochs):
        selected = batches(method, n, b, rng, so_order)
        if method != "wr":
            assert np.array_equal(np.sort(selected.ravel()), np.arange(n))
        for idx in selected:
            avg += x  # pre-update average, matching the convention explained in P08
            count += 1
            gradient = ((x - centers[idx]) * h).mean(axis=0)
            x = x - eta * gradient
        history.append(gap(x))
    assert count == epochs * n // b
    assert np.isfinite(history).all()
    return dict(gaps=history, final_x=x.tolist(), averaged_gap=gap(avg / count),
                updates=count, component_gradients=count * b)


def checks(centers):
    h = np.array([1.0, 20.0])
    x = np.array([0.2, -0.4])
    objective = lambda z: float(0.5 * np.mean(np.sum((z - centers)**2 * h, axis=1)))
    eps = 1e-5
    numeric = np.array([(objective(x + eps * e) - objective(x - eps * e)) / (2 * eps)
                        for e in np.eye(2)])
    err = float(np.max(np.abs(numeric - h * (x - centers.mean(axis=0)))))
    assert err < 1e-7
    eta = 0.01
    optimum = centers.mean(axis=0)
    expected = optimum + (1 - eta * h)**5 * 3.0
    fullbatch_error = 0.0
    for method in METHODS[1:]:
        actual = np.array(run(method, centers, h, len(centers), eta, 3, 5)["final_x"])
        fullbatch_error = max(fullbatch_error, float(np.max(np.abs(actual - expected))))
    assert fullbatch_error < 1e-12
    # Exact enumeration at a fixed point: n=6, b=3, zero-mean gradient vectors.
    vectors = np.arange(12, dtype=float).reshape(6, 2)
    vectors -= vectors.mean(axis=0)
    empirical = np.mean([np.sum(vectors[list(ids)].mean(axis=0)**2)
                         for ids in itertools.combinations(range(6), 3)])
    predicted = np.mean(np.sum(vectors**2, axis=1)) * (6 - 3) / (3 * (6 - 1))
    variance_error = float(abs(empirical - predicted))
    assert variance_error < 1e-12
    eta = 0.1
    endpoints = []
    for order in ([1.0, -1.0], [-1.0, 1.0]):
        z = 0.0
        for center in order:
            z -= eta * (z - center)
        endpoints.append(z)
    assert np.allclose(endpoints, [-eta**2, eta**2])
    # Explicitly verify SO keeps the exact same order across epochs.
    rng = np.random.default_rng(7)
    so_order = rng.permutation(64)
    assert np.array_equal(batches("so", 64, 8, rng, so_order),
                          batches("so", 64, 8, rng, so_order))
    return dict(gradient_max_abs_error=err, fullbatch_vs_gd_error=fullbatch_error,
                finite_population_identity_error=variance_error,
                two_sample_endpoints=endpoints, sampler_coverage="checked in every trajectory",
                so_reuses_order=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="experiment/v1_sampling_quadratic")
    args = parser.parse_args()
    output = ROOT / args.output
    if output.exists():
        raise SystemExit("Output already exists; choose a new --output version (no overwrite).")
    rng = np.random.default_rng(CONFIG["data_seed"])
    centers = rng.normal(size=(CONFIG["n"], CONFIG["d"]))
    centers = centers[np.argsort(centers[:, 0])]
    validation = checks(centers)
    trials = []
    summaries = []
    for kappa, b, c, method in itertools.product(CONFIG["kappas"], CONFIG["batch_sizes"],
                                                 CONFIG["eta_multipliers"], METHODS):
        eta = c / kappa
        group = []
        for seed in CONFIG["sampling_seeds"]:
            result = run(method, centers, np.array([1., kappa]), b, eta, seed, CONFIG["epochs"])
            record = dict(kappa=kappa, batch_size=b, eta_multiplier=c, eta=eta,
                          method=method, seed=seed, **result)
            trials.append(record)
            group.append(record)
        curves = np.array([r["gaps"] for r in group])
        mean_x = np.mean([r["final_x"] for r in group], axis=0)
        mean_x_gap = float(0.5 * np.sum(np.array([1., kappa]) * (mean_x - centers.mean(axis=0))**2))
        summaries.append(dict(kappa=kappa, batch_size=b, eta_multiplier=c, method=method,
                              curve_mean=curves.mean(axis=0).tolist(),
                              curve_std=curves.std(axis=0, ddof=1).tolist(),
                              checkpoints={str(k): dict(mean=float(curves[:,k].mean()),
                                                       std=float(curves[:,k].std(ddof=1)))
                                           for k in CONFIG["checkpoints"]},
                              final_mean_gap=float(curves[:,-1].mean()),
                              gap_of_mean_final_parameter=mean_x_gap,
                              mean_averaged_iterate_gap=float(np.mean([r["averaged_gap"] for r in group])),
                              updates=CONFIG["epochs"]*CONFIG["n"]//b,
                              component_gradients=CONFIG["epochs"]*CONFIG["n"]))
    output.mkdir(parents=True)
    metrics = dict(config=CONFIG, scope="teaching only; no paper figure reproduced", validation=validation,
                   environment=dict(python=platform.python_version(), numpy=np.__version__,
                                    matplotlib=matplotlib.__version__),
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   centers_sha256=hashlib.sha256(centers.tobytes()).hexdigest(),
                   trajectory_count=len(trials), summaries=summaries)
    (output / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    (output / "trajectories.json").write_text(json.dumps(trials, separators=(",", ":"))+"\n", encoding="utf-8")
    fig, axes = plt.subplots(2, 3, figsize=(13, 7), layout="constrained")
    work = np.arange(CONFIG["epochs"]+1) * CONFIG["n"]
    for row, kappa in enumerate(CONFIG["kappas"]):
        for col, b in enumerate(CONFIG["batch_sizes"]):
            ax = axes[row,col]
            for s in summaries:
                if (s["kappa"],s["batch_size"],s["eta_multiplier"]) != (kappa,b,0.2):
                    continue
                mean, sd = np.array(s["curve_mean"]), np.array(s["curve_std"])
                ax.semilogy(work, np.maximum(mean,1e-18), label=s["method"])
                ax.fill_between(work,np.maximum(mean-sd,1e-18),np.maximum(mean+sd,1e-18),alpha=0.08)
            ax.set(title=f"kappa={kappa}, b={b}", xlabel="Component gradient evaluations", ylabel="F(x) - F* (mean)")
            ax.grid(alpha=0.25)
    axes[0,0].legend(fontsize=8)
    fig.suptitle("Teaching example: fixed eta=0.2/L; 10 sampling seeds; shading = +/- 1 SD")
    fig.savefig(output/"convergence.png",dpi=150)
    plt.close(fig)
    fig, axes = plt.subplots(2,3,figsize=(13,7),layout="constrained")
    for row, kappa in enumerate(CONFIG["kappas"]):
        for col, b in enumerate(CONFIG["batch_sizes"]):
            ax=axes[row,col]
            for method in METHODS:
                values=[next(s["final_mean_gap"] for s in summaries if
                             (s["kappa"],s["batch_size"],s["eta_multiplier"],s["method"]) == (kappa,b,c,method))
                        for c in CONFIG["eta_multipliers"]]
                ax.semilogy(CONFIG["eta_multipliers"],np.maximum(values,1e-18),"o-",label=method)
            ax.set(title=f"kappa={kappa}, b={b}",xlabel="eta * L",ylabel="Final F(x) - F* (mean)")
            ax.grid(alpha=0.25)
    axes[0,0].legend(fontsize=8)
    fig.suptitle("All prespecified step sizes, same 1280 component-gradient budget")
    fig.savefig(output/"stepsize_grid.png",dpi=150)
    plt.close(fig)
    print(json.dumps(dict(output=str(output), trajectories=len(trials), validation=validation), ensure_ascii=False))


if __name__ == "__main__":
    main()
