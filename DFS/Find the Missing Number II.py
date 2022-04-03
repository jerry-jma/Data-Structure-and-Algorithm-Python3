# Description
# To give a random string sequence composed of 1 - n integers, in which an integer is lost, please find it.

# n < 100
# Data guarantees have only one solution.
# if the list that you've found has more than one missing numbers, which could be that you didn't find the correct way to split the string.

# Example
# Example1

# Input: n = 20 and str = 19201234567891011121314151618
# Output: 17
# Explanation:
# 19'20'1'2'3'4'5'6'7'8'9'10'11'12'13'14'15'16'18
# Example2

# Input: n = 6 and str = 56412
# Output: 3
# Explanation:
# 5'6'4'1'2

class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def find_missing2(self, n: int, str: str) -> int:
        result = []
        self.helper(n, str, set(), result)
        total = 0

        for i, val in enumerate(result[0]):
            total += int(val)

        return n*(n+1)//2 - total

    def helper(self, n, str, combo, result):
        if str == '' and len(combo) == n - 1:
            result.append(list(combo))
            return

        if str and str[0] == '0':
            return

        for i in range(1, 3):
            if i > len(str):
                break

            num = str[:i]

            if int(num) > n or int(num) < 0 or num in combo:
                continue

            # add this condition here will got RuntimeError
            # if i == 2 and num[0] == '0':
                # continue

            combo.add(num)
            self.helper(n, str[i:], combo, result)
            combo.remove(num)











