# -*- coding: utf-8 -*-

"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
"""


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while n:
            # The characters left in buf4 will lost in the next call of read().
            # Therefore read() can only be called once.
            buf4 = [''] * 4
            tmp = read4(buf4)
            if not tmp:
                return index
            for i in xrange(min(tmp, n)):
                buf[index] = buf4[i]
                index += 1
                n -= 1
        return index
