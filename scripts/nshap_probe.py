#!/usr/bin/env python3
import json, re
from pathlib import Path
import requests

studies={
  "20541":{"round":"R1","page":"https://www.icpsr.umich.edu/web/NACDA/studies/20541/datadocumentation"},
  "34921":{"round":"R2","page":"https://www.icpsr.umich.edu/web/NACDA/studies/34921/datadocumentation"},
  "36873":{"round":"R3_COVID","page":"https://www.icpsr.umich.edu/web/NACDA/studies/36873/datadocumentation"},
}
out=Path("data/raw/nshap")
out.mkdir(parents=True,exist_ok=True)
report={}
s=requests.Session()
s.headers["User-Agent"]="Mozilla/5.0"
for sid,meta in studies.items():
    r=s.get(meta["page"],timeout=60)
    report[sid]={"round":meta["round"],"page_status":r.status_code,"page_url":meta["page"],"bytes":len(r.content)}
    if r.ok:
        (out/f"{sid}.html").write_bytes(r.content)
        links=sorted(set(re.findall(r'https?://[^"\'<> ]+',r.text)))
        cand=[x for x in links if ("download" in x.lower() or ".zip" in x.lower())]
        report[sid]["download_candidates"]=cand[:100]
Path("manifests").mkdir(exist_ok=True)
Path("manifests/nshap-access-probe.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
