import unittest
import subprocess
import pathlib


class TestCif2Cell(unittest.TestCase):
    def test_cif(self):
        for path in pathlib.Path('cifs').glob("*.cif"):
            out = subprocess.check_output(['cif2cell', path])
            print(out)

