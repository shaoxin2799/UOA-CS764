#!/usr/bin/env bash
set -euo pipefail

OUT="${1:-data/raw/atus/2003-2024}"
mkdir -p "$OUT"
cd "$OUT"

BASE="https://www.bls.gov/tus/datafiles"
REF="https://www.bls.gov/tus/data/datafiles-0324.htm"
FILES=(
  atusresp-0324.zip
  atusrost-0324.zip
  atusact-0324.zip
  atussum-0324.zip
  atuswho-0324.zip
  atuscps-0324.zip
)

for f in "${FILES[@]}"; do
  if [[ -s "$f" ]]; then
    echo "[skip] $f already exists"
    continue
  fi
  echo "[download] $f"
  curl -fL --retry 5 --retry-all-errors --connect-timeout 30     -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/129 Safari/537.36"     -e "$REF" -o "$f" "$BASE/$f"
  test -s "$f"
  unzip -t "$f" >/dev/null
done

sha256sum *.zip | tee SHA256SUMS.txt
