[x] Membuat sebuah proyek Django baru.
[x] Membuat aplikasi dengan nama main pada proyek tersebut.
[x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
[x] Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.

    - name
    - price
    - description

[x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
[x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
[x] Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
[x] Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
        Pertama-tama dengan membuat folder baru sesuai nama yang diperlukan, lalu melakukan virtual environment sesuai framework pc masing-masing dan mengaktifkan virtual environment, lalu membuat direktori yaitu requirements.txt yang berisi tools-tools yang dibutuhkan, kemudian buat proyek dengan nama sekreatif mungkin lalu mengonfigurasi proyek dan menjalankan server dengan manambahkan localhost pada ALLOWED_HOSTS dan juga memastikan bahwa file manage.py ada pada folder setalah itu mengaktifkan server dengan perintah "python manage.py runserver" setelah menjalankan server dapat menonaktifkan dengan perintah "deactivate" pada window. Setelah melakukan semua itu, buat repositori pada github dan lakukan git init pada folder yang pertama kali dibuat setelah git init, tambahkan berkas .gitignore dan isi berkas tersebut sesuai dengan yang diperintahkan, lakukan add, commit, dan push dari repositori lokal ke repositori github, lalu buat akun untuk mendeployment pada web yang sudah disediakan lalu register pada web tersebut setelah daftar dan berhasil login, buat project pada web tersebut dan akan muncul credential, lalu pada settings.py di bagian ALLOWED_HOSTS tambahkan URL deployment pws lalu lakukan add, commit, push, setelah itu ganti branch ke master untuk push ke web deployment dengan perintah git push pws main:master dan lakukan add dan commit. 

        Pada direktori ke cmd dengan perintah  "django-admin startproject konohapedia ." dan juga pastikan struktur direktori lokal sudah sesuai, lalu buat aplikasi bernama main dalam folder utama dengan perintah "python manage.py startapp main", lalu ke folder main dan pilih settings.py dan tambahkan "main" pada INSTALLED_APPS, setelah itu implementasikan template dasar dengan membuat folder baru yaitu bernama templates dan buat berkas pada folder templates bernama "main.html" dan isi dengan kode template yang sudah disediakan, setelah itu buat berkas baru pada aplikasi main bernama models.py dan isi dengan kode yang sudah disediakan, lalu migrasi model dengan perintah "python manage.py startapp main" tujuannya untuk melacak perubahan yang belum diaplikasikan ke dalam basis data lalu lalukan perintah "python manage.py startapp main" tujuannya untuk melakukan perubahan, lalu buka berkas views.py pada main dan tambahkan kode-kode yang diperlukan, lalu modifikasi template dan pergi ke berkas "main.html" dan tambahkan kode yang sudah disediakan setelah itu mengonfigurasi routing URL Aplikasi main, pergi ke berkas urls.py pada folder main dan tambahkan kode yang diperlukan setelah itu konfigurasi routing urls proyek buka file berkas pada konohapedia dan buka berkas urls.py dan tambahkan kode yang diperlukan, setelah itu pergi ke cmd dan lakukan perintah "python manage.py runserver" untuk menjalankan server dan melihat hasil dari proyek yang baru saja dibuat dan yang terakhir buat unit tests tujuannya untuk mengatahui dimana letak salahnya proyek yang sudah dibuat dan juga memeriksa kualitas web.

    Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

        request Client, adalah perintah yang diminta oleh user 
               |
        urls.py, adalah permintaan dari request client dan urls.py akan mencocokan sesuai dengan permintaan yang diberikan
               |
        views.py, adalah setelah url ditemukan pada file views.py akan menjalakan sesuai dengan perintah 
               |
        models.py, adalah struktur data yang dipetakan ke database 
               |
        HTML Page, adalah hasil render yang sudah dibuat pada template html

    Jelaskan fungsi git dalam pengembangan perangkat lunak! 
        Git dalam perangkat lunak dapat menyimpan proyek yang telah dibuat, dengan perintah "git add ." akan menambahkan folder dan file yang ada dalam proyek yang telah dibuat, "git commit "..."" untuk membarikan pesan, dan "git push origin main" untuk nge push dari repositori lokal ke repositori github, adalagi yaitu perintah "git branch" untuk menentukan ke branch mana proyek yang akan dipush.

    Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
        menurut saya karena popularitasnya sudah rame, aman, dan terpercaya, juga kualitas, performance dari django itu sangat baik, dan simpel, django sudah menyediakan tools-tools untuk membuat proyek.

    Mengapa model pada Django disebut sebagai ORM?
        mengapa disebut sebagai ORM karena ORM (Object-Relational Mapping) menggunakan ORM untuk memetakan objek-objek dalam kode Python ke tabel-tabel dalam database ralasional 
    



