# Project Overview

This project is the beginning (i.e. Step 0) of a multi-step, scalable project that explores the qualities and interesting phenomena of "Tesla Numbers", i.e. numbers divisible by 3, e.g. 3, 6, 9, 12, 15, 18, etc.

Each step will explore additional concepts and features of both Tesla Numbers as well as unit testing.

Each step consists of a number of tasks - each of which will be unit tested.

This Step 0 will test if user input data are valid Tesla Numbers, i.e. if divisible by 3.

In order to gain a better perspective and learn the essential testing concepts, we will first develop our tests using the `unittest` testing library.  Then we will develop the same project with the third-party `pytest` testing library in order to compare testing philosophies, concepts, and features.

`pytest` requires less boilerplate code than the built-in `unittest` testing library which comes as part of the Python Standard Library.  This library contains built-in modules written in Python that provide standardized solutions for many problems that occur in everyday programming.

https://docs.python.org/3/library/

The only dependency that is required for this project is installation of the third-party `pytest` library.

https://docs.pytest.org/en/stable/getting-started.html

# Background

### "If you only knew the magnificence of the 3, 6, and 9, then you would have a key to the universe." - Nikola Tesla

Nikola Tesla was a deep and mysterious man. He sought and discovered hidden laws, facts, and truths of the Universe, and shared them with mankind. As you will come to know, Mathematics is something that is discovered (not invented), Mathematics is the language of the Universe, and Mathematics never lies.  

Nikola Tesla is reputed to have been fascinated unto the point of obsession with the numbers 3, 6, and 9. Indeed, these 3 numbers have special qualities and properties when compared to the other digits in our number system. Watch the video below for a quick introduction.

https://www.youtube.com/watch?v=GnEWOYKgI4o

# `unittest`

The framework implemented by `unittest` supports fixtures, test suites, and a test runner to enable automated testing.(Hellman 2017: 1051)

# Basic Test Structure
Tests, as defined by `unittest`, have two parts:

<ol>
  <li> code to manage test dependencies (called fixtures)</li>
  <li> the test itself.</li>
</ol>

Individual tests are created by subclassing `TestCase` and overriding or adding appropriate methods.(Hellman 2017: 1051)

# Running Tests
The easiest way to run unittest tests is use the automatic discovery available through the command-line interface (CLI).(Hellman 2017: 1051)
`python -m unittest test_unittests.py`

# Project Tasks

You can do this project by completing the Project Tasks:

https://github.com/DanielYohai/PluralsightProject0/blob/master/tasks.md

# References

##### Hellmann, D.;The Python 3 Standard Library by Example, 2017

https://doughellmann.com/blog/the-python-3-standard-library-by-example/

https://www.oreilly.com/library/view/the-python-3/9780134291154/



