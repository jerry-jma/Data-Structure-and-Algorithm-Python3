# Description
# Given a string str containing only 0 or 1, please return the number of substrings that consist of 0 .

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# 1<=|str|<=30000

# Example
# Example 1:

# Input:
# "00010011"
# Output:
# 9
# Explanation:
# There are 5 substrings of "0",
# There are 3 substrings of "00",
# There is 1 substring of "000".
# So return 9
# Example 2:

# Input:
# "010010"
# Output:
# 5
class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """
    def string_count(self, str: str) -> int:
        if not str:
            return 0

        fast = 1
        counter = 0

        for slow in range(len(str)):
            if str[slow] != '0':
                continue
            fast = max(slow + 1, fast)
            while fast < len(str) and str[fast] != '1':
                fast += 1
            counter += fast - slow

        return counter
