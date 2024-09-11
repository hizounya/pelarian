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
