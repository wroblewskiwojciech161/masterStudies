# Exercise 1 steps explained

We want to get private key from low-bit(368 bits) rsa encription and then create signatured based on grade.txt file

## Extract modulus and public factor

### Getting modulus from cacertificate.pem

```
openssl x509 -in cacertificate.pem -noout -modulus
```

As a result we get hexadecimal modulus value

```
Modulus=E649D57F6FF9CFF655CB79EE38380C8F8278EB374A90059B0FF06534829D337C753D0E59AFED6FA489F015CF33
```

### Convert modulus to decimal number using online converter

```
2112664634855999140031945945998785346946804826144846396410436155861557104011009549879696604291518474904522547
```

### Factor the modulus using factorization alg into 2 large primes

```
1524938362073628791222322453937223798227099080053904149
```

```
1385409854850246784644682622624349784560468558795524903
```

### Getting public exponent of rsa encription from cacertificate.pem

```
openssl x509 -in cacertificate.pem -noout -text
```

As a result we get

```
Exponent: 65537 (0x10001)
```

### Use script and RSA lib to generate private key

```
-----BEGIN RSA PRIVATE KEY-----
MIHkAgEAAi4A5knVf2/5z/ZVy3nuODgMj4J46zdKkAWbD/BlNIKdM3x1PQ5Zr+1v
pInwFc8zAgMBAAECLT/O74A7F53+5HDX3SDortpIzZZnIJrU93O2hwZom1NeFGiJ
kzyyMi8aQTGHiQIXD+vNKx7XRLvtGKRfICO2s5DWEwOGUxUCFw523+PB/OAFczNk
upoX1C9wkosNKEsnAhcLd9fesqVvXkqn0Gaw+Oi2qaJ6KbTNDQIXAZClKuyLYuXU
ECR++DtJzxQ8FuWGjZMCFwYnXyGcz8NzMENGa/lNLrkQ9D0gutHw
-----END RSA PRIVATE KEY-----
```

## Creating digital signature

```
openssl dgst -md5 -sign key.pem -out new_grade.sign new_grade.txt
```

## Final veryfication

```
openssl dgst -md5 -verify public.pem -signature new_grade.sign new_grade.txt
```

# Solution with RSA CRACK

```
$ docker run -it b4den/rsacrack "$(cat public.pem)"
[*] pubkey.e: 65537
[*] pubkey.n: 2112664634855999140031945945998785346946804826144846396410436155861557104011009549879696604291518474904522547
[*] Key looks like 360 bits
[*] Using cadonfs to compute primes
[*] results are: [u'1524938362073628791222322453937223798227099080053904149', u'1385409854850246784644682622624349784560468558795524903', 65537L]
[*] Key extraction done.
-----BEGIN RSA PRIVATE KEY-----
MIHkAgEAAi4A5knVf2/5z/ZVy3nuODgMj4J46zdKkAWbD/BlNIKdM3x1PQ5Zr+1vpInwFc8zAgMB
AAECLT/O74A7F53+5HDX3SDortpIzZZnIJrU93O2hwZom1NeFGiJkzyyMi8aQTGHiQIXD+vNKx7X
RLvtGKRfICO2s5DWEwOGUxUCFw523+PB/OAFczNkupoX1C9wkosNKEsnAhcHddmtZCl9g5nr5pyK
aq8A0kYmsJ34+gIXC54yOausngJd5VukSE+itVTZENmI7MECFwYnXyGcz8NzMENGa/lNLrkQ9D0g
utHw
-----END RSA PRIVATE KEY-----
```

## Crack ScrrenProof

![](images/rsacrack_proff.png)
