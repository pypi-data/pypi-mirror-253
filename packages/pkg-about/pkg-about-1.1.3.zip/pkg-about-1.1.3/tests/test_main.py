# Copyright (c) 2020 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/license/zlib

import unittest
from pathlib import Path

import pkg_about


class MainTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_about(self):
        pkg_about.about("pkg_about")
        self.assertEqual(__title__, "pkg-about")
        self.assertEqual(__version__, "1.1.3")
        self.assertEqual(__version_info__.major, 1)
        self.assertEqual(__version_info__.minor, 1)
        self.assertEqual(__version_info__.micro, 3)
        self.assertEqual(__version_info__.releaselevel, "final")
        self.assertEqual(__version_info__.serial, 0)
        self.assertEqual(__summary__, "Shares Python package metadata at runtime.")
        self.assertEqual(__uri__, "https://pypi.org/project/pkg-about/")
        self.assertEqual(__author__, "Adam Karpierz")
        self.assertEqual(__email__, "adam@karpierz.net")
        self.assertEqual(__author_email__, "adam@karpierz.net")
        self.assertEqual(__maintainer__, "Adam Karpierz")
        self.assertEqual(__maintainer_email__, "adam@karpierz.net")
        self.assertEqual(__license__,
                         "zlib/libpng License ; https://opensource.org/license/zlib")
        self.assertIsNone(__copyright__)

    def test_about_from_setup(self):
        pkg_about.about_from_setup(Path(__file__).resolve().parent.parent)
        self.assertEqual(about.__title__, "pkg-about")
        self.assertEqual(about.__version__, "1.1.3")
        self.assertEqual(about.__version_info__.major, 1)
        self.assertEqual(about.__version_info__.minor, 1)
        self.assertEqual(about.__version_info__.micro, 3)
        self.assertEqual(about.__version_info__.releaselevel, "final")
        self.assertEqual(about.__version_info__.serial, 0)
        self.assertEqual(about.__summary__, "Shares Python package metadata at runtime.")
        self.assertEqual(about.__uri__, "https://pypi.org/project/pkg-about/")
        self.assertEqual(about.__author__, "Adam Karpierz")
        self.assertEqual(about.__email__, "adam@karpierz.net")
        self.assertEqual(about.__author_email__, "adam@karpierz.net")
        self.assertEqual(about.__maintainer__, "Adam Karpierz")
        self.assertEqual(about.__maintainer_email__, "adam@karpierz.net")
        self.assertEqual(about.__license__,
                         "zlib/libpng License ; https://opensource.org/license/zlib")
        self.assertEqual(about.__copyright__, "Copyright (c) 2020-2024 Adam Karpierz")
