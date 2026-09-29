#!/usr/bin/env python3
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

def sha256(path: Path, chunk=1024*1024):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()

p=argparse.ArgumentParser()
p.add_argument("root")
p.add_argument("--name", required=True)
p.add_argument("--source", action="append", default=[])
p.add_argument("--output", required=True)
args=p.parse_args()

root=Path(args.root)
files=[]
for f in sorted(x for x in root.rglob("*") if x.is_file()):
    files.append({"path": str(f.relative_to(root)), "bytes": f.stat().st_size, "sha256": sha256(f)})

out={"name": args.name, "created_at_utc": datetime.now(timezone.utc).isoformat(), "sources": args.source, "root": str(root), "files": files}
Path(args.output).parent.mkdir(parents=True, exist_ok=True)
Path(args.output).write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"name":args.name,"n_files":len(files),"output":args.output}))
