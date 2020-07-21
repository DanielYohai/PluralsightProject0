## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import unittest
import main

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES

## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES

## END DECLARE VARIABLES
## END DECLARE VARIABLES
## END DECLARE VARIABLES

## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)

class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""

    def setUp(self):
        """ This is docstring for setUp method...
        Method called to prepare the Test Fixture.
        This is called immediately before calling the test method(s)."""
        
        ## DECLARE LIST OF VARIABLES OF FILENAMES
        self.ListOfFileNames = ["main.py", "__init__.py"]

    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        
        ## BEGIN FOR LOOP
        for each in self.ListOfFileNames:
            
            self.assertEqual(main.fn_DoesObjectExist(each), True)
            self.assertTrue(main.fn_DoesObjectExist(each), True)
            
        ## END FOR LOOP

    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""

        ## BEGIN FOR LOOP
        for each in self.ListOfFileNames:
            
            self.assertEqual(main.fn_IsObjectFile(each), True)
            self.assertTrue(main.fn_IsObjectFile(each), True)
          
        ## END FOR LOOP

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
