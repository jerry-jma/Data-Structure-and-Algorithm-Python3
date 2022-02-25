# Description
# Prime factorize a given integer.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# You should sort the factors in ascending order.

# Example
# Example 1:

# Input: 10
# Output: [2, 5]
# Example 2:

# Input: 660
# Output: [2, 2, 3, 5, 11]

from typing import (
    List,
)

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def prime_factorization(self, num: int) -> List[int]:
        result = []
        up = int(math.sqrt(num))

        k = 2

        while k <= up:
            while num % k == 0:
                num = num // k
                result.append(k)
            k += 1

        if num != 1:
            result.append(num)

        return result
