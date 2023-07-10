#!/usr/bin/python3
""" 
Write a class MyList that inherits from list:
"""


class MyList(list):
    """Class definition"""
    def print_sorted(self):
	"""prints the sorted list"""
        print(sorted(self))
