import unittest
import json
from polylabel import polylabel


class PolyLabelTestCast(unittest.TestCase):

    def test_short(self):
        with open("./fixtures/short.json", "r") as f:
            short = json.load(f)
            self.assertEqual(polylabel(short), [3317.546875, 1330.796875])

    def test_watter1(self):
        with open("./fixtures/water1.json", "r") as f:
            water1 = json.load(f)
            self.assertEqual(polylabel(water1), [
                              3865.85009765625, 2124.87841796875])
            self.assertEqual(polylabel(water1, 50), [3854.296875, 2123.828125])

    def test_float(self):
        with open("./fixtures/float.json", "r") as f:
            float_poly = json.load(f)
            self.assertEqual(polylabel(float_poly),
                             [-23.210525613080737, 24.425270860193958])

    def test_works_on_degenerate_polygons(self):
        out = polylabel([[[0, 0], [1, 0], [2, 0], [0, 0]]])
        self.assertEqual(out, [0, 0])
        out = polylabel([[[0, 0], [1, 0], [1, 1], [1, 0], [0, 0]]])
        self.assertEqual(out, [0, 0])

    def test_watter2(self):
        with open("./fixtures/water2.json", "r") as f:
            water2 = json.load(f)
            self.assertEqual(polylabel(water2, 1), [3263.5, 3263.5])


if __name__ == '__main__':
    unittest.main()
