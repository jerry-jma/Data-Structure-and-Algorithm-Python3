# Description
# Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

# Example
# Example1

# Input: "123"
# Output: [["1","2","3"],["12","3"],["1","23"]]
# Example2

# Input: "12345"
# Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        if not s:
            return [[]]

        result = []
        self.helper(s, [], result)
        return result

    def helper(self, s, combo, result):
        # exit
        if len(s) == 0:
            result.append(combo[:])
            return

        for i in range(2):
            if i+1 <= len(s):
                combo.append(s[:i+1])
                self.helper(s[i+1:], combo, result)
                combo.pop()
