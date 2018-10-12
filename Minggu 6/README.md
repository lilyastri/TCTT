#### Membuat REST API endpoint Menggunakan NodeJS dam Express
---
Disini saya menggunakan NodeJS sehingga framework yang digunakan adalah"Express". Sebelum membuat REST API sederhana menggunakan Express, pastikan kita sudah menginstall nodeJS dan Express

---
Cara Mendownload nodeJS bisa klik link https://nodejs.org/en/download/
setelah proses instalasi selesai, buka cmd dan masukkan perintah 
    
    node -v
    
perintah diatas digunakan untuk mengecek versi dari nodeJS kita Install tadi. 

---
Selanjutnya buat Direktori Projek, misalnya "Travel". Sesudah membuat directory masuk ke direktory dengan perintah cd Travel. Setelah masuk install Packages yang diperlukan. Disini packages yang diperlukan hanya Express, sehingga saya hanya akan menginstal Express saja gunakan perintah seperti dibawah untuk menginstall Express  
     
     npm install --save express

---
Setelah proses penginstalan selesai, buat file dengan nama index.js kemudian simpan di directory "Travel" yang dibuat tadi. 
	
	const express = require('express');
	const app = express(); 
	app.get('/', (req, res) => { 
	res.jsonp({Nama:'Lily Isnaini Astriningsih'});
	}) 
	app.listen(3000, () => console.log("server berjalan pada http://localhost:3000"))

---
Langkah selanjutnya, jalankan file index.js melalui cmd dengan memasukkan perintah 
	
	node index.js

   <img src="https://github.com/lilyastri/tct/blob/master/img/gam1.jpg" alt="cap22"/>
---
Langkah terakhir, salin url yang terdapat pada layar cmd setelah index.js berhasil dijalankan tadi kemudian jalankan url tersebut melalui browser.
   <img src="https://github.com/lilyastri/tct/blob/master/img/gam2.jpg" alt="cap33"/>
	

