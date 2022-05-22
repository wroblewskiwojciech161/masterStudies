# Task 2

1. Go to devtools in browser
2. Eval script alert(document.cookie);
3. Answer "yes" in text-field and submit
4. Done

# Task 7

1. In upper textfield pass

```
<script>alert()</script>
```

2. Click ok
3. done

# Task 10

1. Find the test route
2. Go to developing tools
3. Exploit js files
4. Find file GoatRouter.js
5. Find testRoute in given file
6. U can see lines below

```
  routes: {
            'welcome': 'welcomeRoute',
            'lesson/:name': 'lessonRoute',
            'lesson/:name/:pageNum': 'lessonPageRoute',
            'test/:param': 'testRoute',
            'reportCard': 'reportCard'
        },
```

7.

Answer

```
start.mvc#test/
```

# task 11

1. We are about to run script

```
<script>webgoat.customjs.phoneHome(); </script>
```

2. Encode this script as url

```
%3c%73%63%72%69%70%74%3e%77%65%62%67%6f%61%74%2e%63%75%73%74%6f%6d%6a%73%2e%70%68%6f%6e%65%48%6f%6d%65%28%29%3b%20%3c%2f%73%63%72%69%70%74%3e
```

3. Page is valnerable in sense of xss. test endpoint can preview everything
4. Concatenate test endpoint with encoded script

```
http://localhost:8080/WebGoat/start.mvc#test/%3c%73%63%72%69%70%74%3e%77%65%62%67%6f%61%74%2e%63%75%73%74%6f%6d%6a%73%2e%70%68%6f%6e%65%48%6f%6d%65%28%29%3b%20%3c%2f%73%63%72%69%70%74%3e
```

5. CHeck console to get number

# task 12

1. Are trusted websites immune to XSS attacks?
   Solution 4: No because the browser trusts the website if it is acknowledged trusted, then the browser does not know that the script is malicious.
2. When do XSS attacks occur?
   Solution 3: The data is included in dynamic content that is sent to a web user without being validated for malicious content.
3. What are Stored XSS attacks?
   Solution 1: The script is permanently stored on the server and the victim gets the malicious script when requesting information from the server.
4. What are Reflected XSS attacks?
   Solution 2: They reflect the injected script off the web server. That occurs when input sent to the web server is part of the request.
5. Is JavaScript the only way to perform XSS attacks?
   Solution 4: No there are many other ways. Like HTML, Flash or any other type of code that the browser executes.
