# Description
# A mirror number is a number that looks the same when rotated 180 degrees (looked at upside down).For example, the numbers "69", "88", and "818" are all mirror numbers.

# Write a function to determine if a number is mirror. The number is represented as a string.

# Example
# Example 1:

# Input : "69"
# Output : true
# Example 2:

# Input : "68"
# Output : false

class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        if not num:
            return False
        hash_map = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in hash_map or num[left] != hash_map[num[right]]:
                return False
            left += 1
            right -= 1

        return True