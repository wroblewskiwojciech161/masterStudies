#!/usr/bin/env python3

import argparse
from Crypto.PublicKey import RSA


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=int)
    parser.add_argument('q', type=int)
    parser.add_argument('e', type=int)
    args = parser.parse_args()

    p = args.p
    q = args.q
    e = args.e

    private_key = RSA.construct(
        (p * q, e, pow(e, -1, (p - 1) * (q - 1)), p, q))

    key_text = private_key.exportKey()
    print(key_text.decode('utf-8'))


if __name__ == "__main__":
    main()
