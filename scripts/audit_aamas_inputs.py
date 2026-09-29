#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys

ROOT=Path("data/raw")
EXPECTED={
  "atus/2003-2024":[
    "atusresp-0324.zip","atusrost-0324.zip","atusact-0324.zip",
    "atussum-0324.zip","atuswho-0324.zip","atuscps-0324.zip"
  ],
  "brfss":[],
  "nshap":[]
}

def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

report={}
missing=[]
for rel,names in EXPECTED.items():
    d=ROOT/rel
    present=sorted(str(p.relative_to(ROOT)) for p in d.rglob("*") if p.is_file()) if d.exists() else []
    expected_missing=[str(Path(rel)/n) for n in names if not (d/n).exists()]
    missing.extend(expected_missing)
    report[rel]={"exists":d.exists(),"files":present,"missing_required":expected_missing}
print(json.dumps(report,indent=2))
sys.exit(1 if missing else 0)
