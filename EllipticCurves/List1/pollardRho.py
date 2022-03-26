from DLGenerator import generate_DL
from dataclasses import dataclass
import random
import sys


@dataclass
class DLP:
    """
    g^k === y mod p
    p = 2 * q + 1 (q \in prime)

    """
    g: int
    y: int
    p: int
    q: int


@dataclass
class CE:
    """
    Collision element

    """

    VAL: int
    a: int
    b: int


def f(ce, dlp):
    if ce.VAL % 3 == 1:
        return CE((ce.VAL * dlp.g) % dlp.p, (ce.a + 1) % dlp.q, ce.b)
    elif ce.VAL % 3 == 2:
        return CE((ce.VAL * ce.VAL) % dlp.p, (2 * ce.a) % dlp.q, (2 * ce.b) % dlp.q)
    return CE((ce.VAL * dlp.y) % dlp.p, ce.a, (ce.b + 1) % dlp.q)


def pollard_rho_discrete_logarithm(dlp, a=0, b=0):
    # turtoiuse
    T = CE(pow(dlp.g, a, dlp.p) * pow(dlp.y, b, dlp.p), a, b)
    # hare
    H = CE(T.VAL, T.a, T.b)

    # main loop of the algorithm
    while True:
        # turtoise move
        T = f(T, dlp)
        # hare move
        H = f(f(H, dlp), dlp)
        if T.VAL % dlp.p - H.VAL % dlp.p == 0:
            break
    nom = (T.a - H.a) % dlp.q
    denom = (H.b - T.b) % dlp.q

    if denom == 0:
        return pollard_rho_discrete_logarithm(dlp, a=random.randint(2, dlp.q), b=random.randint(2, dlp.q))
    return (nom * pow(denom, -1, dlp.q)) % dlp.q


def main(bits=40):
    # Generate DLP instance
    g_tylda, k_actual, y, p, p_tylda = generate_DL(bits)
    # Create object
    dlp = DLP(g_tylda, y, p, p_tylda)
    print(
        f"DLP instance:\nbase (g_tylda): {dlp.g}\nexponent (k): {k_actual}\noutcome (y): {dlp.y}\nmodulus (p): {dlp.p}")
    # Run Pollard Rho algorithm
    k_calculated = pollard_rho_discrete_logarithm(dlp)
    # Check result
    print(
        f"Result: {k_actual} {'=' if k_actual == k_calculated else '!='} {k_calculated} expected")


main(int(sys.argv[1]))
