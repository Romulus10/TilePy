import unittest

import TilePy.romulus_tools as rt


class RomulusToolsTest(unittest.TestCase):
    def test_remove_newlines(self):
        x = ['a', '\n', 'u']
        self.assertEqual(rt.remove_newlines(x), ['a', 'u'])


if __name__ == "__main__":
    unittest.main()
