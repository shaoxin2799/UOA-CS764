# AAMAS data staging

Frozen external-data inputs for the social-simulation extension.

## Planned roles

- **BRFSS** — population / state-distribution backbone.
- **ATUS 2003–2024** — activity profiles and time-with-others signals; not a direct preference label.
- **NSHAP R1–R3** — network structure, UCLA-3 loneliness calibration, and long-horizon persistence constraints.

## Acquisition policy

1. Download once from the official source.
2. Preserve raw files unchanged.
3. Record source URL, acquisition timestamp, byte size and SHA-256.
4. Run formal experiments from a frozen local snapshot only.
5. Do not silently substitute mirrors or harmonized versions.
6. Restricted/authenticated sources are audited but never bypassed.

ATUS is automated via GitHub Actions. BRFSS/NSHAP acquisition remains source/version explicit so we do not accidentally mix years or licensed extracts.
