# Docker Swarm

1. Membuat VMs dengan nama ff dan ff2 menggunakan docker machine
![](image-13/1.png).

![](image-13/2.png).



2. Membuat ff menjadi swarm manager dengan ssh ke mesin ff kemudian menjalankan perintah docker swarm init --advertise-addr 192.168.99.102.

![](image-13/3.png).

![](image-13/4.png).

3. Docker info berfungsi untuk melihat status pada swarm.

![](image-13/5.1.png).

![](image-13/5.2.png).

4. Perintah docker node ls berfungsi melihat informasi node.

![](image-13/6.png).

5. SSH mesin ff2

![](image-13/7.png).

6. Join ff2 ke swarm ff.

![](image-13/8.png).

7. Connect ke ff, dan jalankan perintah di bawah ini.

![](image-13/9.png).
