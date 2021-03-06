# Description
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

# Wechat reply the【BAT】get the latest frequent Interview questions of ByteDance, Alibaba, etc. (wechat id :jiuzhang15)

# Example
# Example 1:

# Input：["0010","0110","0100"]，x=0，y=2
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0,1), and the lower right coordinate is (2,2).
# Example 2:

# Input：["1110","1100","0000","0000"], x = 0, y = 1
# Output：6
# Explanation：
# The upper left coordinate of the matrix is (0, 0), and the lower right coordinate is (1,2).

from typing import (
    List,
)

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0

        row_len = len(image)
        col_len = len(image[0])

        left = self.find_first(image, 0, y, self.check_column)
        right = self.find_last(image, y, col_len-1, self.check_column)
        up = self.find_first(image, 0, x, self.check_row)
        down = self.find_last(image, x, row_len-1, self.check_row)

        return (right - left + 1) * (down - up + 1)

    def find_first(self, image, start, end, check_func):
        while start + 1 < end:
            mid = (start + end) // 2
            if check_func(image, mid):
                end = mid
            else:
                start = mid

        if check_func(image, start):
            return start

        return end

    def find_last(self, image, start, end, check_func):
        while start + 1 < end:
            mid = (start + end) // 2
            if check_func(image, mid):
                start = mid
            else:
                end = mid

        if check_func(image, end):
            return end

        return start

    def check_column(self, image, col):
        for i in range(len(image)):
            if image[i][col] == '1':
                return True
        return False

    def check_row(self, image, row):
        for j in range(len(image[0])):
            if image[row][j] == '1':
                return True

        return False
