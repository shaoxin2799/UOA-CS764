#!/usr/bin/env python3
import shutil, sys
from pathlib import Path
checks={"python": shutil.which("python") or shutil.which("python3"),"git": shutil.which("git"),"curl": shutil.which("curl"),"unzip": shutil.which("unzip")}
bad=False
for k,v in checks.items():
    print(f"{k:8} {'OK' if v else 'MISSING'} {v or ''}")
    bad |= not bool(v)
print("repo:", Path.cwd())
sys.exit(1 if bad else 0)
