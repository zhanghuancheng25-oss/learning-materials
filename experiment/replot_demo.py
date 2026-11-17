"""Improve log-axis display from saved metrics; no rerunning or filtering trials."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

output = Path(__file__).resolve().parent / "v1_sampling_quadratic"
metrics = json.loads((output/"metrics.json").read_text(encoding="utf-8"))
summaries = metrics["summaries"]
fig, axes = plt.subplots(2,3,figsize=(13,7),layout="constrained")
work = np.arange(21)*64
for row,kappa in enumerate([1,100]):
    for col,b in enumerate([1,8,64]):
        ax=axes[row,col]
        relevant=[s for s in summaries if (s["kappa"],s["batch_size"],s["eta_multiplier"]) == (kappa,b,0.2)]
        for s in relevant:
            mean,sd=np.array(s["curve_mean"]),np.array(s["curve_std"])
            ax.semilogy(work,mean,label=s["method"])
            ax.fill_between(work,np.maximum(mean-sd,1e-18),mean+sd,alpha=0.08)
        positive=[v for s in relevant for v in s["curve_mean"] if v>0]
        ax.set_ylim(min(positive)*0.3,max(positive)*2)
        ax.set(title=f"kappa={kappa}, b={b}",xlabel="Component gradient evaluations",ylabel="F(x) - F* (mean)")
        ax.grid(alpha=0.25)
axes[0,0].legend(fontsize=8)
fig.suptitle("Teaching example: eta=0.2/L; mean +/- 1 SD; bands clipped at log-axis limits")
fig.savefig(output/"convergence.png",dpi=150)
