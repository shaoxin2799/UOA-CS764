#!/usr/bin/env bash
set -euo pipefail

TAG="${1:-research-data-2026-09-30}"
OUT="${2:-data/frozen}"
BASE="https://github.com/shaoxin2799/UOA-CS764/releases/download/$TAG"
mkdir -p "$OUT"
cd "$OUT"

FILES=(
  atus-2003-2024.zip
  brfss-2024.zip
  timeseries-thuml-seed.zip
  gifteval.zip
  SHA256SUMS.txt
)
for f in "${FILES[@]}"; do
  echo "[download] $f"
  curl -fL --retry 5 --retry-all-errors -o "$f" "$BASE/$f"
done
sha256sum -c SHA256SUMS.txt --ignore-missing
echo "Frozen public datasets are ready under: $(pwd)"
