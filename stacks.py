# -*- coding: utf-8 -*-

from utils import Empty


class ArrayStack(object):

    def __init__(self):
        self._arr = []

    def __len__(self):
        return len(self._arr)

    def is_empty(self):
        return len(self._arr) == 0

    def push(self, e):
        self._arr.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._arr[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._arr.pop()


class LinkedStack(object):

    class _Node(object):

        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Empty stack!')
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e


if __name__ == '__main__':

    s = ArrayStack()

    print 'Empty stack? {}'.format(s.is_empty())

    for i in xrange(5):
        s.push(i)

    print 'Stack length: {}'.format(len(s))
    print 'Stack top: {}'.format(s.top())

    for i in xrange(5):
        print s.pop()

    s = LinkedStack()

    print 'Empty stack? {}'.format(s.is_empty())

    for i in xrange(5):
        s.push(i)

    print 'Stack length: {}'.format(len(s))
    print 'Stack top: {}'.format(s.top())

    for i in xrange(5):
        print s.pop()

