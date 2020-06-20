"""
Adapted from http://javarng.googlecode.com/svn/trunk/com/modp/random/BlumBlumShub.java
From https://github.com/VSpike/BBS
"""

import random
from decimal import *
import numpy as np


def bitLen(x):
    """
    Get the bit length of a positive number

    :param x: Value to be evaluated
    :return: The length of bits
    """
    assert x > 0
    q = 0
    while x:
        q += 1
        x >>= 1
    return q


def is_prime(n, t=128):
    """
    Check if a number is prime or not
    :param n: Number to be checked if it is prime or not
    :param t: Maximum amount of tries for checking
    :return: True if it is prime. Otherwise False is returned
    """
    # Base cases
    if n == 2 or n == 3:
        return True

    # Non prime numbers' base case and even numbers
    if n <= 1 or n % 2 == 0:
        return False

    # Get r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    # Test the amount of times defined by "t"
    for _ in range(t):
        a = random.randrange(2, n - 1)
        x = pow(a, r, n)

        if x != 1 and x != n - 1:
            j = 1

            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:  # Not prime
                    return False
                j += 1

            if x != n - 1:  # Not prime
                return False
    return True


def get_prime(p_len):
    """
    Creates a random prime number with p_len bits
    :param p_len: The length of the prime numbers in bits
    :return: The random prime number
    """
    getcontext().prec = 10  # Set precision to use Decimal

    # Calculate 2^p_len to avoid recalculating it
    two_to_len = Decimal(2) ** Decimal(p_len)
    two_to_len_minus = Decimal(2) ** Decimal(p_len - 1)

    # Set lower bound
    lower_bound = two_to_len_minus + 1

    # Generate initial random number
    p_num = random.randint(lower_bound, two_to_len)

    # Check until a prime number is found
    while not is_prime(p_num, 128):
        # Calculate a new random number
        p_num = random.randint(int(lower_bound), two_to_len)

    return p_num  # Return obtained prime number


def get_bbs_prime(bits):
    """
    Generate appropriate prime number for use in Blum-Blum-Shub.

    This generates the appropriate primes (p = 3 mod 4) needed to compute the
    "n-value" for Blum-Blum-Shub.

    bits - Number of bits in prime
    """
    while True:
        p = get_prime(bits)
        if p & 3 == 3:
            return p


def generateN(bits):
    """
    This generates the "n value" for use in the Blum-Blum-Shub algorithm.

    :param bits: The number of bits of security
    :return: N = p * q
    """

    p = get_bbs_prime(bits / 2)
    while 1:
        q = get_bbs_prime(bits / 2)
        # make sure p != q (almost always true, but just in case, check)
        if p != q:
            return p * q


class BlumBlumShub(object):

    def __init__(self, bits):
        """
        Constructor, specifying bits for n.

        :param bits: Number of bits
        """
        self.n = generateN(bits)

        length = bitLen(self.n)
        seed = random.getrandbits(length)

        self.state = None  # To avoid warnings
        self.setSeed(seed)  # Set the seed

    def setSeed(self, seed):
        """
        Sets or resets the seed value and internal state.

        :param seed: The new seed
        """

        self.state = seed % self.n

    def next(self, num_bits):
        """
        Returns up to numBit random bits
        :param num_bits:
        :return: The resulting pseudorandom number
        """

        result = 0
        for i in range(num_bits):
            self.state = (self.state ** 2) % self.n
            result = (result << 1) | (self.state & 1)

        return result


def bbs_suf(profile_size, attack_size, traces, pt, attack_num):
    # TODO Comment

    # Get the train traces
    tracesTrain = traces[0:profile_size]

    ptTrain = pt[0:profile_size]

    tracesTest, ptTest = [], []

    traces_len = len(traces)
    bit_length = traces_len.bit_length()

    # Create a BlumBlumShub number with the given bit number
    bbs = BlumBlumShub(bit_length)
    attack_list = []

    for i in range(0, attack_num):
        # To get the number in the space of the Traces length
        rdn = bbs.next(bit_length) % attack_size

        while rdn in attack_list:
            rdn = bbs.next(bit_length) % attack_size

        attack_list.append(rdn)

        tracesTest.append(traces[profile_size + rdn])
        ptTest.append(pt[profile_size + rdn])

    return tracesTrain, ptTrain, tracesTest, ptTest, attack_list
