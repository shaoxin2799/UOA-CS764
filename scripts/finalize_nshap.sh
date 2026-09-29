#!/usr/bin/env bash
set -euo pipefail

# Finalize authenticated ICPSR NSHAP downloads without committing raw data.
# Expected ICPSR bundles (filenames may contain extra text):
#   20541 / v10 — NSHAP Round 1
#   34921 / v5  — NSHAP Round 2
#   36873 / v9  — NSHAP Round 3 + COVID-19

SOURCE_DIR="${1:-data/incoming/nshap}"
OUT_DIR="${2:-artifacts/nshap}"
TAG="${TAG:-research-data-2026-09-30}"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Missing source directory: $SOURCE_DIR" >&2
  exit 2
fi

mkdir -p "$OUT_DIR"
rm -f "$OUT_DIR"/nshap-icpsr-* \
  "$OUT_DIR/nshap-manifest.json" \
  "$OUT_DIR/NSHAP_SHA256SUMS.txt"

find_bundle() {
  local study_id="$1"
  local -a matches=()
  mapfile -t matches < <(find "$SOURCE_DIR" -maxdepth 2 -type f \
    \( -iname "*${study_id}*.zip" -o -iname "*${study_id}*.tar.gz" \) | sort)
  if [[ "${#matches[@]}" -ne 1 ]]; then
    echo "Expected exactly one archive containing study ID ${study_id}; found ${#matches[@]}" >&2
    printf '  %s\n' "${matches[@]:-}" >&2
    exit 3
  fi
  printf '%s\n' "${matches[0]}"
}

validate_archive() {
  local file="$1"
  case "$file" in
    *.zip) unzip -tq "$file" >/dev/null ;;
    *.tar.gz) tar -tzf "$file" >/dev/null ;;
    *) echo "Unsupported archive: $file" >&2; exit 4 ;;
  esac
}

declare -A versions=(
  [20541]="v10"
  [34921]="v5"
  [36873]="v9"
)

for study_id in 20541 34921 36873; do
  src="$(find_bundle "$study_id")"
  validate_archive "$src"
  case "$src" in
    *.zip) ext="zip" ;;
    *.tar.gz) ext="tar.gz" ;;
  esac
  dest="$OUT_DIR/nshap-icpsr-${study_id}-${versions[$study_id]}.${ext}"
  cp -f "$src" "$dest"
  echo "[validated] $dest"
done

python3 scripts/build_manifest.py "$OUT_DIR" \
  --name "NSHAP public-use rounds 1-3" \
  --source "ICPSR 20541 version 10" \
  --source "ICPSR 34921 version 5" \
  --source "ICPSR 36873 version 9" \
  --output "$OUT_DIR/nshap-manifest.json"

(
  cd "$OUT_DIR"
  sha256sum nshap-icpsr-* > NSHAP_SHA256SUMS.txt
  sha256sum -c NSHAP_SHA256SUMS.txt
)

if [[ "${UPLOAD:-0}" == "1" ]]; then
  command -v gh >/dev/null || {
    echo "UPLOAD=1 requires GitHub CLI (gh) authenticated for this repository." >&2
    exit 5
  }
  gh release upload "$TAG" \
    "$OUT_DIR"/nshap-icpsr-* \
    "$OUT_DIR/nshap-manifest.json" \
    "$OUT_DIR/NSHAP_SHA256SUMS.txt" \
    --clobber
  echo "Uploaded NSHAP assets to release: $TAG"
else
  echo "NSHAP archives validated and hashed under: $OUT_DIR"
  echo "After confirming redistribution terms, rerun with UPLOAD=1 to upload them."
fi
