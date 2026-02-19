# Развертывание postgres с помощью докер.
1. создадим контейнер с помощью команды 
```bash
   docker run --name habr-pg-13.3 -p 5432:5432 -e POSTGRES_USER=habrpguser -e POSTGRES_PASSWORD=pgpwd4habr -e POSTGRES_DB=habrdb -d postgres:13.3
   ```
   ![b1ed798ca1238af4e3f2007a7cac2bcd.png](../../../Downloads/herzen_downloads/БД-2024/images/b1ed798ca1238af4e3f2007a7cac2bcd.png)

2. Подключимся к контейнеру через docker desktop и подключимся к нашей бд 

![ce8574092937913690445d204da08675.png](../../../Downloads/herzen_downloads/БД-2024/images/ce8574092937913690445d204da08675.png "ce8574092937913690445d204da08675.png")


![3d69153d93a69803bbfc5368303a0972.png](../../../Downloads/herzen_downloads/БД-2024/images/3d69153d93a69803bbfc5368303a0972.png "3d69153d93a69803bbfc5368303a0972.png")

Как видно базавая бд развернута на компьютере.