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

## Task 1 - Create Python File `main.py`

Begin your project by creating a Python file named `main.py` in the root folder of your project.

We will be using `unittest` to test for the existence of the files that we create.

Within the file `main.py`, import both the `unittest` and `os` modules from the Python Standard Library, as we will be exploring some features of how Python interacts with your local computer file system.

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
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES
## BEGIN DECLARE VARIABLES

NameOfFile = "main.py"

## END DECLARE VARIABLES
## END DECLARE VARIABLES
## END DECLARE VARIABLES
```

Then we will create two custom functions with two built-in Python functions that will 1.) check for the existence of an object within your local file path; and 2.) check if an object is of type file.  Both functions from the `os` library return Boolean values `True` or `False`.

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

Next we will create a class to contain our `unittest` unit tests.  Remember that tests in `unittest` are defined as methods of an instance of the the `unittest.Testcase` subclass, i.e. in this case `cls_Tests`.  The following `test` methods in our class use the `assertEqual` method of the `unittest.Testcase` subclass.  In the first parameter of each assert statement, they call the functions `fn_DoesObjectExist()` and `fn_IsObjectFile()` respectively that return Boolean Values `True` or `False`.  These returned values are then compared with the expected values of `True` (in the second parameter) if the file exists, and the test passes if so.

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

Now run the program, and you should see the following message which tells us that the tests have passed:

```
DoesObjectExist =  True
.IsObjectFile =  True
.
----------------------------------------------------------------------
Ran 2 tests in 0.018s

OK
>>> 
```


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
