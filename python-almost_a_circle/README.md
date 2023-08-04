<p align="center">Python - Almost a Circle</p>
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/600px-Python-logo-notext.svg.png" alt="Python Logo">
</p>

This repository contains the source code and test files for the "Almost a Circle" project in Python. In this project, we will review various concepts related to Python, including import, exceptions, classes, private attributes, getters/setters, class methods, static methods, inheritance, unittest, and file read/write operations.

## Background Context

The "Almost a Circle" project covers a wide range of Python concepts and techniques, allowing us to deepen our understanding of the language. Throughout this project, we will encounter various topics such as serialization/deserialization, JSON handling, *args and **kwargs, and more.

## Step-by-step Guide

1. **Write the first class Base**: This class will serve as the base for all other classes in the project. It will manage the 'id' attribute and ensure that each instance has a unique identifier.

2. **Write the class Rectangle**: Inherit from the Base class to create the Rectangle class. Implement validation for all setter methods and instantiation (excluding the 'id' attribute).

3. **Add area() method to Rectangle**: Implement a public method 'area()' that calculates and returns the area of the Rectangle instance.

4. **Display method for Rectangle**: Add a public method 'display()' that prints the Rectangle instance using the character '#'.

5. **Override str method for Rectangle**: Override the '__str__' method in the Rectangle class to return the representation '[Rectangle] instance'.

6. **Enhance the display method for Rectangle**: Improve the 'display()' method to print the Rectangle instance considering the 'x' and 'y' coordinates.

7. **Update method for Rectangle**: Add a public method 'update(self, *args)' that assigns arguments to each attribute of the Rectangle.

8. **Update method with kwargs for Rectangle**: Modify the 'update()' method to accept key/value arguments and update the corresponding attributes.

9. **Write the class Square**: Inherit from the Rectangle class to create the Square class.

10. **Getter and Setter for Square**: Add public getter and setter methods for the 'size' attribute in the Square class.

11. **Update method for Square**: Implement the 'update()' method in the Square class to assign arguments to the Square attributes.

12. **to_dictionary method for Rectangle and Square**: Add a public method 'to_dictionary()' to both Rectangle and Square classes to return their dictionary representation.

13. **Class method savetofile() for Base**: Add a class method 'savetofile(cls, listobjs)' to the Base class to write the JSON string representation of a list of objects to a file.

14. **Static method fromjsonstring() for Base**: Include a static method 'fromjsonstring(jsonstring)' in the Base class to return a list of objects from a JSON string.

15. **Class method create() for Base**: Implement a class method 'create(cls, dictionary)' in the Base class to create an instance with attributes already set.

16. **Class method loadfromfile() for Base**: Add a class method 'loadfromfile(cls)' to the Base class to return a list of instances from a file.

## Learning Objectives

After completing this project, you will be able to:

- Understand Unit testing and implement it in a large project.
- Serialize and deserialize a Class using JSON.
- Read and write JSON files in Python.
- Utilize *args and **kwargs for handling variable-length arguments in functions.
- Handle named arguments in Python functions effectively.

## Requirements

- Python Scripts:
  - Allowed editors: vi, vim, emacs
  - All files interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
  - Files should end with a new line.
  - The first line of all files should be exactly "#!/usr/bin/python3".
  - A README.md file at the root of the folder is mandatory.
  - Code should follow pycodestyle (version 2.7.*).
  - All files must be executable.
  - The length of files will be tested using wc.
  - All modules, classes, and functions should be documented.

- Python Unit Tests:
  - Allowed editors: vi, vim, emacs
  - Files should end with a new line.
  - All test files should be inside a folder named 'tests'.
  - unittest module must be used for writing test cases.
  - All tests should be executed using 'python3 -m unittest discover tests'.
  - File organization in the 'tests' folder should match the project structure.

We encourage collaboration on test cases to ensure coverage of all possible edge cases.

**Happy coding!**

## Author
Youssef Saad 
