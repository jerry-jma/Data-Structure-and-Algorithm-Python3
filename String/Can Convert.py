# Description
# Given two string S and T, determine if S can be changed to T by deleting some letters (including 0 letter)

# Wechat reply 【1540】 get the latest requent Interview questions . (wechat id : jiuzhang15)

# Example
# Example1

# Input: S = "lintcode" and T = "lint"
# Output: true
# Example2

# Input: S = "lintcode" and T = "ide"
# Output: true
# Example3

# Input: S = "adda" and T = "aad"
# Output: false
# Explanation: You can not change "adda" to "aad" by deleting one 'd'.


class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # if not s or not t or len(s) < len(t):
        #     return False
        # index_holder = []
        # for (i, elem) in enumerate(t):
        #     if s.find(elem) < 0:
        #         return False
        #     index_holder.append(s.find(elem))
        # if len(index_holder) <= 1:
        #     return True
        # for i in range(len(index_holder)-1):
        #     curr = index_holder[i]
        #     next_elem = index_holder[i+1]
        #     if curr > next_elem:
        #         return False
        # return True

        if not s or not t or len(s) < len(t):
            return False
        index_T = 0

        for char in s:
            if char == t[index_T]:
                index_T += 1
                if index_T == len(t):
                    return True

        return False


