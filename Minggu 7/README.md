### Menampilkan Data Menggunakan Python Flask dan Mysql 
----

untuk membuat proyek menggunakan Python, jika belum memiliki Python bisa install Python di ............................ 
di tugas ini saya menggunakan Pyton versi 2.7 
---

Disini Framework yang akan saya gunakan adalah Flask. Sebelum penginstallan flask maka kita harus melakukan penginstalan pip
download file get-pip.py disini -----
setelah itu jalankan perintah dibawah untuk mengecek versi pip yang akan digunakan. untuk menjalankan file get-pip.py pastikan sudah masuk ke direktory penyimpanan file nya. Disini saya menyimpannya di desktop.
	pip --version 
gb1....
kemudian jalankan file get-pip.py dengan perintah 
		python get-pip.py

kemudian menambahkan direktori python/pip ke dalam environment variables, caranya seperti ini :
- klik kanan pada This PC kemudian klik properties
  gb2...
- kemudian pilih Advanced system settings dan klik Environment Variables
  gb3
- klik Path di bagian System variables kemudian masukkan direktori python/ 
tempat penyimpanan pip, yaitu di Python27/Script
  gb4..

setelah selesai setting, kemudian membuat direktory baru dengan nama Projek
	mkdir projek

masuk ke directori projek dan install pip dengan perintah 
	cd projek
	pip install virtualenv

kemudian kita untuk membuat projek baru dengan perintah 
	virtualenv venv

sehingga dalam direktory projek yang kita buat tadi akan muncul packages baru bernama venv yang berisi directory-directory untuk membuat project seperti gambar dibawah 
gb7....
kemudian masuk ke directory venv, dan buat folder app 
gb8...
sehingga nanti akan muncul direktori baru di folder venv
lalu di dalam folder app , buat file dengan nama app.py dan flask_version.py
file app.py ini nanti akan berfungsi mengambil data dari tabel customer di database Sale yang akan ditampilkan di browser. Penjelasan scriptnya terdapat di source code nya. 
file app.py..............


dan file flask_version.py
....


kemudian masuk ke directory script yang berada di direktori venv , dan jalankan activate untuk mengaktifkan mode venv supaya file app.py dapat dijalankan, perintah untuk menjalankannya adalah 
	activate

lalu install framework flask dengan perintah 
	pip install flask 

kemudian install flask mysql untuk menghubungkan dengan database yang akan ambil datanya dengan perintah 
	pip install flask-mysql

membuat page templates di dalam directori app. 
template digunakan sebagai view. 


