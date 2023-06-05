
			General
	Why Python programming is awesome
	Who created Python
	Who is Guido van Rossum
	Where does the name ‘Python’ come from
	What is the Zen of Python
	How to use the Python interpreter
	How to print text and variables using print
	How to use strings
	What are indexing and slicing in Python
	What is the official Python coding style and how to check your code with pycodestyle

			Requirements
		Python Scripts
	Allowed editors: vi, vim, emacs
	All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	All your files should end with a new line
	The first line of all your files should be exactly #!/usr/bin/python3
	A README.md file at the root of the repo, containing a description of the repository
	A README.md file, at the root of the folder of this project, is mandatory
	Your code should use the pycodestyle (version 2.8.*)
	All your files must be executable
	The length of your files will be tested using wc

		Shell Scripts
	Allowed editors: vi, vim, emacs
	All your scripts will be tested on Ubuntu 20.04 LTS
	All your scripts should be exactly two lines long (wc -l file should print 2)
	All your files should end with a new line
	The first line of all your files should be exactly #!/bin/bash
	All your files must be executable

			TASKS
	0) Write a Shell script that runs a Python script.
		The Python file name will be saved in the environment variable $PYFILE
			guillaume@ubuntu:~/py/0x00$ cat main.py 
			#!/usr/bin/python3
			print("Best School")

			guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
			guillaume@ubuntu:~/py/0x00$ ./0-run
			Best School
			guillaume@ubuntu:~/py/0x00$ 
	1) write a Shell script that runs Python code.
		The Python code will be saved in the environment variable $PYCODE
			export PYCODE='print(f"Best School: {88+10}")'
			guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
			Best School: 98
	2) Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
	3) The output of the script should be:
		the number, followed by Battery street, followed by a new line
		output should be like this: 98 Battery street
	4) The output of the program should be: Float: 3.14
		Float:, followed by the float with only 2 digits, followed by a new line
		You are not allowed to cast number to string
		You have to use f-strings
	5) You can find the source code here
		The output of the program should be: Holberton SchoolHolberton SchoolHolberton School
Holberton
			3 times the value of str
			followed by a new line
			followed by the 9 first characters of str, followed by a new line
	6) output for concatenating the 2 strings should be Welcome to Holberton School!
		you have to use both str1 and str2
	7) Your program should be exactly 8 lines long
		word_first_3 should contain the first 3 letters of the variable word
		word_last_2 should contain the last 2 letters of the variable word
		middle_word should contain the value of the variable word without the first and last letters
		First 3 letters: Hol, Last 2 letters: on, Middle word: olberto
	8) str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
		print(str)
		your code should print object-oriented programming with Python, followed by a new line.
	9) Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
	10) Write a function in C that checks if a singly linked list has a cycle in it.
		Prototype: int check_cycle(listint_t *list);
		Return: 0 if there is no cycle, 1 if there is a cycle
	11) Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.
			Use the function write from the sys module
			You are not allowed to use print
			Your script should print to stderr
			Your script should exit with the status code 1
	12) Write a script that compiles a Python script file.
		The Python file name will be stored in the environment variable $PYFILE
		The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
	13) Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode
		  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
		
				THE END :)
