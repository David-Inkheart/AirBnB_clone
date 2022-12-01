# AirBnB Clone - The Console

  
## Getting Started

**This console is a command line interpreter for the AirBnB clone**

> we want to be able to manage the objects of our project:


- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object


## General Learning Objectives

 - How to create a Python package
   
  - How to create a command interpreter in Python using the cmd module
   
   - What is Unit testing and how to implement it in a large project
   
   - How to serialize and deserialize a Class
   
   - How to write and read a JSON file
   
   - How to manage datetime
   
   - How to use UUID
   
   - How to *args and how to use it
   
   - How **kwargs and how to use it
   
   - How to handle named arguments in a function



## Execution

  
This shell works like this in interactive mode:

  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```

## Usage Examples

**Launching the console**
```
$ ./console.py
(hbnb)
```
**Creating a new object**
```
(hbnb) create
** class name missing **
(hbnb) create User
49faff9a-6318-451f-87b6-910505c55907
```
**Show an object**
```
(hbnb) show User
** instance id missing **
(hbnb) show User 49faff9a-6318-451f-87b6-910505c55907
[User] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(
2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907',
 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
**Update an object**
```
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907
** attribute name missing **
(hbnb) update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) all
["[User] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(
2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907',
'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300), "first_name": "Betty"}"]
(hbnb)
```
**Destroy an object**
```
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
(hbnb) destroy User 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
(hbnb) quit
$
```
