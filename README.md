# healthcare-claims-etl

De-identified claims ingestion and encounter normalization with validation rejection output.

## Stack and design

Python, SQL, ADF/Databricks pipeline design. The runnable core is deliberately kept lightweight and dependency-free so the project can be tested locally without cloud credentials. Cloud products described here are architectural targets or integration examples **unless actual integration code is present**.

## Architecture

`data/sample.csv` → `pipeline.py` (validation and transformations) → `output.json` (inspection/reconciliation output)

Input example: fictional claim identifiers.

## Quickstart

Requires Python 3.10 or newer. From the repository root:

```bash
python cli.py
python -m unittest discover -s tests -v
```

Output is written to `output.json`; customize paths with:

```bash
python cli.py --input data/sample.csv --output output.json
```

## Implementation notes

- Functional logic is in `pipeline.py`, separate from the CLI.
- Includes a representative dataset, automated unit tests, and a CI workflow.
- No external services or credentials are required for the demo run.
- Run against a larger synthetic dataset and record timing/data-quality results before describing performance improvements.

## Repository layout

- `pipeline.py` — domain-specific transformation, validation, or aggregation
- `cli.py` — command-line entrypoint
- `data/` — safe sample input records
- `tests/` — reproducibility checks
- `.github/workflows/tests.yml` — GitHub Actions test workflow

## Scope and limitations

This is an independent portfolio prototype, **not an employer production system**. It does not claim live cloud infrastructure, secured PHI handling, operational SLAs, or HIPAA certification. For real data, add secrets management, access controls, PII redaction, schema contracts, monitoring, and integration tests.

## Suggested next iteration

Wire the validated core into the Python environment, add failure injection tests, and document before/after metrics.

## License

MIT
