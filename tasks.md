# Project 0 Tasks
<br />The tasks for this Project 0 are as follows:

## Task 0 - Install `pytest`

`pytest` is not part of the Python Standard Library.  For this project's unit testing, it will be necessary to install third-party `pytest` library on your local development platform:

https://docs.pytest.org/en/stable/getting-started.html

After installing `pytest`, check that the library has been properly installed by confirming the version with either of the following commands:

`py.test --version`

`pytest --version`

Both commands should return output that is similar to the following, but will vary according to your specific local development environment:

`This is pytest version 5.4.1, imported from c:\python380\lib\site-packages\pytest\__init__.py`

If you do not see a message similar to the one above, then `pytest` wasn't installed properly, and you will need to troubleshoot and solve this issue before you can proceed with the Projects Tasks.

As this project scales, it will be increasingly difficult to test things manually, and therefore we will first use `unittest` and then `pytest` to automate our unit testing throughout.

## Task 1 - Create Python File `main.py`

Begin your project by creating a Python file named `main.py` in the root folder of your project.

We will be using `unittest` to test for the existence of the files that we create.

Within the file `main.py`, import the following `unittest` and `os` modules from the Python Standard Library:

```
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import unittest
import os

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES
```

A testcase is created by subclassing `unittest.TestCase`.  Individual tests are defined with methods whose names start with the letters `test`.  This naming convention informs the test runner about which methods represent tests.(Reference 2)

Let's create our first testcase with tests to confirm the existence of the file `main.py`.

Within the file `main.py`, add the following code below the section where you imported modules:

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
    
    def setUp(self):
        """ This is docstring for setUp method...
        Method called to prepare the test fixture.
        This is called immediately before calling the test method."""
        pass
        
    def tearDown(self):
        """ This is docstring for tearDown method...
        Method called immediately after the test method has been
        called and the result recorded."""
        pass

    def test_Assert1(self):
        """ This is docstring for test_Assert1..."""
        self.assertTrue(0, True)
    
    def test_AssertDoesObjectExistInDirectory(self):
        """ This is docstring for test_AssertDoesObjectExistInDirectory..."""
        self.assertTrue(os.path.exists, True)
        
    def test_AssertIsObjectFile(self):
        """ This is docstring for AssertIsObjectFile..."""
        self.assertTrue(os.path.isfile, True)
        
       
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

## Task 2 - 

Within the file `main.py`, create a Python list object called variable `t` that will be a List of a Range of Tesla Numbers (from 3 to 3000) to be defined as all numbers that are divisible by 3. The range will start at integer 3 and continue until integer 3003 in steps of 3, and thus will include all multiples of 3 including the integer 3000 (but not including integer 3003), i.e. a total of 1000 integer numbers.

Most testing follows the Arrange-Act-Assert Model which will be explained throughout.
```
## DECLARE VARIABLES - ARRANGE - i.e. ARRANGE THE VARIABLES AND CONDITIONS TO BE TESTED
t = list(range(3,3003,3))

## TESTING PURPOSES - TEST MANUALLY - PRINT OUTPUT - 
print(type(t))
print(len(t))
```

Run the program from your IDLE, IDE, or Command Line Interface (CLI), and you will see the following output:

``` 
<class 'list'>
1000
```
