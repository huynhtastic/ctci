"""
URLify: Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
(Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE
Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
"""

def urlify(string, true_length):
    """Returns a string with all spaces replaced with %20.

    For in-place purposes, we convert the string to a bytearray and discount
    this from our complexity.

    We make a single-scan approach where we have two points, left and right.
    Left scans the string for chars and spaces and right holds the place where
    we either swap characters or entre the %20.

    Worst case, we have something like '     s          ', where the true_length
    is 6 but it's filled with spaces. This will make our right and left meet at
    the beginning of the string. This makes it 2n pases where n is the number
    of characters.

    Time: O(n)
    Space: O(1)
    """

    string = bytearray(string, 'utf-8')
    right = len(string) - 1
    left = true_length - 1
    while left != right:
        if chr(string[left]).isalnum():
            string[right] = string[left]
            right -= 1
        else:
            for char in '02%':
                string[right] = ord(char)
                right -= 1
        left -= 1
    return string
