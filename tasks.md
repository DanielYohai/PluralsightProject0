# Project 0 Tasks
<br />The tasks for this Project 0 are as follows:

## Task 0 - Install `pytest`

Pytest is not part of the Python Standard Library.  For this project's unit testing, it will be necessary to install third-party `pytest` library on your local development platform:

https://docs.pytest.org/en/stable/getting-started.html

After installing `pytest`, check that the library has been properly installed by confirming the version with either of the following commands:

`py.test --version`

`pytest --version`

Both commands should return output that is similar to the following, but will vary according to your specific local development environment:

`This is pytest version 5.4.1, imported from c:\python380\lib\site-packages\pytest\__init__.py`

If you do not see a message similar to the one above, then `pytest` wasn't installed properly, and you will need to troubleshoot and solve this issue before you can proceed with the Projects Tasks.

## Task 1 - Create Python File `main.py`

Begin your project by creating a Python file named `main.py` in the root folder of your project.

We will be using `unittest` to test for the existence of the files that we create.

Within the file `main.py`, import the following `unittest` and `os` modules from the Python Standard Library:

```
import unittest
import os
```



However, as this project scales, it will be increasingly difficult to test things manually, and therefore we will first use `unittest` and then `pytest` to automate our unit testing.



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
