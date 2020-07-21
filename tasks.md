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

As this project scales, it will become increasingly difficult to test things manually, and therefore we will first use `unittest` and then `pytest` to automate our unit testing throughout.

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
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

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
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

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

Let's continue our project by creating another Python file named `__init__.py` in the same root folder of your project where we just created the `main.py` file.  The `__init__.py` file makes the directory a Python package with all the features and benefits that this entails.

Within our `unittest.Testcase` subclass `cls_Tests()`, create two more tests.  Change the `assertEqual()` assertion to be `assertTrue()`, and use a text string `"__init__.py"` as the value for the first parameter.  We will find opportunity to refactor this code in a later step.

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

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

## Task 3 - Create a Test that Fails; `self.assertTrue()`

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
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

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

Run the unit tests in both `unittest` and `pytest`, and both Test Frameworks confirm that these last two tests fail because indeed no such file exists within our project's root directory with the name `"NoFile.py"`.

```
DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  False
FIsObjectFile =  False
F
======================================================================
FAIL: test_3A_AssertDoesObjectExist (__main__.cls_Tests)
This is docstring for test_3A_AssertDoesObjectExist...
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python380\test\main.py", line 79, in test_3A_AssertDoesObjectExist
    self.assertTrue(fn_DoesObjectExist("NoFile.py"), True)
AssertionError: False is not true : True

======================================================================
FAIL: test_3B_AssertIsObjectFile (__main__.cls_Tests)
This is docstring for test_3B_AssertIsObjectFile...
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python380\test\main.py", line 83, in test_3B_AssertIsObjectFile
    self.assertTrue(fn_IsObjectFile("NoFile.py"), True)
AssertionError: False is not true : True

----------------------------------------------------------------------
Ran 6 tests in 0.062s

FAILED (failures=2)
>>> 
```

## Task 4 - Modify the Test to Pass; `self.assertFalse()`

Now let's modify these last two tests so that they will pass.  Since we are expecting no such file to exist, change the `assertTrue()` assertion to be `assertFalse()`, and change the second parameter to `False`. 

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
    
class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""
      
    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

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

Since we are expecting these two unit tests to return `False` when they check for the existence of the non-existent file `"NoFile.py"`, these two tests now pass successfully.

```
DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  False
.IsObjectFile =  False
.
----------------------------------------------------------------------
Ran 6 tests in 0.058s

OK
>>> 
```

## Task 5 - Refactor Code:  Separate Functionalities

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
        self.assertEqual(fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

    def test_2A_AssertDoesObjectExist(self):
        """ This is docstring for test_2A_AssertDoesObjectExist..."""
        self.assertTrue(fn_DoesObjectExist("__init__.py"), True)
        
    def test_2B_AssertIsObjectFile(self):
        """ This is docstring for test_2B_AssertIsObjectFile..."""
        self.assertTrue(fn_IsObjectFile("__init__.py"), True")

    def test_3A_AssertDoesObjectExist(self):
        """ This is docstring for test_3A_AssertDoesObjectExist..."""
        self.assertFalse(fn_DoesObjectExist("NoFile.py"), False)
        
    def test_3B_AssertIsObjectFile(self):
        """ This is docstring for test_3B_AssertIsObjectFile..."""
        self.assertFalse(fn_IsObjectFile("NoFile.py"), False)

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

However, even though we have separated our code sections (i.e. IMPORT MODULES, DECLARE VARIABLES, DEFINE FUNCTIONS, DEFINE CLASSES, MAIN PROGRAM) with comments, the script is nonetheless becoming quite large and will become more difficult to maintain as the code base grows.  In order to make it easier to maintain, let's begin to separate our code into separate modules, packages, etc.

In your project's root directory, create a new Python file, and name it `test_unittests.py`.  Within this file, create sections for each of the following:  IMPORT MODULES, DECLARE VARIABLES, DEFINE CLASSES:

Within the section for importing modules, import the modules `unittest` and `main`.  We need to import the `main.py` module because we will need access to the functions that we declared there.

```
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import unittest
import main

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES
```

We will also need to move the variable `NameOfFile` that we declared in the `main.py` module to the `test_unittest.py` module.

```
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES

NameOfFile = "main.py"

## END DECLARE VARIABLES
## END DECLARE VARIABLES
## END DECLARE VARIABLES
```

From the `main.py` module, cut the code that contains your `unittest.TestCase` subclass, i.e. `cls_Tests()`, and paste it in the `test_unittest.py` module.  Since the functions that we will call are still located in the `main.py` module, it will be necessary to import this module in order to gain access to the objects contained there.

It will be necessary to refactor our test assertions with PYTHONIC MODULE.FUNCTION DOT.NOTATION, e.g.:

```
self.assertEqual(main.fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
self.assertEqual(main.fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")
self.assertTrue(main.fn_DoesObjectExist("__init__.py"), True)
self.assertTrue(main.fn_IsObjectFile("__init__.py"), True)
self.assertFalse(main.fn_DoesObjectExist("NoFile.py"), False)
self.assertFalse(main.fn_IsObjectFile("NoFile.py"), False)

```

Thus your code for the test class and its test methods should look like the following:

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)

class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""

    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(main.fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(main.fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")

    def test_2A_AssertDoesObjectExist(self):
        """ This is docstring for test_2A_AssertDoesObjectExist..."""
        self.assertTrue(main.fn_DoesObjectExist("__init__.py"), True)
        
    def test_2B_AssertIsObjectFile(self):
        """ This is docstring for test_2B_AssertIsObjectFile..."""
        self.assertTrue(main.fn_IsObjectFile("__init__.py"), True)

    def test_3A_AssertDoesObjectExist(self):
        """ This is docstring for test_3A_AssertDoesObjectExist..."""
        self.assertFalse(main.fn_DoesObjectExist("NoFile.py"), False)
        
    def test_3B_AssertIsObjectFile(self):
        """ This is docstring for test_3B_AssertIsObjectFile..."""
        self.assertFalse(main.fn_IsObjectFile("NoFile.py"), False)
   
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

Within the `main.py` module, import the module `test_unittests.py`:

```
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES
## BEGIN IMPORT MODULES

import unittest
import pytest
import os
import test_unittests

## END IMPORT MODULES
## END IMPORT MODULES
## END IMPORT MODULES
```

If we ran the `main.py` module now, it would not run any unit tests since the tests are now located in a separate module, i.e. `test_unittests.py`.  Therefore, it will be necessary to refactor the code snippet `unittest.main()` to include reference to where the unit tests are located:   `unittest.main(module=test_unittests)`

Therefore your code in the section for the MAIN PROGRAM in the file `main.py` should now look like this:

```
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

if __name__ == "__main__":

    ## EXECUTE UNIT TESTS
    unittest.main(module=test_unittests)
    
    
## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM
```

Now run the `main.py` script from your IDE, and all the tests should pass:

```
DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  False
.IsObjectFile =  False
.
----------------------------------------------------------------------
Ran 6 tests in 0.051s

OK
>>> 
```

However, if you try to run these tests from the CLI, the following commands will not work since the unit tests are now located in the `test_unittests.py` module:

```
python -m unittest main.py
python -m unittest -v main.py
python -m pytest main.py
python -m pytest -v main.py
```

Therefore, if you wish to run these tests from the CLI, you will have to specify the current location of the unit tests:

```
python -m unittest test_unittests.py
python -m unittest -v test_unittests.py
python -m pytest test_unittests.py
python -m pytest -v test_unittests.py
```

Run the tests from the CLI, and you should receive a success message similar to the following:

```
DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  True
.IsObjectFile =  True
.DoesObjectExist =  False
.IsObjectFile =  False
.
----------------------------------------------------------------------
Ran 6 tests in 0.003s

OK
>>> 
```

## Task 6 - Refactor Code:  Combine Assertion Statements

We can refactor our tests to be more concise by gathering the assertions into two tests only, each with three assertions.

```
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)
## BEGIN DEFINE CLASSES (UNITTESTS)

class cls_Tests(unittest.TestCase):
    """ This is docstring for the class cls_Tests..."""

    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        self.assertEqual(main.fn_DoesObjectExist(NameOfFile), True, "Should be True:  Object should exist")
        self.assertTrue(main.fn_DoesObjectExist("__init__.py"), True)
        self.assertFalse(main.fn_DoesObjectExist("NoFile.py"), False)
        
    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""
        self.assertEqual(main.fn_IsObjectFile(NameOfFile), True, "Should be True:  Object should be of type file")
        self.assertTrue(main.fn_IsObjectFile("__init__.py"), True)
        self.assertFalse(main.fn_IsObjectFile("NoFile.py"), False)

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

Run the tests, and you should see a success message.  Note that we have reduced our tests from six to two, each with three assertion statements.  We can see from the output printed to the console that the six assertion statements still make six calls to the functions in `main.py`.

```
DoesObjectExist =  True
DoesObjectExist =  True
DoesObjectExist =  False
.IsObjectFile =  True
IsObjectFile =  True
IsObjectFile =  False
.
----------------------------------------------------------------------
Ran 2 tests in 0.041s

OK
>>> 
```


## Task 7 - Refactor Code:  Multiple Variables

As it is forseeable that we may need to unit test for the existence of multiple files, we need to refactor this code.  Within your `test_unittests.py` module, define a new class method called `setUp()`.  The `setUp()` method contains the Text Fixtures that are necessary to prepare data or processes for subsequent tests.

Within the `setUp` method, create an attribute of the class called `self.ListOfFileNames` which will contain a list of file names whose existence will be unit tested.  Then alter the code of your two tests to contain a `for` loop that will iterate through the file names.  Replace the static parameters contained within the current tests (i.e. `NameOfFile`, `"__init__.py"`, `"NoFile.py"`) with the `for` loop's iteration variable `each`. 

Since we have now refactored code to include multiple variables, we can now delete the variable declaration `NameOfFile = "main.py"` that we declared earlier.

```
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
        self.ListOfFileNames = ["main.py", "__init__.py", "NoFile.py"]

    def test_1A_AssertDoesObjectExist(self):
        """ This is docstring for test_1A_AssertDoesObjectExist..."""
        
        ## BEGIN FOR LOOP
        for each in self.ListOfFileNames:
            
            self.assertEqual(main.fn_DoesObjectExist(each), True, "Should be True:  Object should exist")
            self.assertTrue(main.fn_DoesObjectExist(each), True)
            self.assertFalse(main.fn_DoesObjectExist(each), False)
            
        ## END FOR LOOP

    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""

        ## BEGIN FOR LOOP
        for each in self.ListOfFileNames:
            
            self.assertEqual(main.fn_IsObjectFile(each), True, "Should be True:  Object should be of type file")
            self.assertTrue(main.fn_IsObjectFile(each), True)
            self.assertFalse(main.fn_IsObjectFile(each), False)
            
        ## END FOR LOOP

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
``` 

Run the tests, and note that they have failed:

```
DoesObjectExist =  True
DoesObjectExist =  True
DoesObjectExist =  True
FIsObjectFile =  True
IsObjectFile =  True
IsObjectFile =  True
F
======================================================================
FAIL: test_1A_AssertDoesObjectExist (test_unittests.cls_Tests)
This is docstring for test_1A_AssertDoesObjectExist...
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python380\test\test_unittests.py", line 44, in test_1A_AssertDoesObjectExist
    self.assertFalse(main.fn_DoesObjectExist(each), False)
AssertionError: True is not false : False

======================================================================
FAIL: test_1B_AssertIsObjectFile (test_unittests.cls_Tests)
This is docstring for test_1B_AssertIsObjectFile...
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python380\test\test_unittests.py", line 56, in test_1B_AssertIsObjectFile
    self.assertFalse(main.fn_IsObjectFile(each), False)
AssertionError: True is not false : False

----------------------------------------------------------------------
Ran 2 tests in 0.048s

FAILED (failures=2)
>>> 
```

The tests failed because we have passed each filename through a `for` loop to both tests, and therefore all three filenames must be tested against all three assertions.  The two files that exist (i.e. `"main.py"` and `__init__.py`) will not pass the `assertFalse()` assertion, and the file that does not exist (i.e. `"NoFile.py"`) will not pass the `assertEqual()` and `assertTrue()` assertions.  

Therefore, we must make some architectural decisions, and refactor our code.

Since we are essentially concerned with testing for the presence of files that we expect to exist, we can remove the `"NoFile.py"` element from our `self.ListOfFileNames` class attribute, as well as remove the `assertFalse()` statements from our two tests.

```
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
            
            self.assertEqual(main.fn_DoesObjectExist(each), True, "Should be True:  Object should exist")
            self.assertTrue(main.fn_DoesObjectExist(each), True)
            
        ## END FOR LOOP

    def test_1B_AssertIsObjectFile(self):
        """ This is docstring for test_1B_AssertIsObjectFile..."""

        ## BEGIN FOR LOOP
        for each in self.ListOfFileNames:
            
            self.assertEqual(main.fn_IsObjectFile(each), True, "Should be True:  Object should be of type file")
            self.assertTrue(main.fn_IsObjectFile(each), True)
          
        ## END FOR LOOP

## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
## END DEFINE CLASSES (UNITTESTS)
```

Run the tests again, and you see that they now all pass for each variable.  Note that we pass two variables (i.e. `"main.py"` and `"__init__.py"`) to two tests that each have two assertions, i.e. 2 x 2 x 2 = 8 function calls, and therefore 8 `print()` statements are executed:

```
DoesObjectExist =  True
DoesObjectExist =  True
DoesObjectExist =  True
DoesObjectExist =  True
.IsObjectFile =  True
IsObjectFile =  True
IsObjectFile =  True
IsObjectFile =  True
.
----------------------------------------------------------------------
Ran 2 tests in 0.077s

OK
>>> 
```

## Conclusion

Congratulations!  If you have made it this far, then you have successfully completed Step 0 to set up the unit testing frameworks and files.

Now that we have our initial files set up and successfully unit tested, we will continue next time with our study and examination of the mathematics of Tesla Numbers.
