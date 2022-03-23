#!/usr/bin/env python3
import base64


def main():
    p = 1385409854850246784644682622624349784560468558795524903
    q = 1524938362073628791222322453937223798227099080053904149
    e = 65537
    phi = (p-1)*(q-1)
    # d = e^{-1} \mod \phi(N)
    d = pow(e, -1, phi)
    print("numeric private exponent -> ", d)


if __name__ == "__main__":
    main()
