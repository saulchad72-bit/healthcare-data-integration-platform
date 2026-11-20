import tempfile,unittest
from pathlib import Path
from pipeline import run

ROOT=Path(__file__).resolve().parents[1]
class PipelineTests(unittest.TestCase):
    def test_sample_produces_output(self):
        with tempfile.TemporaryDirectory() as work:
            output=Path(work)/"output.json"
            result=run(ROOT/"data"/"sample.csv",output)
            self.assertTrue(output.is_file())
            self.assertIsInstance(result,dict)
            self.assertGreater(len(result),0)

if __name__=="__main__":unittest.main()
