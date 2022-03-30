# Description
# Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.

# A and B are strings which are composed of numbers
# Example
# Example1:
# Input:
# A = "99"
# B = "111"
# Output: "11010"
# Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1,connect them，so answer is "11010"
# Example2:
# Input:
# A = "2"
# B = "321"
# Output: "323"
# Explanation: because 2 + 1 = 3, 2 + 0 = 2, 3 + 0 = 3, connect them，so answer is "323"

class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return the sum of two strings
    """
    def sumof_two_strings(self, a: str, b: str) -> str:
        index_a, index_b = len(a) - 1, len(b) - 1

        result = ''
        while index_a >= 0 and index_b >= 0:
            str_a = a[index_a]
            str_b = b[index_b]
            curr_total = int(str_a) + int(str_b)

            result = str(curr_total) + result

            index_a -= 1
            index_b -= 1

        while index_a >= 0:
            result = a[index_a] + result
            index_a -= 1

        while index_b >= 0:
            result = b[index_b] + result
            index_b -= 1

        return result