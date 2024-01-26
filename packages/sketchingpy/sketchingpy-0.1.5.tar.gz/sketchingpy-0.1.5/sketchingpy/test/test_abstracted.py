import unittest

import sketchingpy.abstracted


class AbstractedTests(unittest.TestCase):

    def test_reorder_coords(self):
        output_coords = sketchingpy.abstracted.reorder_coords(1, 4, 2, 3)
        self.assertEqual(len(output_coords), 4)
        self.assertEqual(output_coords[0], 1)
        self.assertEqual(output_coords[1], 3)
        self.assertEqual(output_coords[2], 2)
        self.assertEqual(output_coords[3], 4)
