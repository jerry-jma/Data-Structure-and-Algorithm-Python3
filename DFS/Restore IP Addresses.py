# Description
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# (Your task is to add three dots to this string to make it a valid IP address. Return all possible IP address.)

# You can return all valid IP address in any order.

# Example
# Example 1:

# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# Explanation: ["255.255.111.35", "255.255.11.135"] will be accepted as well.
# Example 2:

# Input: "1116512311"
# Output: ["11.165.123.11","111.65.123.11"]

from typing import (
    List,
)

class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restore_ip_addresses(self, s: str) -> List[str]:
        result = []
        self.helper(s, [], result)
        return result

    def helper(self, s, path, result):
        # exit.
        if len(path) == 4 and s == '':
            result.append('.'.join(path))
            return

        if len(path) > 4:
            return

        for i in range(1, 4):
            if i > len(s):
                break

            curr_str = s[:i]
            # take care the leading 0s
            to_num = int(curr_str)
            to_str = str(to_num)
            if len(curr_str) != len(to_str):
                continue

            if int(curr_str) > 255 or int(curr_str) < 0:
                continue

            path.append(curr_str)
            self.helper(s[i:], path, result)
            path.pop()







