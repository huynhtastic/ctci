"""
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

def one_away(first, second):
    """
    This approach goes through each letter in the first word and keeps track
    of the count of each letter.

    We then go through each letter in the second word and subtract from the
    count of each letter from the memorized dictionary. If the entry in the
    dictionary goes to 0, we get rid of that entry altogether to mark that
    we have exhausted the count in the first word.

    If there are letters in the second word that aren't in the first word,
    we add it to another memorization list, but this time we don't need to
    keep track of the counts for comparisons. We can just see if there are
    a lot of letters in the second word that the first word doesn't have.

    If there are more than two entries in either the dictionary or list, we
    say that there is more than one edit needed to match the words.

    Time: O(f+s) where f is # of letters in first and s is # of letters in
          second
    Space: O(f+s) where f is # of letters in first and s is # of letters in
           second

    Worst-case time: Worst case is best case as we will need to always
        loop through all letters in f and s.
    Worst-case space: All of the letters in first aren't in second and
        vice-versa. This means we need to hold all of the letters as none
        of them will be popped.
    """
    mem = {}
    for letter in first:
        if letter in mem:
            mem[letter] += 1
        else:
            mem[letter] = 1
    mems = []
    for letter in second:
        if letter in mem:
            if mem[letter] == 1:
                mem.pop(letter)
            else:
                mem[letter] -= 1
        else:
            mems.append(letter)
        print(mem)
    return len(mem) < 2 and len(mems) < 2
