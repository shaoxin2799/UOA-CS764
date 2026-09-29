#!/usr/bin/env python3
from pathlib import Path
import shutil
from huggingface_hub import hf_hub_download

REPO="thuml/Time-Series-Library"
FILES=[
    "electricity/electricity.csv",
    "traffic/traffic.csv",
    "weather/weather.csv",
    "exchange_rate/exchange_rate.csv",
    "ETT-small/ETTh1.csv",
    "ETT-small/ETTh2.csv",
    "ETT-small/ETTm1.csv",
    "ETT-small/ETTm2.csv",
]
root=Path("data/raw/timeseries/thuml")
for remote in FILES:
    dest=root/remote
    dest.parent.mkdir(parents=True, exist_ok=True)
    p=Path(hf_hub_download(repo_id=REPO, repo_type="dataset", filename=remote))
    shutil.copy2(p, dest)
    print(f"{remote} -> {dest}")
