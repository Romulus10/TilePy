import unittest

import TilePy.tools as t


class ToolsTest(unittest.TestCase):
    def test_remove_newlines(self):
        x = ['a', '\n', 'u']
        self.assertEqual(t.remove_newlines(x), ['a', 'u'])


if __name__ == "__main__":
    unittest.main()
