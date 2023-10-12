#!/usr/bin/python3
"""Minimum operations quiz"""


def minOperations(n):
    """Minimum operations"""
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
