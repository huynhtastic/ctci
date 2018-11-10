"""
Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other.
"""

def check_perm(perm, string):
    """Check if a string is a permutation of the other.

    First we check if the lengths of the strings match (can't be a permutation
    if they're different lengths). If they are valid candidates of each other,
    then we go through each letter of both string and compare the letters. If
    they don't match, we check a dictionary to see if we've seen these letters
    before. If we have, we delete the letter entry from the dictionary. If we
    haven't, we add them into the dictionary to check later letters in the
    strings.

    To determine if the strings are permutations, we check if our found
    dictionary is empty.

    Time: O(n)
    Space: O(n)

    """
    if len(perm) != len(string):
        return False
    founds = {}
    for i in range(len(perm)):
        if perm[i] != string[i]:
            # then we check dict
            if perm[i] not in founds:
                founds[perm[i]] = 1
            else:
                del founds[perm[i]]
            if string[i] not in founds:
                founds[string[i]] = 1
            else:
                del founds[string[i]]
    return bool(founds) == False
