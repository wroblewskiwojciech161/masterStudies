#!/usr/bin/env python3

import argparse
from Crypto.PublicKey import RSA


def create_private_key(format='utf-8'):
    parser = argparse.ArgumentParser()
    parser.add_argument('P', type=int)
    parser.add_argument('Q', type=int)
    parser.add_argument('E', type=int)
    args = parser.parse_args()
    '''
    p - first modulus factor
    q - second modulus factor
    e - public exponent
    '''
    p = args.P
    q = args.Q
    e = args.E

    '''
    construct RSA object with RSA lib
    retrive private key && decode as utf-8
    '''
    print("dupa \n")
    print(RSA.construct((p * q, e, pow(e, -1, (p - 1) * (q - 1)), p, q)
                        ).publickey().export_key("OpenSSH"))
    return RSA.construct((p * q, e, pow(e, -1, (p - 1) * (q - 1)), p, q)).exportKey().decode(format)


def main():

    private = create_private_key()
    print("Generated key: \n")
    print(private)


if __name__ == "__main__":
    main()
