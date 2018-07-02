from PageObject.Helper import *
import unittest


class testCases(unittest.TestCase):

    def setUp(self):
        return
    def test_1(self):
        item = jsonReader.getData("Browser")
        print(item)