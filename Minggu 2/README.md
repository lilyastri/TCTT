# Software as a Service

**Saas adalah** aplikasi web-based interface, yang dijalankan di sisi pihak ketiga, sehingga dapat diakses melalui jaringan oleh setiap pelanggan. 
Anda tidak perlu melakukan deployment aplikasi dari awal, tidak perlu membayar lisensi software, maupun membeli seperangkat server untuk menjalankan aplikasi yang Anda butuhkan. 
Anda cukup membayar aplikasi sesuai dengan penggunaan per user yang dibayar secara rutin dengan mekanisme OPEX. Karena aplikasi ini berbasis web, maka Anda hanya butuh koneksi 
internet dan sebuah browser untuk menjalankannya.

Kata - kata Software merujuk kepada perangkat lunak suatu system, dimana perangkat lunak pada umumnya memiliki beragam karakteristik. 
Tidak semua perangkat lunak yang beredar di pasaran dapat dikategorikan sebagai SaaS,
Beberapa karakteristik yang harus terpenuhi :
- Berbasis  internet  :  software  harus  dapat  diakses  dan  dikelola  oleh  pengguna  melalui media internet.
- Software  bersifat  terpusat  atau  ter-sentral  sehingga  memungkinkan  pengguna  untuk mengaksesnya darimana dan kapan saja.
- Memiliki  fasilitas  untuk  meng-update  atau  meng-upgrade  secara  terpusat  sehingga pengguna tidak perlu download patch atau upgrade di masing – masing komputer.
- Aplikasi yang ditawarkan oleh provider bersifat multi tenant.

**Keuntungan Penggunaan SaaS**
- Model  rancangan  dan  distribusi  software  lebih  menarik  dan  harga  terjangkau  karena memungkinkan membagi satu aplikasi kepada ratusan perusahaan 
  dan berjalan dalam lingkungan  sistem  biasa.  
- Secara  luas  memberikan  improvisasi  kepada  model  client /server.
- Biaya pemakaian bandwidth untuk menjaga tingkat konektivitas relatif terjangkau.
- Mempermudah pengguna untuk melakukan migrasi aplikasi, dengan menghilangkan sisi pembayaran license software dan keharusan membayar upgrade.
- Meningkatkan produktivitas bagi pengguna.

**Implementasi layanan SaaS**
Implementasi cloud computing dapat diterapkan pada jaringan yang bersifat public atau jaringan yang bersifat private. 
Jaringan yang bersifat public adalah suatu jaringan yang dapat diakses dan digunakan secara umum oleh setiap orang
selama orang tersebut. terkoneksi dengan internet sedangkan jaringan yang bersifat private adalah suatu jaringan yang hanya dapat diakses dan digunakan oleh orang – orang tertentu meskipun melalui koneksi internet.Ketika cloud computing diimplementasikan ke dalam jaringan public, maka seluruh sumber daya atau resources dari aplikasi sepenuhnya berada internet. 

Layanan SaaS yang bersifat public sering kita jumpai dalam bentuk aplikasi web atau web services. Ketika provider meletakkan seluruh sumber daya atau resources dari aplkasi ke dalam internet tetapi hanya beberapa orang yang dapat menggunakannya maka layanan SaaS tersebut bersifat private.SaaS yang ditawarkan provider kepada pengguna baik melalui jaringan public maupun jaringan private pada dasarnya mempunyai satu karakteristik yang sama yaitu mudah diakses dan berskala luas ( upgrade aplikasi, modifikasi aplikasi disesuaikan dengan kebutuhan dan keinginan pengguna ).

Berbagai SaaS yang dibuat oleh provider sering disebut 
dalam berbagai versi yaitu versi berbasis web, on demand dan sebagainya. Apapun versi yang dibuat oleh provider, yang diperlukan oleh pengguna adalah koneksi internet untuk dapat menggunakan SaaS tersebut.Metodologi pengembangan dari SaaS memiliki kesamaan dengan pengembangan software desktop baik dari sisi kemampuan aplikasi diakses dalam skala besar, tingkat keamanan dan aplikasi yang nyaman digunakan oleh pengguna.

**Apa saja yang perlu diperhatikan apabila kamu ingin memasuki ranah SaaS?**
- Buat produk yang disukai pengguna
	Pertama adalah fokus mengembangkan produk yang bagus dan disukai pengguna, karena ini adalah pilar utama dari sebuah SaaS.Brad dari Intuit menekankan 
	bahwa kamu yang ingin terjun di dunia SaaS bisa memulai dengan membuat layanan yang memiliki sebuah fitur utama. Karena apabila kamu mengembangkan 
	sebuah layanan SaaS yang memiliki begitu banyak fitur. Perusahaan-perusahaan besar seperti Intuit sebenarnya sudah melakukan hal yang sama. Jadi, 
	dengan membuat produk yang sangat spesifik, produk buatanmu akan menjadi pilihan dan disukai oleh pengguna.
	
	Contohnya adalah aplikasi kolaborasi berbasis cloud Slack yang sedang naik daun dan banyak digunakan oleh developer-developer di perusahaan teknologi. 
	Sebenarnya ada banyak sekali aplikasi seperti ini, tetapi Slack berhasil menjadi pemimpin karena mengembangkan produk yang disukai pengguna. 
	Caranya adalah dengan iterasi pengembangan produk secara berulang-ulang berdasarkan masukan dari pengguna, sehingga mereka dapat membuat fitur-fitur yang 
	sesuai dengan kebutuhan pengguna.
	
- Layanan konsumen
	Yuen pernah menceritakan bagaimana ia sempat secara tidak sengaja menghapus semua datanya di Google Drive, layanan penyimpanan awal dari Google. 
	Ia kemudian menghubungi layanan konsumen Google. Hanya dalam waktu satu jam, pihak Google mengembalikan semua data-data yang telah terhapus 
	dalam periode 24 jam sebelumnya.Kejadian itulah yang membuat layanan konsumen menjadi hal kedua yang diperlukan oleh startup SaaS. Di samping itu, 
	layanan konsumen juga berperan untuk menerima masukan-masukan dari pengguna.
	
- Tip memonetisasi layanan
	Hal ketiga yang diperlukan startup SaaS adalah menjaring pendapatan. Bagian ini sedikit kontroversi, karena Diede menjelaskan sempat mengenakan tarif yang 
	terlalu tinggi pada masa awal pengembangan Stripe. Bahkan lebih tinggi dari kompetitor-kompetitor mereka yang sudah hadir lebih dahulu. Walau demikian 
	tetap saja ada pengguna yang mau membayar dengan tarif tinggi.

**Karakteristik SaaS**
Cara mudah untuk memahami cara kerja software as a service adalah dengan merumpamakannya sebagai bank. Hal ini karena bank dapat melindungi privasi masing-masing 
pengguna dan juga menyediakan servis yang dapat diandalkan dan aman dalam skala besar. Nasabah bank juga menggunakan sistem finansial dan teknologi tanpa harus 
khawatir orang lain dapat mengakses informasi pribadi tanpa ijin. Bank juga metafor yang tepat untuk memahami SaaS karena karakteristiknya yang sama.
- Multi-Arsitektur
	Multi arsitektur, yaitu dimana semua pengguna dan aplikasi mempunyai satu infrastruktur yang sama dan kode dasar yang dapat dikelola secara terpusat. 
	Karena semua pengguna SaaS berada pada infrastruktur dan kode dasar yang sama, maka vendor pun dapat berinovasi lebih cepat dan menyimpan lebih banyak waktu 
	yang dulunya dihabiskan untuk mengelola versi-veri kode yang kedaluwarsa.
- Kostumisasi Mudah
	Kemampuan tiap pengguna yang dapat menyesuaikan aplikasi untuk kebutuhan bisnis masing-masing tanpa harus merubah insfrastruktur pusat. Perubahan pun dapat 
	dibuat untuk masing-masing perusahaan atau pengguna. Dengan begitu, penyedia SaaS pun dapat membuat perubahan sesering mungkin tanpa merugikan pengguna dan biaya yang mahal.
- Akses Lebih Baik
	Akses data dari berbagai perangkat dapat membuat berbagai hal menjadi lebih mudah. Seperti memantau penggunaan data dan memastikan bahwa semua pengguna melihat 
	data/informasi yang sama dalam satu waktu.
- SaaS Memanfaatkan Konsumen Web
	Semua pasti sudah familiar dengan tampilan Amazon dan Yahoo yang serupa dengan aplikasi SaaS. Dengan model SaaS, anda pun dapat mengkostumisasi dengan mudah tanpa memakan 
	waktu lama.
- Tren SaaS
	Berbagai organisasi telah mengembangkan berbagai platform integrasi SaaS untuk membangun aplikasi SaaS tambahan. Software as a service dapat berkembang melebihi software dengan 
	fungsi tunggal. Sehingga, SaaS pun dapat menjadi sebuah platform dengan berbagai aplikasi yang dapat menyelesaikan tugas-tugas kompleks dan penting.


	








