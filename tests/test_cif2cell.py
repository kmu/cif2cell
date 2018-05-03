import unittest
import subprocess
import glob


class TestCif2Cell(unittest.TestCase):
    def test_cif(self):
        for path in glob.glob('cifs/*.cif'):
            p = subprocess.Popen(['./cif2cell', path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout_data, stderr_data = p.communicate()
            print("OUT")
            print(stdout_data.decode())

            assert not "***Warning: Space group operation check failed" in stdout_data.decode()
