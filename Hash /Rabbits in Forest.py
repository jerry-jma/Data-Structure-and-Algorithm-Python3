# Description
# In a forest, each rabbit has a color. Some of rabbits (possibly all of them) will tell you how many other rabbits have the same color as them. Those answers are placed in an array.

# Return the minimum number of rabbits that could be in the forest.

# The giver array will have length at most 1000.
# Each element in the array will be an integer in the range [0, 999].
# Example
# Example 1:

# Input: [1, 1, 2]
# Output: 5
# Explanation:
#   The two rabbits that answered "1" could both be the same color, say red.
#   The rabbit than answered "2" can't be red or the answers would be inconsistent.
#   Say the rabbit that answered "2" was blue.
#   Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
#   The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
# Example 2:

# Input: [10, 10, 10]
# Output: 11

class Solution:
    """
    @param answers: some subset of rabbits (possibly all of them) tell
    @return: the minimum number of rabbits that could be in the forest.
    """
    def numRabbits(self, answers):
        # write your code here
        total = 0
        hash = {}

        for answer in answers:
            hash[answer] = hash.get(answer, 0) + 1

        for k,v in hash.items():
            rabbits_per_group = k + 1
            num_of_group = v // k

            if v % k != 0:
                num_of_group += 1

            total += rabbits_per_group * num_of_group

        return total