from sympy import isprime, nextprime
import random


def get_random_prime(bottom):
    return nextprime(bottom)


def get_strong_prime(bits):
    # generate p = 2 * p_tylda + 1
    p = None
    p_tylda = None
    btm_num = pow(2, bits - 1) + 1

    while True:
        p_tylda = get_random_prime(btm_num)
        p = 2 * p_tylda + 1
        if isprime(p):
            break
        else:
            btm_num = p_tylda

    return p, p_tylda


def generate_DL(bits):
    """
    Generate instance of Discrete Logarithm Problem
    A tuple (y, g_tylda, x, p)

    1. generate strong prime p = 2 * p_tylda + 1
        1.1 generate p_tylda (39 or 59 bit)
        1.2 check if p is also prime

    2. take random g from F_p {2, ...,p-1}
        do:
            g_tylda = g^2 mod p
        while g_tylda == 1 mod p

        Then g_tylda != 1 mod p and ord(g_tylda) = p_tylda

    3. take random x from {2, ..., p_tylda - 1}
    4. calculate y = g_tylda ^ x mod p
    5. return (y, g_tylda, x, p)

    Then construct problem as:

        y = (g_tylda ^ x`) mod p

    """
    # generate strong prime
    p, p_tylda = get_strong_prime(bits)
    # generate g_tylda
    g_tylda = None
    g = None
    while True:
        g = random.randint(2, p - 1)
        g_tylda = pow(g, 2, p)
        if g_tylda != 1:
            break
    # take random exponent (expected value that should be computed by pollardRho)
    # RANDOMIZE VALUE THAT WILL BE FOUND BY POLLARD RHO
    k = random.randint(2, p_tylda)
    y = pow(g_tylda, k, p)  # g_tylda^k === y mod p

    return g_tylda, k, y, p, p_tylda
