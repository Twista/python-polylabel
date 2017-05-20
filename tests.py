import unittest
import json
from polylabel import polylabel


class PolyLabelTestCast(unittest.TestCase):

    def test_short(self):
        short = json.load(open("./fixtures/short.json", "r"))
        self.assertEquals(polylabel(short), [3317.546875, 1330.796875])

    def test_watter1(self):
        water1 = json.load(open("./fixtures/water1.json", "r"))
        self.assertEquals(polylabel(water1), [3865.85009765625, 2124.87841796875])
        self.assertEquals(polylabel(water1, 50), [3854.296875, 2123.828125])

    def test_works_on_degenerate_polygons(self):
        out = polylabel([[[0, 0], [1, 0], [2, 0], [0, 0]]])
        self.assertEquals(out, [0, 0])
        out = polylabel([[[0, 0], [1, 0], [1, 1], [1, 0], [0, 0]]])
        self.assertEquals(out, [0, 0])

    def test_watter2(self):
        water2 = json.load(open("./fixtures/water2.json", "r"))
        self.assertEquals(polylabel(water2, 1),[3263.5, 3263.5])
