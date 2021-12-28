#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from sys import path

path.append('..')  # setting this to make possible to run test files without Pycharm e.g. from cmd.

from pages.ZalandoPage import ZalandoPage


class TestZalandoPage(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
