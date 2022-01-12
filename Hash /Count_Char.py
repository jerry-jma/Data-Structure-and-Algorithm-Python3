# Description
# Count characters in a string. Return a hash map which key is character and value is the occurrency of this character.

# Example
# Example 1:

# Input:
# str = "abca"

# Output:
# {
#   "a": 2,
#   "b": 1,
#   "c": 1
# }
# Example 2:

# Input:
# str = "ab"

# Output:
# {
#   "a": 1,
#   "b": 1
# }

class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here

        results = {}
        for char in str:
            if char in results:
                results[char] += 1
            else:
                results[char] = 1
        return results

        # hashmap = {}
        # for char in str:
        #     hashmap[char] = hashmap.get(char, 0) + 1
        # return hashmap