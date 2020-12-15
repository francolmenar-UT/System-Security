import random
from decimal import *

from src.constant.constant import PRIME_LEN, NOISE


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
    # Adjust the bit number when it's not multiple of 2
    if bits % 2 != 0:
        first_bits = int(bits / 2)
        second_bits = first_bits + 1
    else:
        first_bits, second_bits = int(bits / 2), int(bits / 2)

    p = get_bbs_prime(first_bits)
    while 1:
        q = get_bbs_prime(second_bits)
        # make sure p != q (almost always true, but just in case, check)
        if p != q:
            return p * q, p, q


class BlumBlumShub(object):

    def __init__(self, bits):
        """
        Constructor, specifying bits for n.

        :param bits: Number of bits
        """
        self.n, self.p, self.q = generateN(bits)

        self.state = None  # To avoid warnings

        self.setSeed(self.calc_seed())  # Set the seed

    def calc_seed(self):
        """
        Calculates a correct seed for the BBS
        :return:
        """
        length = self.n.bit_length()
        seed = 0

        while seed == 0 or seed == 1 or seed % self.p == 0 or seed % self.q == 0 \
                or seed % self.n == 0 or seed % self.n == 1:
            seed = random.getrandbits(length)

        return seed

    def setSeed(self, seed):
        """
        Sets or resets the seed value and internal state.

        :param seed: The new seed
        """

        self.state = seed % self.n

    def next(self, num_bits):
        """
        Returns up to numBit random bits
        :param num_bits: Maximum amount of bits for the random number generated
        :return: The resulting pseudorandom number
        """

        result = 0
        for i in range(num_bits):
            self.state = pow(self.state, 2, self.n)
            result = (result << 1) | (self.state & 1)

        return result


def bbs_suf(profile_size, attack_size, traces, pt, attack_num, noise):
    """
    Performs the BBS Blum Blum Shub returning the traces to be used for the attack

    :param noise: Boolean describing if there is going to be added noise in the traces
    :param profile_size: Amount of measurements for profiling
    :param attack_size: Amount of measurements for attacking
    :param traces: Traces to attack
    :param pt: Plain text
    :param attack_num: Amount of attack traces to be used
    """
    # Get the train traces
    traces_train = traces[0:profile_size]
    pt_train = pt[0:profile_size]

    # Use all the values, then it is not needed to calculate the random values
    if attack_num == attack_size:
        traces_test = traces[profile_size:profile_size + attack_size]
        pt_test = pt[profile_size:profile_size + attack_size]

        return traces_train, pt_train, traces_test, pt_test

    # Check if the number of attack traces to use is larger than the half of the total attack traces
    # If reverse is True, the random numbers calculated are the only traces not used
    reverse = True if attack_num > int(attack_size / 2) else False

    # Initialize Test Variables - traces and plaintext
    traces_test, pt_test = [], []

    # Length of the last attack trace in bits
    bit_length = int(attack_size.bit_length())

    # Create a BlumBlumShub number with the given bit number
    bbs = BlumBlumShub(PRIME_LEN)
    # List containing the random numbers generated
    rdn_list = []

    # The amount of random numbers created depends on reverse
    rdn_to_gen = attack_size - attack_num if reverse else attack_num

    # For each random number to generate
    rdn_count = 0
    while rdn_count < rdn_to_gen:
        # Generate the new random number
        next_nm = bbs.next(bit_length)
        # To get the number in the space of the Traces length
        rdn = next_nm % attack_size

        # Same number generated
        while rdn in rdn_list:
            rdn = bbs.next(bit_length) % attack_size

        # Save the new number created
        rdn_list.append(rdn)

        rdn_count += 1

    # If reverse is true we take all the elements which are not in the random list
    if reverse:
        rdn_list = list(set(range(0, attack_size)) - set(rdn_list))

    # Add the attack traces with noise
    if noise:
        for num in rdn_list:
            traces_test.append(traces[profile_size + num] + random.randint(NOISE[0], NOISE[1]))
            pt_test.append(pt[profile_size + num])

    # Add the attack traces without noise
    else:
        for num in rdn_list:
            traces_test.append(traces[profile_size + num])
            pt_test.append(pt[profile_size + num])

    return traces_train, pt_train, traces_test, pt_test
