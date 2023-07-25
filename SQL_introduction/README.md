<p align="center">SQL - Introduction</p>

<p align="center">
  <img src="https://media0.giphy.com/media/vISmwpBJUNYzukTnVx/giphy.gif" alt="SQL Logo">
</p>

## Concepts
For this project, we expect you to look at this concept:

- Databases

## Resources
Read or watch:
- [What is Database & SQL?](https://www.youtube.com/watch?v=HXV3zeQKqGY)
- [Install MySQL (MySQL Server)](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Basic SQL statements: DDL and DML](https://www.ibm.com/docs/en/db2/11.5?topic=statements-data-definition-data-manipulation)
- [Basic queries: SQL and RA](https://webdam.inria.fr/Jorge/files/IF/SQL-Slides-1.pdf)
- [SQL technique: functions](https://www.w3schools.com/sql/sql_functions.asp)
- [SQL technique: subqueries](https://www.tutorialspoint.com/sql/sql-sub-queries.htm)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402326/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe)
- [MySQL Cheat Sheet](https://www.sqlshack.com/mysql-cheat-sheet/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## More Info
### Comments for your SQL file:
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```

### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
```

### Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```

### Use the sandbox to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
```bash
$ service mysql start
 * Starting MySQL database server mysqld 
$
```

```bash
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
```

In the container, credentials are root/root

---

This README file provides an overview of the SQL - Introduction project. It includes relevant information about the topics covered, resources for learning, and the learning objectives. The README also provides details on the requirements and instructions on how to set up MySQL 8.0 on Ubuntu 20.04 LTS. It concludes with additional information about using MySQL within the provided sandbox environment.

## Author
Youssef Saad
