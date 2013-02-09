#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jon
#
# Created:     09/02/2013
# Copyright:   (c) Jon 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        print memo.keys()
        return memo[x]
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fib = memoize(fib)

print(fib(400))