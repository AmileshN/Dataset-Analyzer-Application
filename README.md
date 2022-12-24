# Dataset Analyzer Program Version 1.0  

###### ECOR 1042 Winter 2022 
###### Date: 11/04/2022

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### The Dataset Analyzer Program team leader can be reached at:
**Team Leader Name**: Amilesh Nanthakumaran
**Voice**: 123-456-7890 
**Website**: www.amileshn.com
**Email**: amileshnanthakumaran@cmail.carleton.ca

## Description 
- The project analyzes a subset of the Google Books dataset in the 
programming language Python. This is achieved using multiple modules to load the dataset, add and remove books, and presents the user multiple methods to analyze the dataset such as getting all the books by title or sorting books by author.
- The project is made up of 5 files and 2 sample datasets:
	- T030_check_equal.py:			A module that is used for automated testing of functions to ensure they work properly
	- T030_P5_load_data.py:			A module for reading and loading the data from the dataset file, organizes the books by category
	- T030_add_remove_search_dataset.py:	A module that contains the functionalities to add and remove books and retrieve different books by title, rate, publisher,category or author 
	- T030_sorting_fun.py:			A module that contains the functionalities to sort the dataset by title, rate, publisher or author
	- T030_P4_booksUI.py:			A module that contains the interactive user interface that will allow the user to load, manipulate and analyze the dataset
	- google_books_dataset.csv:		A sample dataset that can be analyzed by the program
	- test_dataset_P2.csv: A smaller version of google_books_dataset.csv 

## Installation 
Python **3.8.2** or later must be installed. 
Only built-in Python modules are used. No external modules must be loaded.


## Usage
  
With python installed, run this in the command line:
```
>>> python T030_P4_booksUI.py
```
The interactive user interface will run:
``` 	
	The available commands are:
	    1- L)oad data
	    2- A)dd book
	    3- R)emove book
	    4- G)et books
			 T)itle R)ate P)ublisher A)uthor
	    5- GCT)Get all Categories for book Title
	    6- S)ort books
			 T)itle R)ate P)ublisher A)uthor
	    7- Q)uit

	Please type your command:  
```
When prompted, enter a command to execute that functionality. Some functions will ask for more prompts such as the file name or book title. To utilize commands 2-6, the dataset must be loaded or the message "_File not loaded_" will be returned. To load the dataset, enter L when prompted to enter a command.
``` 	
	The available commands are:
	    1- L)oad data
	    2- A)dd book
	    3- R)emove book
	    4- G)et books
			 T)itle R)ate P)ublisher A)uthor
	    5- GCT)Get all Categories for book Title
	    6- S)ort books
			 T)itle R)ate P)ublisher A)uthor
	    7- Q)uit

	Please type your command: L  
```

When prompted enter the name of the file to be loaded and that file will be loaded.
```
Enter the name of the file to be loaded: google_books_dataset.csv
```
Make sure the dataset is in the **same folder** as the project and the dataset has Title, Author, Rating (0.0-5.0, inclusive), Publisher, Pages,Category, Language in the header in that order. If an invalid command is entered, the message "_No such command_" will be returned. Entering '_Q_' will terminate the program.
``` 	
	The available commands are:
	    1- L)oad data
	    2- A)dd book
	    3- R)emove book
	    4- G)et books
			 T)itle R)ate P)ublisher A)uthor
	    5- GCT)Get all Categories for book Title
	    6- S)ort books
			 T)itle R)ate P)ublisher A)uthor
	    7- Q)uit

	Please type your command: Q 
```

```
Q was entered, terminating the program
```
## Credits 
1. Amilesh Nanthakumaran:
	1. Load data module 
	2. Get books by category function
	3. Get books by title function
	4. Sort books by title function 
	5. Load data function in booksUI module 
	6. Display function in booksUI module 
	7. Get books function in booksUI module 
	8. Get all categories for book title function in booksUI module
2. George Reda Gad:
	1. Add book function 
	2. Get books by author function 
	3. Dict to list function 
	4. Sort books by author function 
	5. Sort data function in booksUI module
	6. Checks equal function in check_equals module
3. Ayo Owolabi:
	1. Get books by rate function 
	2. Get books by publisher function 
	3. Sort books by ascending rate function 
	4. Get books function in booksUI module 
4. Eliana Schartner:
	1. Remove book function 
	2. Get all categories for book title function 
	3. Sort books by publisher function 
	4. Add remove book function in booksUI module


#### MIT License

Copyright (c) 2022 Amilesh Nanthakumaran, George Reda Gad, Ayo Owolabi, and Eliana Schartner  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.