"""Wmls."""


def sum_multiples(n):
    """Knlxa."""
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print(sum_multiples(1000))


def even_sum(n):
    """Knlxa."""
    total = 2
    a = 1
    b = 2
    c = 3
    while c < n:
        if c % 2 == 0:
            total += c
    c = a + b
    a = b
    b = c
    return total


print(even_sum(4000000))


def max_palindrome(n):
    """Khan."""
	
