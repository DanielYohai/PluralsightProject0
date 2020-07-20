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

As we encounter programming issues, we will refactor our code as necessary.

## Task 1 - Create Python File `main.py`; `self.assertEqual()`

Begin your project by creating a Python file named `main.py` in the root folder of your project.

We will be using `unittest` to test for the existence of the files that we create.

Within the file `main.py`, import both the `unittest` and `os` modules from the Python Standard Library as we will be exploring some features of how Python interacts with your local computer file system.  It will also be necessary to import `pytest` that you just downloaded and installed on your local computer.

```
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import unittest
import pytest
import os

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES
```

A Test Case is created by subclassing `unittest.TestCase`.  Individual tests are defined with methods whose names start with the letters `test`.  This naming convention informs the Test Runner about which methods represent tests.(Reference 2)

Let's create our first Test Case with tests to confirm the existence of the file `main.py`.

Within the file `main.py`, add the following code below the section where you imported modules:

``` 
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES

NameOfFile = "main.py"

## END DECLARE VARIABLES
## END DECLARE VARIABLES
## END DECLARE VARIABLES
```

Then, using two built-in Python functions from the `os` library, we will create two custom functions in order to 1.) check for the existence of an object within your local file path; and 2.) check if an object is of type file.  Both functions from the `os` library return Boolean values `True` or `False`.

```
## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS

def fn_DoesObjectExist(NameOfFile):

    ## CALL FUNCTION - CHECKS IF OBJECT EXISTS IN LOCAL FILE PATH 
    DoesObjectExist = os.path.exists(NameOfFile)

    ## TEST - PRINT OUTPUT TO CONSOLE - THIS WILL GIVE US VISUAL CONFIRMATION THAT THIS FUNCTION WAS CALLED
    print("DoesObjectExist = ", DoesObjectExist)

    ## RETURN VARIABLE --> BOOLEAN TRUE or FALSE
    return(DoesObjectExist)


def fn_IsObjectFile(NameOfFile):

    ## CALL FUNCTION - CHECKS IF OBJECT IS OF TYPE FILE
    IsObjectFile = os.path.isfile(NameOfFile)

    ## TEST - PRINT OUTPUT TO CONSOLE - THIS WILL GIVE US VISUAL CONFIRMATION THAT THIS FUNCTION WAS CALLED
    print("IsObjectFile = ", IsObjectFile)

    ## RETURN VARIABLE --> BOOLEAN TRUE or FALSE
    return(IsObjectFile)

## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS
```

Next we will create a class to contain our `unittest` unit tests.  Remember that tests in `unittest` are defined as methods of an instance of the the `unittest.Testcase` subclass, i.e. in this case `cls_Tests()`.  

The following two `test` methods in our class use the `assertEqual()` assertion method of the `unittest.Testcase` subclass.  In the first parameter of each assertion, it calls the functions `fn_DoesObjectExist()` and `fn_IsObjectFile()` respectively that each return Boolean values of `True` or `False`.  These Boolean values are returned to the `test_` methods that call them, and are compared with the expected values of `True` or `False` that are contained in the second parameter.

Here is a list of `unittest`'s Assert Methods:

https://docs.python.org/3/library/unittest.html#assert-methods

If the file `main.py` exists, then these first two tests will pass.

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True)
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True)

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

Finally, add the following code at the bottom below all other code in order to tie things together.

```
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

if __name__ == "__main__":

    ## EXECUTE UNIT TESTS
    unittest.main()

    
## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER
```

Now run the program, and you should see a message similar to the following which tells us that the tests have passed:

```
DoesObjectExist =  True
.IsObjectFile =  True
.
----------------------------------------------------------------------
Ran 2 tests in 0.018s

OK
>>> 
```

Remember that you can run these unit tests from the Command Line Interface (CLI) with or without the `-v` option for more verbosity.

Test the program from your CLI with `unittest`.

`python -m unittest main.py`

`python -m unittest -v main.py`

Alternatively, you can test the same program with `pytest` and the results message will be similar (yet not identical) to the one returned by `unittest`.

`python -m pytest main.py`

`python -m pytest -v main.py`



## Task 2 - Create Python File `__init__.py`; `self.assertTrue()`

Currently, a view of the entire code script should look like this:

```
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import unittest
import pytest
import os

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES

## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES

NameOfFile = "main.py"

## END DECLARE VARIABLES
## END DECLARE VARIABLES
## END DECLARE VARIABLES

## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS
## BEGIN DEFINE FUNCTIONS

def fn_DoesObjectExist(NameOfFile):

    ## CALL FUNCTION - CHECKS IF OBJECT EXISTS IN LOCAL FILE PATH 
    DoesObjectExist = os.path.exists(NameOfFile)

    ## TEST - PRINT OUTPUT TO CONSOLE - THIS WILL GIVE US VISUAL CONFIRMATION THAT THIS FUNCTION WAS CALLED
    print("DoesObjectExist = ", DoesObjectExist)

    ## RETURN VARIABLE --> BOOLEAN TRUE or FALSE
    return(DoesObjectExist)


def fn_IsObjectFile(NameOfFile):

    ## CALL FUNCTION - CHECKS IF OBJECT IS OF TYPE FILE
    IsObjectFile = os.path.isfile(NameOfFile)

    ## TEST - PRINT OUTPUT TO CONSOLE - THIS WILL GIVE US VISUAL CONFIRMATION THAT THIS FUNCTION WAS CALLED
    print("IsObjectFile = ", IsObjectFile)

    ## RETURN VARIABLE --> BOOLEAN TRUE or FALSE
    return(IsObjectFile)

## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS
## END DEFINE FUNCTIONS

## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True)
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True)

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

if __name__ == "__main__":

    ## EXECUTE UNIT TESTS
    unittest.main()

    
## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER
```

Let's continue our project by creating a Python file named `__init__.py` in the same root folder of your project where we just created the `main.py` file.  The `__init__.py` file makes the directory a Python package with all the features and benefits that this entails.

Within our `unittest.Testcase` subclass `cls_Tests()`, create two more tests.  Change the `assertEqual()` assertion to be `assertTrue()`, and use a text string `"__init__.py"` as the value for the first parameter.  We will find opportunity to refactor this code in a later step.

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True)
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True)

    def test_2A_AssertDoesObjectExist(self):
        """ This is docstring for test_2A_AssertDoesObjectExist..."""
        self.assertTrue(fn_DoesObjectExist("__init__.py"), True)
        
    def test_2B_AssertIsObjectFile(self):
        """ This is docstring for test_2B_AssertIsObjectFile..."""
        self.assertTrue(fn_IsObjectFile("__init__.py"), True)

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

Run your script again, and you should see message similar to the following:

```
DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  True
.IsObjectFile =  True
.
----------------------------------------------------------------------
Ran 4 tests in 0.034s

OK
>>> 
```

## Task 3 - Create a Test that Fails; `self.assertTrue()`; `self.assertFalse()`

So far we have created tests that have all passed.  Now let's intentionally create a test that fails in order to examine the test results message.

Within our `unittest.Testcase` subclass `cls_Tests()`, create two more tests.  Change the `assertEqual()` assertion to be `assertTrue()`, and use a text string `"NoFile.py"` as the value for the first parameter to test and compare with the value of the second parameter (which is what we expect to be returned from a successful unit test).

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True)
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True)

    def test_2A_AssertDoesObjectExist(self):
        """ This is docstring for test_2A_AssertDoesObjectExist..."""
        self.assertTrue(fn_DoesObjectExist("__init__.py"), True)
        
    def test_2B_AssertIsObjectFile(self):
        """ This is docstring for test_2B_AssertIsObjectFile..."""
        self.assertTrue(fn_IsObjectFile("__init__.py"), True)

    def test_3A_AssertDoesObjectExist(self):
        """ This is docstring for test_3A_AssertDoesObjectExist..."""
        self.assertTrue(fn_DoesObjectExist("NoFile.py"), True)
        
    def test_3B_AssertIsObjectFile(self):
        """ This is docstring for test_3B_AssertIsObjectFile..."""
        self.assertTrue(fn_IsObjectFile("NoFile.py"), True)

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

## Task 4 - Modify the Test to Pass; `self.assertTrue()`; `self.assertFalse()`

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True)
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True)

    def test_2A_AssertDoesObjectExist(self):
        """ This is docstring for test_2A_AssertDoesObjectExist..."""
        self.assertTrue(fn_DoesObjectExist("__init__.py"), True)
        
    def test_2B_AssertIsObjectFile(self):
        """ This is docstring for test_2B_AssertIsObjectFile..."""
        self.assertTrue(fn_IsObjectFile("__init__.py"), True)

    def test_3A_AssertDoesObjectExist(self):
        """ This is docstring for test_3A_AssertDoesObjectExist..."""
        self.assertFalse(fn_DoesObjectExist("NoFile.py"), False)
        
    def test_3B_AssertIsObjectFile(self):
        """ This is docstring for test_3B_AssertIsObjectFile..."""
        self.assertFalse(fn_IsObjectFile("NoFile.py"), False)

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```



## Task X - 

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
