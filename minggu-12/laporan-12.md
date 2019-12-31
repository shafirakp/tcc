# Instalasi Drupal

1. Membuat folder Minggu-12 pindah ke direktori tersebut, kemudian membuat direktori my_drupal dan pindah ke direktori tersebut.

![](image-12/1.png) .

2. Membuat file docker-compose.yml, kemudian di dalam file tersebut ketikkan perintah seperti di bawah ini. Pada file ini akan membuat 2 container drupal yaitu menggunakan imae drupal:latest dan postgres:10. rupal dapat diakses menggunakan port 8088 dan drupal menggunakan port 5432.

![](image-12/2.png) .

3. Menjalankan file docker-compose.yml dengan perintah docker-compose up -d.

![](image-12/3.png) .

4. Melihat container yang sudah ada dengan perintah docker ps.

![](image-12/4.png) .

5. Mengakses drupal ke URL http://127.0.0.1:8088 , untuk halaman yang muncul adalah halaman memilih bahasa, saya memilih bahasa inggris kemudian klik save and continue.

![](image-12/5.png) .

6. Memilih Profil instalasi, disini saya memilih profil standard.

![](image-12/6.png) .

7. Konfigurasi database, isi field sesuai dengan yang ada pada file docker-compose.yml.

![](image-12/7.png) .

8. Pada step 7 setelah selesai mengisi kemudian klik save and continue. Dan akan memasuki proses instalasi Drupal.

![](image-12/8.png) .

9. Konfigurasi Site, mengisi field .

![](image-12/9.1.png)
![](image-12/9.2.png)

10. Jika proses instalasi selesai maka akan muncul tampilan seperti di bawah ini .

![](image-12/10.png)
