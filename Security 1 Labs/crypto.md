# Crypto Basics

## Task 2

echo 'YWRtaW4xMjM6YWRtaW4=' | base64 \thinspace --decode
admin123:admin

## Task 3

decoder: https://strelitzia.net/wasXORdecoder/wasXORdecoder.html

## Task 4

123456,password
decoder: https://md5hashing.net/hash/sha256

## Task 6

### First approach

Modulus:

```
nano test.key (file with privite kay)
openssl rsa -in test.key -pubout > test.pub
openssl rsa -in test.pub -pubin -modulus -noout
```

Signature:

```
echo -n "modulus string" | openssl dgst -sign test.key -sha256 -out sign.sha256
openssl enc -base64 -in sign.sha256 -out sign.sha256.base64
cat sign.sha256.base64
```

### Second approach

Modulus:

```
openssl rsa -in data/00-crypto/id_rsa -modulus -noout
Signature:
openssl dgst -sha256 -sign data/00-crypto/id_rsa data/00-crypto/rsa_modulus.txt | base64 --wrap=0
```

## Task 8

### Find secret ( start given docker image)

docker run -d webgoat/assignments:findthesecret

### get dokcer id

docker ps

### log into container as root , in root/default_secret is secret key

docker exec -u root -t -i [container id] /bin/bash

### go to root

cd ~/root

### decrypt message

echo "U2FsdGVkX199jgh5oANElFdtCxIEvdEvciLi+v+5loE+VCuy6Ii0b+5byb5DXp32RPmT02Ek1pf55ctQN+DHbwCPiVRfFQamDmbHBUpD7as=" | openssl enc -aes-256-cbc -d -a -kfile

### Final message

Leaving passwords in docker images is not so secure
