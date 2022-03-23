## Task2

People at Gras realized their mistake and they changed the way RSA key
is generated.
Fortunately for you they did not change the way the sign SignService works, but still ude md5 for signature

## Approach

1. Try to make prefix attack
2. Want to find such s1 and s2, that MD5(m1 || s1) == MD5(m2 || s1)

## Possible ?

1. paper : Chosen-prefixcollisions for MD5 2012
2. Shown that for aproximately 2^39 calls to MD%, it is possible to find s1,s2 for any m1,m2

## We can try hashclash (probably ?), evilize program, md5collgen

Example with hashclash

```
cpc.sh grade.txt  updated_grade.txt
```

## suppouse that we got 2 field on output

out1.txt and out2.txt

## Perform md5

md5(out1.txt) == md5(out2.txt)

## if so, we can try make digital signature

openssl dgst -md5 -sign cakeySec.pem -out grade.sign out1.txt

## And veryfy

openssl dgst -md5 -verify public.pem -signature grade.sign out2.txt
