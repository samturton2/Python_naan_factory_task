# import the NaanFactory class
from naan_factory import NaanFactory

#import the test modules needed
import pytest
import unittest

# create a test class
class TestFactory(unittest.TestCase):
    #create an object of our naan factory
    factory_1 = NaanFactory()

    # tests the make_dough function
    def test_make_dough(self):
        # If the make dough function works it should return true so the test should pass
        self.assertTrue(self.factory_1.make_dough(True, True))

    # tests the make_naan function
    def test_make_naan(self):
        self.assertTrue(self.factory_1.make_naan(True))

    # tests the run_factory function
    def test_run_factory(self):
        self.assertTrue(self.factory_1.run_factory(True, True))