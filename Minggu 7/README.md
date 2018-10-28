### Menampilkan Data Menggunakan Python Flask dan Mysql 
----
Untuk membuat proyek menggunakan Python, jika belum memiliki Python bisa install Python di https://www.python.org/downloads/. Di tugas ini saya menggunakan Pyton versi 2.7 

---
Disini Framework yang akan saya gunakan adalah Flask. Sebelum penginstallan flask maka kita harus melakukan penginstalan pip. Download file get-pip.py disini https://pip.pypa.io/en/stable/installing/

---
Setelah itu jalankan perintah dibawah untuk mengecek versi pip yang akan digunakan. untuk menjalankan file get-pip.py pastikan sudah masuk ke direktory penyimpanan file nya. Disini saya menyimpannya di desktop.
        
	pip --version 
gb1....
kemudian jalankan file get-pip.py dengan perintah 
	
	python get-pip.py

---
kemudian menambahkan direktori python/pip ke dalam environment variables, caranya seperti ini :
- klik kanan pada This PC kemudian klik properties
     <img src="https://github.com/lilyastri/tct/blob/master/img/gb2.jpg" alt="gb22"/>
- kemudian pilih Advanced system settings dan klik Environment Variables
     <img src="https://github.com/lilyastri/tct/blob/master/img/gb3.jpg" alt="gb32"/>
- klik Path di bagian System variables kemudian masukkan direktori python/tempat penyimpanan pip, yaitu di Python27/Script
     <img src="https://github.com/lilyastri/tct/blob/master/img/gb4.jpg" alt="gb42"/>

---
Setelah selesai setting, kemudian membuat direktory baru dengan nama Projek
	
	mkdir projek

masuk ke directori projek dan install pip dengan perintah 
        
	cd projek
        pip install virtualenv

kemudian kita untuk membuat projek baru dengan perintah 
	
	virtualenv venv

sehingga dalam direktory projek yang kita buat tadi akan muncul packages baru bernama venv yang berisi directory-directory untuk membuat project seperti gambar dibawah 
   <img src="https://github.com/lilyastri/tct/blob/master/img/gb7.JPG" alt="gb72"/>

---
kemudian masuk ke directory venv, dan buat folder app 
   <img src="https://github.com/lilyastri/tct/blob/master/img/gb8.JPG" alt="gb82"/>
sehingga nanti akan muncul direktori baru di folder venv

---
Lalu di dalam folder app , buat file dengan nama app.py dan flask_version.py. File app.py ini nanti akan berfungsi mengambil data dari tabel customer di database Sale yang akan ditampilkan di browser. Penjelasan scriptnya terdapat di source code nya. 

---
### app.py

	from flask import Flask, render_template, json, request
	from flaskext.mysql import MySQL

	#membuat object mysql
	mysql = MySQL()

	#membuat object flask
	app = Flask(__name__)

	# konfigurasi db
	app.config['MYSQL_DATABASE_USER'] = 'root'
	app.config['MYSQL_DATABASE_PASSWORD'] = ''
	app.config['MYSQL_DATABASE_DB'] = 'sale'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'
	mysql.init_app(app)

	@app.route('/')#routing file pada direktori root
	def main():
    	conn = mysql.connect()
    	cursor = conn.cursor()#koneksi mysql
    	cursor.execute("SELECT * FROM customer")#eksekusi query mysql
    	data = cursor.fetchall()#mengambil data array dari hasil query
    	dataList = []#deklarasi listdata sebagai penampung data
    	if data is not None:#jika data tidak kosong, maka
        for item in data:#dilakukan looping untukk menampilkan data
            dataTempObj = {
                 'id'        : item[0],
                'nama'      : item[1],
                'alamat'     : item[2],
                'no_ktp'  : item[3]
            }#berisi object dan data
            dataList.append(dataTempObj)#memasukkan hasil looping kedalam array datalist
        return json.dumps(dataList)#convert dataList kedalam json 
    else:
        return 'data kosong'#jika data hasil query kosong
    return render_template('index.html')#render halaman pada file index.html

	if __name__ == "__main__":
    app.run()

---
### flask_version.py
---

	import flask
	flask.__version__

---

Kemudian dilanjutkan masuk ke directory script yang berada di folder venv , dan jalankan activate untuk mengaktifkan mode venv supaya file app.py dapat dijalankan, perintah untuk menjalankannya adalah 
	
	activate

lalu install framework flask dengan perintah 
	
	pip install flask 

kemudian install flask mysql untuk menghubungkan dengan database yang akan ambil datanya dengan perintah 
	
	pip install flask-mysql

membuat page templates di dalam directori app. 
template digunakan sebagai view. 


