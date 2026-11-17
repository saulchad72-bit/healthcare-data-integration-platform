import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "sample.csv"

def read_rows():
    with DATA.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))
