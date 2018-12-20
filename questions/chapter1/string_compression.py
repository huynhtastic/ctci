"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2blc5a3. If the "compressed" string would not become smaller
than the original string, your method should return the original string. You
can assume the string has only uppercase and lowercase letters (a - z).
"""

def compress_string(string):
	len_str = 0
	len_compress = 0
	prev_letter = None
	compressed_string = ''

	for letter in string:
		if prev_letter == None:
			prev_letter = letter
			compressed_string += letter
            len_compress += 1
        elif prev_letter == letter:





# Is checking the length of a string O(n) or O(1)?
# Are string comparisons O(m * n) or O(1)?
