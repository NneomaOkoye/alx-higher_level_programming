#!/bin/python3
# Author - Okoye Nneoma

def remove_char_at(str, n):
    if n < 0:
        return (str)
    eturn (str[:n] + str[n+1:])
