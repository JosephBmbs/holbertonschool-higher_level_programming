<h1 align="center">Python - Test-driven development</h1>

<p align="center">
  <img src="https://www.python.org/static/img/python-logo.png" alt="Python Logo">
</p>


![Weight: 1](https://img.shields.io/badge/Weight-1-blue)

Your score will be updated as you progress.

## Background Context

### Important notice on intranet checks for Python projects

Starting from today:

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything.
- The intranet checks for Python projects won't be released before their first deadline, in order for you to focus more on TDD (Test-driven development) and think about all possible cases.
- We strongly encourage you to work together on test cases, so that you don't miss any edge case. But not in the implementation of them!
- Don't trust the user, always think about all possible edge cases.

### Resources

Read or watch:

- [doctest — Test interactive Python examples (until "26.2.3.7. Warnings" included)](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://realpython.com/python-testing/#writing-your-first-test)
- [Writing Effective Documentation](https://realpython.com/documenting-python-code/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

1. Why Python programming is awesome.
2. What's an interactive test.
3. Why tests are important.
4. How to write Docstrings to create tests.
5. How to write documentation for each module and function.
6. What are the basic option flags to create tests.
7. How to find edge cases.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A README.md file, at the root of the folder of the project, is mandatory.
- Your code should use the pycodestyle (version 2.7.*).
- All your files must be executable.
- The length of your files will be tested using wc.

### Python Test Cases

- Allowed editors: vi, vim, emacs.
- All your files should end with a new line.
- All your test files should be inside a folder `tests`.
- All your test files should be text files (extension: `.txt`).
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`.
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- A documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- We strongly encourage you to work together on test cases, so that you don't miss any edge case – The Checker is checking for tests!

## How to Run Tests

To execute the test cases, use the following command:

```bash
python3 -m doctest ./tests/*
```

## Contributors

- Guillaume - [GitHub](https://github.com/your_username)

---

This is a template for a professional README file. Please make sure to replace `your_username` in the `Contributors` section with your actual GitHub username.

## Author
Youssef Saad
