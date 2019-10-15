# Laporan Praktikum Pertemuan Minggu 06

1. Running A Container
- docker search redis berfungsi untuk mencari Image Redis yang ada di docker hub.

![](image-06/1.png)

-docker run -d redis berfungsi untuk menjalankan image redis pada background.

![](image-06/2.png)

2. Finding Running Containers
- docker ps berfungsi untuk melihat containers yang sudah berjalan.

![](image-06/3.png)

-docker inspect vibrant_curie berfungsi untuk melihat detail containers.

![](image-06/4.png)

- docker logs vibrant_curie berfungsi untuk melihat logs pada sebuah containers yang running

![](image-06/5.png)

3. Accessing redis
- docker run -d --name redisHostPort -p 6379:6379 redis:latest berfungsi untuk menjalankan container redisHostPort pada background.

![](image-06/6.png)

4. Accessing redis
- docker run -d --name redisDynamic -p 6379 redis:latest berfungsi untuk menjalankan container redisDynamic pada background.

![](image-06/7.png)

- docker port redisDynamic 6379 berfungsi untuk melihat list mapping port

![](image-06/8.png)

- docker ps berfungsi untuk menjalankan container ubuntu dengan menggunakan comment ps

![](image-06/9.png)

5. Persisting Data
- docker run -d --name redisMapped -v /opt/docker/data/redis:/data redis berfungsi untuk memapping container ke port tersebut

![](image-06/10.png)

6. Running A Container In The Foregroun
- docker run ubuntu ps berfungsi untuk menjalankan container ubuntu yang disertai dengan comment ps

![](image-06/11.png)

7. docker run -it ubuntu bash berfungsi untuk masuk ke dalam container ubuntu

![](image-06/12.png)

![](image-06/13.png)
