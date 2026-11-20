import unittest
from pathlib import Path

class ProjectStructureTests(unittest.TestCase):
    def test_sample_exists_and_is_nonempty(self):
        root=Path(__file__).resolve().parents[1]
        sample=list((root/"data").glob("sample.*"))
        self.assertEqual(len(sample),1)
        self.assertTrue(sample[0].read_text().strip())

if __name__=="__main__":unittest.main()
