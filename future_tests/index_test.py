import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonMapsAndLists(unittest.TestCase):
    def test_palermo_var(self):
        self.assertEqual(palermo, 'Palermo')

    def test_la_boca_var(self):
        self.assertEqual(la_boca, 'La Boca')

    def test_ba_lat_var(self):
        self.assertEqual(ba_latitude, -34.6037)

    def test_ba_long_var(self):
        self.assertEqual(ba_longitude, -58.3816)
