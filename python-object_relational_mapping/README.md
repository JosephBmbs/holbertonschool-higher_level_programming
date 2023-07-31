<div align="center">
  <h1>Python - Object-relational mapping (ORM)</h1>
  <img src="https://hackernoon.imgix.net/images/sEWElcuzkCV0XfEQdlHmORnljWk2-i2037u5.png" alt="ORM Image">
</div>

## Introduction

Welcome to the Python - Object-relational mapping (ORM) project! In this project, we will explore the exciting world of connecting databases and Python using Object-Relational Mapping (ORM). The primary goal of ORM is to abstract the storage from the usage, allowing us to interact with the database using Python objects, rather than writing raw SQL queries.

## Before You Start

Before diving into the project, please ensure that your MySQL server is version 8.0. If you are using Ubuntu 20.04, you can follow the steps below to install MySQL 8.0:

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$ 
```

## Background Context

In this project, we will focus on two main parts:

1. Using the `MySQLdb` module to connect to a MySQL database and execute SQL queries.
2. Utilizing the `SQLAlchemy` module, an Object-Relational Mapper (ORM), to interact with the database using Python objects.

The major advantage of using an ORM is that we no longer need to write SQL queries directly. Instead, we will focus on manipulating Python objects. Furthermore, an ORM allows us to easily switch between different storage systems without significant changes to our code.

Let's see a quick example to understand the difference between using `MySQLdb` and `SQLAlchemy`.

**Without ORM:**

```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

**With ORM:**

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from my_module import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

As you can see, the ORM approach provides a more Pythonic and abstracted way to interact with the database.

## Resources

Before you start the project, we recommend reading or watching the following resources:

- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://www.tutorialspoint.com/python/python_database_access.htm)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Introduction to SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [10 common stumbling blocks for SQLAlchemy newbies](https://www.codementor.io/@mirko0/10-common-stumbling-blocks-for-sqlalchemy-newbies-3mj20hjuf0)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

## Learning Objectives

By the end of this project, you should be able to explain the following topics to anyone without the need for external help:

- How to connect to a MySQL database from a Python script.
- How to SELECT rows in a MySQL table from a Python script.
- How to INSERT rows in a MySQL table from a Python script.
- Understanding the concept of Object-Relational Mapping (ORM).
- How to map a Python Class to a MySQL table.

## Requirements

To work on this project, you must meet the following requirements:

- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- Your files will be executed with MySQLdb version 2.0.x.
- Your files will be executed with SQLAlchemy version 1.4.x.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should adhere to the PEP8 style guide (pycodestyle version 2.7.*).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'` to check).
- All your classes should have documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` to check).
- All your functions (inside and outside a class) should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` to check).
- A documentation is not just a simple word; it's a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- You are not allowed to use `execute` with SQLAlchemy.

## Installation

To install MySQLdb version 2.0.x, ensure that MySQL is installed and then run the following commands:

```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

To install SQLAlchemy version 1.4.x, use the following command:

```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Please note that you might encounter a warning message during the installation, but you can ignore it.

## Author 
Youssef Saad 
