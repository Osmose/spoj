#!/usr/bin/env python
"""
42. Adding Reversed Numbers

http://www.spoj.com/problems/ADDREV/
"""

if __name__ == '__main__':
    cases = input()
    for case in range(cases):
        first, second = raw_input().split()
        result = int(first[::-1]) + int(second[::-1])
        print unicode(result)[::-1].lstrip('0')
