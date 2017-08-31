# Investigate texts and calls

Project Overview
================
In this Project, you will complete five tasks based on a fabricated set of calls and texts exchanged during September 2016. You will use Python to analyze and answer questions about the texts and calls contained in the dataset.

What will I learn?
---------------------------
After completing this Proejct, you'll be able to:

* Design and write your own Python programs to perform real-life tasks,
* program in Python on your own computer,
* write Python code that is readable and conforms to [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines,
* process string and numerical data in Python,
* choose and use Python's built-in data structures,
* use Internet resources to help you,
* use Python's built-in functions and write your own functions and
* use loops and conditional statements in Python.

Why this Project?
-------------
You'll apply the skills you've learned so far in a realistic scenario. The five tasks are structured to give you experience with a variety of programming problems. You will receive code review of your work; this personal feedback will help you to improve your Python programming.

How to prepare for the Project
------
To prepare for this Project, first complete the course materials of Part 1 of Introduction to Python Programming. If you're already confident that you have the skills listed above, feel free to try the project and jump back into the course materials if you find you need to refresh your knowledge. 

Project Details
================
In this Lab, you'll complete five tasks to answer questions about telephone calls and text messages from a fabricated data for a set of calls and texts exchanged during September 2016. 

Step 1
--------
Download and open the zipped folder [here](https://github.com/udacity/cn-python-foundation.git). Under folder `investigate texts and calls` You will find five python files `Task0.py` ~ `Task4.py` and two csv files `calls.csv` and `texts.csv`

About the data
---------
The text and call data are provided in csv files. In each file, the data is already read and stored as lists of lists. 

Each sub-list of the list of texts is structured in this way:

```
a text = [	Sending telephone number (string),
		receiving telephone number (string), 
		timestamp of text message (string)]
```
Each element in the list of phone calls is structured in this way:

```
a call = [	Calling telephone number (string), 
		receiving telephone number (string), 
		start timestamp of telephone call (string),
		duration of telephone call in seconds (string)]
```

All telephone numbers are 10 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number.
There are three different kinds of telephone numbers, each with a different format:

* Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: `(022)40840621`.
* Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: `93412 66159`.
* Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: `1402316533`.

Step 2
----------
Complete the five tasks by the instructions in the files. 

Do not change the data or instructions, simply add your code below what has been provided.

Include all the code that you need for each task in that file. 

The solution outputs for each file should be the print statements described in the instructions. Feel free to use other print statements during the development process, but remember to remove them for submission - the submitted files should print only the solution outputs.

Step 3
---------
Use the rubric to check your work before submission. A Udacity Reviewer will give feedback on your work based on this rubric and will leave helpful comments on your code.

| Criteria| Meets Specifications|
| ------------- |:-------------|
| code quality      | Your code should be well-structured and readable, following best practices explained in the course. |
| Print only the solutin outputs | Feel free to use other print statements during the development process, but remember to remove them for submission      |
| Task 0 successful | The script correctly prints out the infomation of first record of texts and last record of calls      |
| Task 1 successful | The script correctly prints number of distinct telephone numbers in the dataset.      |
| Task 2 successful |The script correctly prints the telephone number that spent the longest time on the phone and the the total time in seconds they spend on phone call.|
| Task 3 successful |The script correctly prints the telephone codes called by fixed-line numbers in Bangalore and the proportion of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.      |
| Task 4 successful |The script correctly prints the list of numbers that could be telemarketers.     |

Submission
======
Submit a zip file named as **submit.zip** with **ONLY** the following files:

- Task0.py
- Task1.py
- Task2.py
- Task3.py
- Task4.py
