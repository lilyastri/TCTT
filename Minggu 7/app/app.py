
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
