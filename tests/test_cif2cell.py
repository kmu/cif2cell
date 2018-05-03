import unittest
import subprocess
import glob


class TestCif2Cell(unittest.TestCase):
    def test_cif(self):
        for path in glob.glob('cifs/*.cif'):
            out = subprocess.check_output(['./cif2cell', path])

