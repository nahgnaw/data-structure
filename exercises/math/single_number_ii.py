# -*- coding: utf-8 -*-

"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3
        result = 0

        for i in xrange(32):
            bit_sum = 0
            # The bit sum of those numbers appearing three times on the ith bit must be 3n
            for x in nums: 
                bit_sum += ((x >> i) & 1)
            result |= ((bit_sum % k) << i) # restore the single number

        if result >= 2 ** 31:
            result -= 2 ** 32
        return result