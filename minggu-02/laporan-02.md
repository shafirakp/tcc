# Laporan Praktikum Pertemuan Minggu 02
1. Pindah ke folder tcc, melihat file yang ada di folder tcc, membuat file minggu-02, pindah ke minggu-02, pada saat saya mengerjakan programnya tetap saya masukkan di file minggu-01, di minggu-02 hanya berisi image dan laporan minggu-02.

![](image-02/1.png)

# Membatalkan perubahan
2. git checkout -b edit-readme-2 : perintah ini berfungsi untuk menukar branch yang aktif dengan branch yang di pilih dan sekaligus membuat branch baru, dan branch yang di pilih adalah edit-readme-2.

![](image-02/2.png)

3. VIM README.md : perintah ini berfungsi untuk mengedit/mengisi file README ketika di enter kemudian tekan i yang berfungsi untuk mengetikkan isi di file tersebut # My Awesome Project Ini isi proyek. Jadi agak kacau nih, setelah di isi kemudian tekan esc :wq yang berfungsi untuk menyimpan.

![](image-02/3.png)

4. git checkout master : perintah ini berfungsi untuk pindah ke branch master.

![](image-02/4.png)

5. cat README.md : berfungsi untuk melihat isi yang ada di file README.md.

![](image-02/5.png)

6. git branch -D edit-readme-2 : perintah ini berfungsi untuk menghapus branch edit-readme-2.

![](image-02/6.png)

7. git branch : perintah ini berfungsi untuk melihat branch dan terdapat branch master.

![](image-02/7.png)

8. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md.

![](image-02/8.png)

9. git reset --hard : perintah ini berfungsi untuk melakukan format secara paksa kemudian melihat hasilnya dengan membuka isi dari file README.md.

![](image-02/14.png)

# Undo Commit Terakhir
10. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md.

![](image-02/14.png)

11. git log --oneline : perintah ini berfungsi untuk melihat riwayat repositori.

![](image-02/15.png)

12. VIM README.md : perintah ini berfungsi untuk mengedit/mengisi file README.md.

![](image-02/16.png)

13. git add -A :  perintah ini berfungsi menambahkan file yang ada.

![](image-02/16.png)

14. git commit -m "Add: contents" : perintah ini berfungsi untuk menyimpan perubahan dan -m untuk menambahkan keterangan.

![](image-02/17.png)

15. git push origin master : berfungsi untuk meng push file ke repository GitHub pada branch master.

![](image-02/18.png)

16. VIM README.md : perintah ini berfungsi untuk mengedit/mengisi file README.md.

![](image-02/19.png)

17. git add -A : perintah ini berfungsi menambahkan file yang ada.

![](image-02/19.png)

18. git commit -m "Add: contents - 2" : perintah ini berfungsi untuk menyimpan perubahan dan -m untuk menambahkan keterangan.

![](image-02/19.png)

19.  git push origin master : berfungsi untuk meng push file ke repository GitHub pada branch master.

![](image-02/20.png)

20. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md.

![](image-02/21.png)

21. git status : perintah ini berfungsi untuk mengetahui status dari repository lokal.

![](image-02/22.png)

22. git revert HEAD : perintah ini berfungsi untuk membuka editor. Pada editor tersebut kita bisa mengetikkan pesan revert ( = pesan commit untuk pembatalan).

![](image-02/23.png)

23. git status : perintah ini berfungsi untuk mengetahui status dari repository lokal.

![](image-02/24.png)

24. git push origin master : berfungsi untuk meng push file ke repository GitHub pada branch master.

![](image-02/25.png)


25. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md. Pada praktik ini sebelumnya README.md saya isi #My Awesome Project Ini Isi proyek Fira.

![](image-02/26.png)

26. vim README.md : perintah ini berfungsi untuk mengedit/mengisi file README.md. Dan edit isi README.md

![](image-02/26.png)

27. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md.

![](image-02/26.png)

28. git add -A : perintah ini berfungsi menambahkan file yang ada.

![](image-02/27.png)

29. git commit -m "Add: isi tambahan 1" : perintah ini berfungsi untuk menyimpan perubahan dan -m untuk menambahkan keterangan.

![](image-02/27.png)

30. git status : perintah ini berfungsi untuk mengetahui status dari repository lokal.

![](image-02/28.png)

31. git log --oneline : perintah ini berfungsi untuk melihat riwayat repositori.

![](image-02/29.png)

31. git reset --hard HEAD^ : perintah ini berfungsi untukmelakukan format secara paksa kemudian melihat hasilnya dengan membuka isi dari file README.md.

![](image-02/30.png)

32. git status : perintah ini berfungsi untuk mengetahui status dari repository lokal.

![](image-02/30.png)

33. cat README.md :  perintah ini berfungsi untuk melihat isi yang ada di file README.md. Setelah di reset maka isi akan berubah ke awal.

![](image-02/30.png)

34. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md. Setelah di reset maka isi akan berubah ke awal.

![](image-02/31.png)

35. git log --oneline : perintah ini berfungsi untuk melihat riwayat repositori.

![](image-02/32.png)

36. git revert a7615fb : perintah ini berfungsi untuk kembali ke perubahan pada saat yang sudah lama output yang dihasilkan fatal karena a7615fb harusnya disamakan pada saat proses git log file mana yang akan dikembalikan

![](image-02/33.png)

37. cat README.md : perintah ini berfungsi untuk melihat isi yang ada di file README.md. vim README.md : berfungsi untuk mengisi dan kemudian di cat lagi untuk melihat isi

![](image-02/34.png)

38. git revert --continue : perintah ini berfungsi untuk melanjutkan kembali ke perubahan pada saat yang sudah lama.

![](image-02/37.png)

39. git push origin master : berfungsi untuk meng push file ke repository GitHub pada branch master.

![](image-02/39.png)
