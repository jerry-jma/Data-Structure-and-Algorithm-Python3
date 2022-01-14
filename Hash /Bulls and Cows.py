# Description
# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret number and friend's guess, use Ato indicate the bulls and B to indicate the cows.

# Please note that both secret number and friend's guess may contain duplicate digits.

# You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

# Example
# Example 1:

# Input：secret = "1807", guess = "7810"
# Output："1A3B"
# Explanation：1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
# Example 2:

# Input：secret = "1123", guess = "0111"
# Output："1A1B"
# Explanation：The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

class Solution:
    """
    @param secret: An string
    @param guess: An string
    @return: An string
    """
    def getHint(self, secret, guess):
        # secret_num = [0] * 10
        # guess_num = [0] * 10

        # bulls, cows = 0, 0

        # for i in range(len(secret)):
        #     curr_secret_num = int(secret[i])
        #     curr_guess_num = int(guess[i])
        #     if curr_secret_num == curr_guess_num:
        #         bulls += 1
        #     secret_num[curr_secret_num] += 1
        #     guess_num[curr_guess_num] += 1
        # print(secret_num, guess_num)

        # counter = 0
        # for i in range(len(secret_num)):
        #     counter += min(secret_num[i], guess_num[i])

        # return f'{bulls}A{counter - bulls}B'

        bulls, cows = 0, 0
        tracker = [0] * 10

        for secret_num, guess_num in zip(secret, guess):
            if secret_num == guess_num:
                bulls += 1
            else:
                tracker[int(secret_num)] += 1
                tracker[int(guess_num)] -= 1

        counter = 0
        for num in trackers:
            if num >= 1:
                counter += num

        return f'{bulls}A{len(secret) - bulls - counter}'