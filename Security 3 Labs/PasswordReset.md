# Password reset

## Task 2

Password

```
321nimda
```

## Task 4

lets choose Tom. By bruteforce on certain colors lowercase dictionary we optain:

```
321nimda
```

## Task 5

WTF? Typical g00nwo. Check 2 different questions and press check.

## Task 6

1. Click forgot password
2. Send mail to tom@webgoat-cloud.org
3. Catch the POST request to Forgot password in Burp, send to Repeater
4. Change localhost from WebGoat to WebWolf ( from 8080 to 9090 ) and send.
5. Trun off Burp interception, then go to WebWolf and find request in Requests Tab.
6. Thing that we are interested in is uri key in response.
7. Change begining of uri to http://localhost:8080/WebGoat, part that should be not changed is /PasswordReset/reset/... Open in new tab.
8. Change password
9. Log as Tom having email tom@webgoat-cloud.org and new password.
