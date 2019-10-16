# Laporan Praktikum Pertemuan Minggu 06

1. Running A Container
- docker search redis berfungsi untuk mencari Image Redis yang ada di docker hub.

![](image-06/1.png)

-docker run -d redis berfungsi untuk menjalankan image redis pada background.

![](image-06/2.png)

2. Finding Running Containers
- docker ps berfungsi untuk melihat container yang sudah berjalan.

![](image-06/3.png)

-docker inspect vibrant_curie berfungsi untuk melihat detail container.

![](image-06/4.png)

- docker logs vibrant_curie berfungsi untuk melihat logs pada sebuah container yang berjalan.

![](image-06/5.png)

3. Accessing redis
- docker run -d --name redisHostPort -p 6379:6379 redis:latest berfungsi untuk menjalankan container redisHostPort pada background.

![](image-06/6.png)

4. Accessing redis
- docker run -d --name redisDynamic -p 6379 redis:latest berfungsi untuk menjalankan container redisDynamic pada background.

![](image-06/7.png)

- docker port redisDynamic 6379 berfungsi untuk melihat list mapping port.

![](image-06/8.png)

- docker ps berfungsi untuk melihat container yang sudah berjalan.

![](image-06/9.png)

5. Persisting Data
- docker run -d --name redisMapped -v /opt/docker/data/redis:/data redis berfungsi untuk menjalankan image yang disertai dengan persistent volume.

![](image-06/10.png)

6. Running A Container In The Foregroun
- docker run ubuntu ps berfungsi untuk menjalankan container ubuntu yang disertai dengan comment ps.

![](image-06/11.png)

- docker run -it ubuntu bash berfungsi untuk masuk ke dalam container ubuntu.

![](image-06/12.png)

![](image-06/13.png)

1. Create Dockerfile

- membuat dockerfile, untuk membangun image dan menyalin konten ke editor.

![](image-06/14.1.png)

2. Build Docker image

- docker build -t webserver-image:v1 berfungsi untuk membuat image statis HTML.

![](image-06/15.png)

- docker image berfungsi untuk melihat list semua image yang ada di host yang digunakan.

![](image-06/16.png)

3. Run
- docker run -d -p 80:80 webserver-image:v1 berfungsi untuk membuat image  dengan memberikan nama dan tag. Menggunakan port 80 karena web server dan menggunakan parameter -p untuk port.

![](image-06/17.png)

- curl docker berfungsi untuk mengakses hasil port 80 melalui curl docker.

![](image-06/18.png)

![](image-06/19.png)

1. Base image
- Membuat image dasar dengan menyalin konten ke editor.

![](image-06/20.2.png)

2. Running Commands
- mengcopy index.html ke editor ke directory /usr/share/nginx/html/index.html.

![](image-06/21.png)

3. Exposing Ports

![](image-06/22.png)

4. Default Commands

![](image-06/23.png)

5. Building Containers
- docker build digunakan untuk membangun container.

 ![](image-06/24.png)

 - docker build -t my-nginx-image:latest berfungsi untuk membuat sebuah image dengan nama my-nginx-image:latest dimana image ini dibuild berdasarkan konfigurasi dari file dockerfile.

 ![](image-06/25.png)

- docker image berfungsi untuk melihat list semua image yang ada di host yang digunakan.

![](image-06/26.png)

6. Launching New image
- docker run -d -p 80:80 my-nginx-image:latest berfungsi untuk menjalankan container my-nginx-image:latest pada background dengan menggunakan port 80.

![](image-06/27.png)

- curl -i http://docker berfungsi untuk mengembalikan file indeks melalui NGINX dan image yang telah dibuat.

![](image-06/28.png)
![](image-06/28.1.png)

-docker  ps berfungsi untuk melihat containers yang sudah berjalan.

![](image-06/29.png)
![](image-06/30.png)
