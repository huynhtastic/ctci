"""
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""

def is_unique(string):
    """Determines if a string has all unique characters in-place.

    First we sort the values [O(n * log(n))] then compare each letter with the
    letter after it.

    Time: O(n * log(n))
    Space: O(1)
    """
    string = ''.join(sorted(string))
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            return False
    return True
