"""Download the paper manifest with Python's standard library (Python >= 3.10).

PDF/source caches stay local. Metadata and hashes are committed for auditability.
Never executes downloaded source; archives are extracted as regular files only.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import html
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import tarfile
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
UA = "research-workflow-rr/1.0 (academic literature download)"


def download(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return response.read(50 * 1024 * 1024)
    finally:
        if "arxiv.org" in url:
            time.sleep(3)


def extract_source(blob: bytes, dest: Path) -> list[str]:
    files = []
    try:
        with tarfile.open(fileobj=io.BytesIO(blob), mode="r:*") as archive:
            members = archive.getmembers()
            if sum(m.size for m in members) > 100 * 1024 * 1024:
                raise ValueError("Source archive too large")
            for member in members:
                path = PurePosixPath(member.name.replace("\\", "/"))
                if path.is_absolute() or ".." in path.parts or any(":" in p for p in path.parts):
                    raise ValueError("Unsafe archive path")
                if not member.isfile():
                    continue
                target = dest.joinpath(*path.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.extractfile(member) as source:
                    target.write_bytes(source.read())
                files.append(target)
    except tarfile.ReadError:
        try:
            raw = gzip.decompress(blob)
        except OSError:
            raw = blob
        if b"\\documentclass" not in raw and b"\\begin{document}" not in raw:
            raise ValueError("Response is not a TeX archive (could be unavailable or an HTML error)")
        target = dest / "main.tex"
        target.write_bytes(raw)
        files.append(target)
    tex_paths = []
    stale = {"history", "old", "backup", "draft", "previous", "archive", "submitted"}
    for target in files:
        relative = target.relative_to(dest)
        if any(p.lower() in stale for p in relative.parts[:-1]):
            isolated = dest / ".stale" / relative
            isolated.parent.mkdir(parents=True, exist_ok=True)
            target.replace(isolated)
            continue
        if target.suffix == ".tex":
            raw = target.read_bytes()
            target.with_suffix(".tex.orig").write_bytes(raw)
            # Same reading-copy convention as upstream, not intended for compilation.
            cleaned = re.sub(rb"(?<!\\)%[^\r\n]*", b"", raw)
            target.write_bytes(cleaned)
            tex_paths.append(str(relative).replace("\\", "/"))
    return tex_paths


def fetch(entry: dict, text_only: bool = False) -> dict:
    dest = ROOT / "related_work" / entry["slug"]
    dest.mkdir(parents=True, exist_ok=True)
    status_path = dest / "metadata.json"
    status = json.loads(status_path.read_text(encoding="utf-8")) if status_path.exists() else dict(entry)
    status["checked_date"] = "2026-11-17"
    if not text_only:
        arxiv = entry.get("arxiv")
        if arxiv:
            pinned = status.get("pinned_arxiv")
            if not pinned:
                page = download(f"https://arxiv.org/abs/{arxiv}").decode("utf-8", errors="replace")
                (dest / "abstract.html").write_text(page, encoding="utf-8")
                versions = re.findall(re.escape(arxiv) + r"v(\d+)", page)
                pinned = arxiv + "v" + str(max(map(int, versions), default=1))
                status["pinned_arxiv"] = pinned
                authors = re.findall(r'<meta name="citation_author" content="([^"]+)"', page)
                status["arxiv_authors"] = [html.unescape(a) for a in authors]
            pdf_url = f"https://arxiv.org/pdf/{pinned}"
            source_url = f"https://arxiv.org/e-print/{pinned}"
        else:
            pdf_url = entry["pdf_url"]
            source_url = None
        pdf = dest / "paper.pdf"
        if not pdf.exists():
            blob = download(pdf_url)
            if not blob.startswith(b"%PDF-"):
                raise ValueError("PDF endpoint did not return a PDF")
            pdf.write_bytes(blob)
        status["pdf_url"] = pdf_url
        status["pdf_sha256"] = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if source_url and status.get("source_status") != "downloaded":
            try:
                blob = download(source_url)
                source = dest / "source"
                source.mkdir(exist_ok=True)
                names = extract_source(blob, source)
                if not names:
                    raise ValueError("No active .tex files in archive")
                status.update(source_status="downloaded", source_url=source_url,
                              source_sha256=hashlib.sha256(blob).hexdigest(), tex_files=names)
                (dest / "source.tar").write_bytes(blob)
                status.pop("source_error", None)
            except Exception as exc:
                status.update(source_status="unavailable_at_fetch", source_url=source_url,
                              source_error=str(exc))
        elif not source_url:
            status["source_status"] = "no_verified_source_endpoint"
    try:
        subprocess.run(["pdftotext", "-layout", str(dest / "paper.pdf"), str(dest / "paper.txt")],
                       check=True, capture_output=True)
        status["text_extracted"] = True
    except (OSError, subprocess.CalledProcessError) as exc:
        status["text_extracted"] = False
        status["text_error"] = str(exc)
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"slug": entry["slug"], "version": status.get("pinned_arxiv"),
            "source": status.get("source_status"), "text": status.get("text_extracted")}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="*", help="Paper slugs; default: all papers")
    parser.add_argument("--text-only", action="store_true")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "related_work" / "papers.json").read_text(encoding="utf-8"))
    failed = []
    for paper in manifest["papers"]:
        if args.only and paper["slug"] not in args.only:
            continue
        try:
            print(json.dumps(fetch(paper, args.text_only), ensure_ascii=False), flush=True)
        except Exception as exc:
            print(json.dumps({"slug": paper["slug"], "error": str(exc)}), flush=True)
            failed.append(paper["slug"])
    if failed:
        raise SystemExit("Failed papers: " + ", ".join(failed))


if __name__ == "__main__":
    main()
