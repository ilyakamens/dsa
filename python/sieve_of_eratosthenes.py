__author__ = 'ilyakamens'
__date__ = '9/6/14'


def get_sieve(n):
    """Uses Eratosthenes's algorithm to determine whether each number
    from 0 - n is prime.

    :param n:   The max number to determine if it's prime
    :return:    None if n < 2, otherwise an array of booleans, where each
                boolean represents whether the number is prime
    """
    if n < 2:
        return None

    nums = [False, False]   # We know 0 and 1 aren't prime
    for i in xrange(2, n + 1):
        nums.append(True)

    for i in xrange(2, int(n**.5)):
        if nums[i]:
            # for j = i^2, i^2 + i, i^2 + 2i, i^2 + 3i...
            for j in xrange(i ** 2, n, i):
                nums[j] = False

    return nums

print get_sieve(1)
print get_sieve(2)
print get_sieve(100)