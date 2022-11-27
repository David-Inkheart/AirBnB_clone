# AirBnB Clone - The Console

  
https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221127%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221127T202758Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8f6f48047020e552dfafc901ab7188ddda873be2a55cb1a05bc87c5e2a059502

Welcome to the AirBnB clone project!

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
