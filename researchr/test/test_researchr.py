# -*- coding: utf-8 -*-

"""
Unit test for researchr.py modul
"""

import researchr as res
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test_searchPublication(self):
        res.searchPublication("web-service")
    def test_searchConference(self):
        res.searchConference("xxx")
        

if __name__ == "__main__":
    unittest.main()
