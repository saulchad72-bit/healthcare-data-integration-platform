# Healthcare Fhir Data Integration

FHIR resource normalization and privacy-aware validation.

**Stack:** Python, HL7 FHIR, SQL.

## Scope
This is a reproducible **portfolio demonstration using synthetic data**. It is not a company codebase, production deployment, or evidence of use of real patient/customer data.

## Run locally

```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is required. The core demo uses only the Python standard library. Optional cloud/orchestration artifacts illustrate deployment integration and require separate infrastructure or credentials.

## Design decisions
- Small, inspectable input data for reproducible output.
- Explicit validation or idempotency logic in the transformation layer.
- No hard-coded secrets or real personal records.

## Limitations and next steps
- Replace sample files with permitted data sources before production use.
- Add durable storage, structured telemetry, monitoring, and integration tests for a deployed pipeline.
- Review security, cost, IAM, and compliance requirements before connecting to a real cloud environment.

## Repository structure
- `src/main.py`: runnable demonstration
- `data/`: synthetic examples
- `tests/`: smoke test
- Additional SQL / infrastructure examples where applicable
