"""Local runnable entrypoint for the project."""
import argparse
from pathlib import Path
from pipeline import run

def main():
    p=argparse.ArgumentParser(description="Run local portfolio pipeline")
    p.add_argument("--input",default=str(Path(__file__).parent/"data"/"sample.csv"))
    p.add_argument("--output",default="output.json")
    args=p.parse_args()
    result=run(args.input,args.output)
    print(f"Wrote {args.output}: {len(result)} top-level fields")

if __name__=="__main__":main()
