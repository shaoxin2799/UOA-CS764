#!/usr/bin/env python3
import argparse
from huggingface_hub import snapshot_download

p=argparse.ArgumentParser()
p.add_argument("--repo", default="Salesforce/GiftEval")
p.add_argument("--local-dir", default="data/raw/timeseries/gifteval")
p.add_argument("--allow", action="append", default=[])
a=p.parse_args()

kwargs=dict(repo_id=a.repo,repo_type="dataset",local_dir=a.local_dir)
if a.allow:
    kwargs["allow_patterns"]=a.allow
snapshot_download(**kwargs)
print(a.local_dir)
