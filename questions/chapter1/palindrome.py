"""
Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palindrome. A palindrome is a word or phrase that is the same
forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""

def palindrome_perm(string):
    """
    This solution goes through each letter once and adds letters into a
    dictionary. If the dictionary contains a letter that we have seen
    before, we pop out that letter from the dictionary.

    This allows us to keep track of letters that have a matching pair for
    the palindrome as a palindrome contains at most 1 letter without a
    matching pair.

    Time: O(n) with n being # of characters
    Space: O(n)
    """
    mem = {}
    for letter in string.lower():
        if letter.isalpha():
            print(mem)
            if letter in mem:
                mem.pop(letter)
            else:
                mem[letter] = 1
    return len(mem) < 2
