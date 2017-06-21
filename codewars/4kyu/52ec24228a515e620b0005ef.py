"""Explosive Sum

https://www.codewars.com/kata/52ec24228a515e620b0005ef/train/python

How many ways can you make the sum of a number?

From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples

Trivial

sum(-1) # 0
sum(1) # 1
Basic

sum(2) # 2  -> 1+1 , 2
sum(3) # 3 -> 1+1+1, 1+2, 3
sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

sum(10) # 42
Explosive

sum(50) # 204226
sum(80) # 15796476
sum(100) # 190569292
See here for more examples.

http://blog.chinaunix.net/uid-26548237-id-3503956.html

"""
import doctest


def partition(n, m):
    if n < 0 or m < 0:
        return 0
    if n == 1 or m == 1:
        return 1
    if n == m:
        return partition(n, m - 1) + 1
    if n > m:
        return partition(n, m - 1) + partition(n - m, m)
    if n < m:
        return partition(n, n - 1) + 1


def exp_sum3(n):
    if n < 0:
        return 0
    dp = {(i, j): 0 for i in range(n + 1) for j in range(n + 1)}
    dp[(0, 0)] = 1
    for i in range(1, n + 1):
        for j in range(0, n + 1):
            if j >= i:
                dp[(i, j)] = dp[(i - 1, j)] + dp[(i, j - i)]
            else:
                dp[(i, j)] = dp[(i - 1, j)]
    return dp[(n, n)]


def exp_sum4(n):
    if n < 0:
        return 0
    dp = {(i, j): 0 for i in range(n + 1) for j in range(n + 1)}
    dp[(0, 0)] = 1
    for i in range(1, n + 1):
        for j in range(0, n + 1):
            dp[(i, j)] = dp[(i - 1, j)]
            if j >= i:
                dp[(i, j)] += dp[(i, j - i)]
    return dp[(n, n)]


def exp_sum2(n):
    if n < 0:
        return 0
    dp = [1] + [0] * n
    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]
    return dp[-1]


def exp_sum(n):
    """
    Basic Example:
    >>> exp_sum(-1)
    0
    >>> exp_sum(1)
    1
    >>> exp_sum(2)
    2
    >>> exp_sum(3)
    3
    >>> exp_sum(4)
    5
    >>> exp_sum(5)
    7
    >>> exp_sum(10)
    42
    >>> exp_sum(50)
    204226
    >>> exp_sum(80)
    15796476

    :param n:
    :return:
    """
    return exp_sum4(n)


if __name__ == '__main__':
    doctest.testmod()
