#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
<<<<<<< HEAD

    Float arguments are typecasted to ints before addition is performed.

=======
    
    Float arguments are typecasted to ints before addition is performed.
    
>>>>>>> a94a2611d7df335c1503544e9154e2722a8ae485
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
