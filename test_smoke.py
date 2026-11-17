import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from main import run

class TestSmoke(unittest.TestCase):
    def test_run_returns_results(self):
        result = run()
        self.assertIsInstance(result, dict)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
