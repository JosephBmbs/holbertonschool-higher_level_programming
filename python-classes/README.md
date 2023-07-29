# <div align="center">Python - Classes and Objects</div>

<div align="center">
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" alt="Python Logo">
</div>

## Table of Contents
- [Background Context](#background-context)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Introduction](#introduction)
- [Classes and Objects](#classes-and-objects)
- [Attributes and Methods](#attributes-and-methods)
- [Properties and Getters/Setters](#properties-and-getterssetters)
- [Data Abstraction, Encapsulation, and Information Hiding](#data-abstraction-encapsulation-and-information-hiding)
- [Dynamic Attributes and Binding](#dynamic-attributes-and-binding)
- [The `__dict__` Attribute](#__dict__-attribute)
- [Finding Attributes in Python](#finding-attributes-in-python)

## Background Context
In this project, we delve into the world of Object-Oriented Programming (OOP) using Python. It is crucial to read and understand the provided resources before proceeding with the tasks. OOP is a powerful paradigm that allows us to model real-world entities as objects, enabling code organization, reusability, and maintainability.

## Resources
Make sure to read or watch the following resources in the order presented:

1. [Object-Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod, and staticmethod yet)
2. [Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
3. [Properties vs. Getters and Setters](https://www.programiz.com/python-programming/property)
4. [Learn to Program 9: Object-Oriented Programming](https://www.youtube.com/watch?v=YXPyB4XeYLA)
5. [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
6. [Object-Oriented Programming](https://www.geeksforgeeks.org/object-oriented-programming-in-python/)

## Learning Objectives
By the end of this project, you will be able to explain the following concepts to anyone without relying on external references:

1. Understanding the concept of Object-Oriented Programming (OOP).
2. Grasping the principle of "first-class everything" in Python.
3. Defining classes and objects, understanding the difference between them.
4. Identifying and using attributes with public, protected, and private access levels.
5. Exploring the role of `self` in Python classes and methods.
6. Utilizing the special `__init__` method for object initialization.
7. Understanding Data Abstraction, Encapsulation, and Information Hiding.
8. Exploring properties and their difference from attributes in Python.
9. Implementing Pythonic getters and setters.
10. Creating dynamic attributes for existing instances of a class.
11. Understanding attribute binding for objects and classes.
12. Exploring the `__dict__` attribute of a class and/or instance.
13. Learning how Python finds attributes for objects and classes.
   
## Requirements
Ensure you meet the following requirements:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should follow the `pycodestyle` rules (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

A documentation is not just a simple word, it’s a real sentence explaining the purpose of the module, class, or method. The length of it will be verified.

## Author
Youssef Saad
