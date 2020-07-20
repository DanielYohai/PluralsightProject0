# Project Tasks

You can do this project by completing the Project Tasks:

https://github.com/DanielYohai/PluralsightProject0/blob/master/tasks.md

# Project Overview

This project is the beginning (i.e. Step 0) of a multi-step, scalable project that explores the qualities and interesting phenomena of "Tesla Numbers", i.e. numbers divisible by 3, e.g. 3, 6, 9, 12, 15, 18, etc.

Each step will explore additional concepts and features of both Tesla Numbers as well as unit testing.  Along the way, we will also learn and/or reinforce various Python concepts.

Each step consists of a number of tasks - each of which will be unit tested.

This Step 0 will begin by testing if input data are valid Tesla Numbers by the `%` MODULO operation, i.e. if divisible by 3, i.e.:

```
if x % 3 == 0: ## IF x % (MODULO, i.e. DIVIDED BY) 3 LEAVES A REMAINDER OF 0 (ZERO)...
  ## ...THEN x IS DIVISIBLE BY 3, AND THEREFORE A VALID TESLA NUMBER 

else:
  ## ...OTHERWISE x IS NOT DIVISIBLE BY 3, AND THEREFORE NOT A VALID TESLA NUMBER
```

However, first we must create modules (i.e. Python files) as a workspace to do our calculations, and we will use both `unittest` and `pytest` to confirm the creation and existence of the files that we create.  

In order to gain a better perspective and learn the essential testing concepts - for each step and task in the project - we will first develop our tests using the `unittest` testing library.  Later we will develop the same steps and tasks a second time (i.e. practice!!) with the third-party `pytest` testing library in order to compare testing philosophies, concepts, and features.

`pytest` requires less boilerplate code than the built-in `unittest` testing library which comes as part of the Python Standard Library.  This library contains built-in modules written in Python that provide standardized solutions for many problems that occur in everyday programming.

https://docs.python.org/3/library/

Another great advantage of `pytest` is it can run the tests that you develop in `unittest`, and `pytest` supports running Python `unittest`-based tests out of the box.   Concretely, `pytest` will automatically collect `unittest.TestCase` subclasses and their `test` methods in `test` files.  You should be able to run your `unittest`-style tests if they are contained in `test_*.py` or `*_test.py` modules [i.e. Python files]. Thus, it's possible to leverage existing `unittest`-based Test Suites by using `pytest` as a Test Runner which also allows to incrementally adapt the Test Suite to take full advantage of `pytest`'s features.  If that works for you then you can make use of most of these `pytest` features.

https://docs.pytest.org/en/3.0.1/unittest.html

Almost all `unittest` features are supported in `pytest`:

https://docs.pytest.org/en/stable/unittest.html

Full `pytest` documentation can be found here:

https://docs.pytest.org/en/3.0.1/contents.html

The only dependency that is required for this project is installation of the third-party `pytest` library.

https://docs.pytest.org/en/stable/getting-started.html

# Background

### "If you only knew the magnificence of the 3, 6, and 9, then you would have a key to the universe." - Nikola Tesla

Nikola Tesla was a deep and mysterious man. He sought and discovered hidden laws, facts, and truths of the Universe, and shared them with mankind. As you will come to know, Mathematics is something that is discovered (not invented), Mathematics is the language of the Universe, and Mathematics never lies.  

Nikola Tesla is reputed to have been fascinated unto the point of obsession with the numbers 3, 6, and 9. Indeed, these 3 numbers have special qualities and properties when compared to the other digits in our number system. Watch the video below for a quick introduction.

https://www.youtube.com/watch?v=GnEWOYKgI4o

# `unittest`

The `unittest` Unit Testing Framework is part of the Python Standard Library. 

https://docs.python.org/3/library/unittest.html

The framework implemented by `unittest` supports Test Fixtures, Test Suites, and a Test Runner to enable automated testing.(Hellman 2017: 1051) `unittest` supports some important concepts in an object-oriented way such as Test Fixture, Test Case, Test Suite, Test Runner:

https://docs.python.org/3/library/unittest.html


# Basic Test Structure
Tests, as defined by `unittest`, have two parts:

<ol>
  <li> code to manage test dependencies (called fixtures)</li>
  <li> the test itself.</li>
</ol>

The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for correctness. In `unittest`, test cases are represented by `unittest.TestCase` instances. To make your own test cases you must write subclasses of `TestCase` or use `FunctionTestCase`.(Reference 2).  That is to say, individual tests are created by subclassing `TestCase` and overriding or adding appropriate methods.(Hellman 2017: 1051)

# Running Tests
The easiest way to run `unittest` tests is use the automatic discovery available through the Command-Line Interface (CLI).(Hellman 2017: 1051)

`python -m unittest test_unittests.py`

For more detailed test results, include the `-v` option for more verbosity.
(Hellman 2017: 1052)

`python -m unittest -v test_unittests.py`

Alternatively, you can place the following code in your scripts so that tests are executed when the script is run:

```
if __name__ == '__main__':
    unittest.main()
```

# Project Tasks

You can do this project by completing the Project Tasks:

https://github.com/DanielYohai/PluralsightProject0/blob/master/tasks.md

# References

##### 1.) Hellmann, D.;The Python 3 Standard Library by Example, 2017

https://doughellmann.com/blog/the-python-3-standard-library-by-example/

https://www.oreilly.com/library/view/the-python-3/9780134291154/

##### 2.)  https://docs.python.org/3/library/unittest.html



