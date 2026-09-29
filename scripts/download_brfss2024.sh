#!/usr/bin/env bash
set -euo pipefail
OUT="${1:-data/raw/brfss/2024}"
mkdir -p "$OUT"
cd "$OUT"
declare -A URLS=(
  [LLCP2024XPT.zip]="https://www.cdc.gov/brfss/annual_data/2024/files/LLCP2024XPT.zip"
  [codebook24_llcp-v2-508.zip]="https://www.cdc.gov/brfss/annual_data/2024/zip/codebook24_llcp-v2-508.zip"
)
for f in "${!URLS[@]}"; do
  [[ -s "$f" ]] && { echo "[skip] $f"; continue; }
  echo "[download] $f"
  curl -fL --retry 5 --retry-all-errors --connect-timeout 30 -o "$f" "${URLS[$f]}"
  test -s "$f"
  unzip -t "$f" >/dev/null
done
sha256sum *.zip | tee SHA256SUMS.txt
