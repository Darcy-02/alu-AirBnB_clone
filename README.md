# alu-AirBnB_clone
# AirBnB clone - the sandbox

## Description of the project
we'll start by building a full web application
here, we create a *command interpreter* in python that allows us to supervise the objects of the AirBnB project

the command interpreter should be able to:
- add new objects(incase for an update)
- get an object from a certain file or the database
- do operations on objects 
- delete objects

this is just the beginning, we'll later create a link with the DB storage, web framework and REST API

## Description of the command interpreter

### How to start it
first of all, make sure the file is executable 
chmod 774 console.py

then run the file( interactive mode ) 
./console.py

or run the file (non-interactive mode)
echo "help" | ./console.py

### How to use it
the sandbox should work like a shell but has limits in commands 

- EOF (Exits the program with CTRL+D)
- help (shows available commands)
keep in mind that an empty line and ENTER won't execute anything.

### Examples

*IN INTERACTIVE MODE*
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

*IN NON INTERACTIVE MODE*
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$