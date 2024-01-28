#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

import unittest

from waflibs import text


class TestText(unittest.TestCase):
    pass


class TestIDNA(TestText):
    def test_idna(self):
        orig = u"カラ"
        result = "xn--lckwg"

        self.assertEqual(text.idna(orig), result)


if __name__ == "__main__":
    unittest.main()
