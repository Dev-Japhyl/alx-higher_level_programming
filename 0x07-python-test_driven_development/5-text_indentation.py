#!/usr/bin/python3
"""
matrix_divided - a function that divides all elements of a matrix.
Returns a new matrix
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    beg = 0
    for idx, val in enumerate(text):
        if val in '?:.':
            print(text[beg:idx + 1].strip() + '\n')
            beg = idx + 1
    if not beg:
        print(text, end='')
    elif beg is not len(text):
        print(text[beg:idx + 1].strip(), end='')
