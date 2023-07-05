#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """
    @text = must be a string, otherwise raise a TypeError exception with the
    message text must be a string
    """
    if isinstance(text, (str)) is False or text is None:
        raise TypeError("text must be a string")
    l = len(text) - 1
    buffer = []
    for idx, char in enumerate(text):
        buffer.append(char)
        if char == ':' or char == '.' or char == '?':
            print("".join(buffer).strip())
            print()
            buffer = []
        elif idx == l:
            print("".join(buffer).strip(), end="")
