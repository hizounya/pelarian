1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Buat repositori lokal mental-health-tracker dan hubungkan ke GitHub menggunakan git init dan git remote add origin.

- Git terpasang, konfigurasi nama pengguna dan email untuk commit, serta aktifkan Git Credential Manager.

- Buat virtual environment, instal dependencies menggunakan pip install.

- Inisialisasi proyek Django dengan django-admin startproject, atur allowed hosts di settings.py.

- Buat aplikasi baru bernama main, daftarkan di INSTALLED_APPS.

- Definisikan model MoodEntry di models.py, lalu migrasi dengan makemigrations dan migrate.

- Buat view di views.py, hubungkan dengan template HTML melalui context di main.html.

- Atur routing URL di urls.py untuk menghubungkan aplikasi dengan halaman utama.

- Tulis unit test di tests.py, jalankan dengan python manage.py test.

- Lakukan deployment aplikasi ke PWS dan pastikan URL deployment berfungsi.

2)  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Pertama mengirimkan request ke URL aplikasi, lalu urls.py mencocokkan URL tersebut dengan fungsi view yang sesuai. views.py memproses logika bisnis dan, jika diperlukan, mengambil data dari models.py, yang mengelola query ke database. Setelah itu, data tersebut dikirimkan ke template HTML untuk di-render. Akhirnya, Django mengirimkan respon dalam bentuk halaman HTML kembali untuk ditampilkan di browser.

3)  Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git dalam pengembangan perangkat lunak berfungsi sebagai sistem kontrol versi yang memudahkan pengembang untuk melacak perubahan kode, berkolaborasi dalam tim, dan menjaga versi yang stabil dari suatu proyek

4)  Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dipilih sebagai framework pembelajaran awal karena memiliki struktur yang jelas dan lengkap, seperti model, view, dan template, serta mendukung pengembangan cepat dengan fitur bawaan yang kuat seperti ORM, sehingga cocok untuk pemahaman dasar pengembangan aplikasi web.

5)  Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut ORM karena berfungsi sebagai alat yang menghubungkan basis data relasional dengan objek dalam kode Python. Dengan ORM, pengembang dapat mengelola database menggunakan kode Python tanpa harus menulis query SQL secara langsung, sehingga mempermudah interaksi dengan database.

Model pada Django disebut ORM karena berfungsi sebagai alat yang menghubungkan basis data relasional dengan objek dalam kode Python. Dengan ORM, pengembang dapat mengelola database menggunakan kode Python tanpa harus menulis query SQL secara langsung, sehingga mempermudah interaksi dengan database.


TUGAS 3

1. Mengapa kita memerlukan data delivery?

Data delivery dibutuhkan untuk memungkinkan server dan klien saling bertukar informasi secara langsung tanpa perlu me-refresh halaman. Hal ini membuat aplikasi lebih efisien dan memberikan pengalaman yang lebih baik bagi pengguna.

2. Mana yang lebih unggul, XML atau JSON? Mengapa JSON lebih sering digunakan?

JSON dinilai lebih unggul karena memiliki format yang lebih ringkas, lebih mudah dibaca oleh manusia, dan lebih cepat diproses dibandingkan XML. Karena kesederhanaannya, JSON menjadi pilihan lebih populer dalam pengembangan aplikasi modern.

3. Apa fungsi dari is_valid() pada form Django?

Fungsi is_valid() digunakan untuk memeriksa apakah data yang diinput ke dalam form sudah sesuai dengan aturan yang berlaku. Fungsi ini penting untuk memastikan data yang masuk aman dan sesuai sebelum diproses lebih lanjut atau disimpan di database.

4. Mengapa kita memerlukan csrf_token pada form di Django?

csrf_token berfungsi untuk melindungi form dari serangan CSRF (Cross-Site Request Forgery), yang bisa terjadi jika ada pihak luar yang mencoba mengirimkan permintaan palsu atas nama pengguna. Tanpa csrf_token, aplikasi dapat menjadi rentan terhadap eksploitasi ini.

5. Bagaimana cara kamu mengimplementasikan checklist di atas secara langkah demi langkah?

-Saya mulai dengan membuat model dan form yang diperlukan.
-Selanjutnya, saya membuat views untuk menangani input form dan memvalidasi datanya.
-Dalam template form, saya menambahkan csrf_token untuk keamanan.
-Setelah itu, saya menyiapkan views yang menampilkan data dalam format XML dan JSON.
-Saya melakukan testing dengan Postman dan memastikan semua berjalan dengan baik sebelum melakukan deployment ke PWS.

