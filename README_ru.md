[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) |   [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md)

# UA Cyber Shield - инструкция на русском

* 🔥 Новый кроссплатформенный софт к бою готов - https://github.com/opengs/uashield 🔥
* Доступно на macOS, Linux, Windows
* Цели координируются админами основных чатов с DDoS
* Желающие помочь с proxy пишите в telegram @esen1n25
* Не забудьте авторам поставить звездочки )

# NoWarDDoS

DDoS Russian websites to help Ukraine to win this hybrid war

* Установите Python версии 3.8 или больше (обязательно отметить галочку "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
* Октройте терминал (консоль), переходите в каталог, в которую распаковали нашу програму (с помощью cd)
* В этом каталоге вводим команду:

Windows: `python attack.py количество_потоков`

macOS/Linux: `python3 attack.py количество_потоков`

* К примеру на 8 CPU і 16 ГБ оперативной памяти ставим 500 потоків.
* Прокси устанавливаются автоматически
* Эксперементируйте с количесвом потоков чтобы загрузить свою машину на полную
* С помощью флага `-v` можно увидить [HTTP коды](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP) ответов
* Чтобы не подтирать логи используйте флаг `-n`
* Если вы хотите увидить прокси укажите флаг `-p`
* Пример: `python3 attack.py 500 -v -n`


На бойтесь быть скомпроментированы, потому что все работает через прокси!

В случае возникновения проблем обращайтесь в телеграм чат Telegram: https://t.me/+wnvf4Dv8AQwxMjVi

Программа обновляется автоматически, каждую минуту, снова запуская аттаку

Если показывает ошибку ModuleNotFoundError или другие попробуйте запустить в каталоге программы:
* Windows: `python -m pip install --upgrade pip`
* Linux: `pip3 install -r requirements.txt`
* macOS: `python3 -m pip install --upgrade pip` (macOS ARM (M1) работает)
Если это не помогло объязательно обращайтесь в Telegram!

## Инструкция запуска с помощью Docker:

1. Устанавливаем Docker с [официального сайта](https://docs.docker.com/desktop/)
2. Делайм билд образа

```shell
docker build . -t nowarddos
```

3. Запускаем контейнер

```shell
docker run --rm nowarddos 500
```

## Инструкция запуска для Kubernetes:

https://github.com/saladar/bellaciao

## Армия наших кибер-войск
Python Devs:
* https://t.me/aleeessioo
* https://t.me/dariy_vel
* https://t.me/burya4ok
* https://t.me/korpan_d_24 
* https://t.me/EdwardBrave
* https://t.me/Djmelyarik
* https://t.me/nrslnvchhhhhh98
* https://github.com/CrunchyMutt
* https://github.com/RomanPryima
* https://github.com/AdamDubnytskyy
* https://github.com/sarah-0-connor
* https://github.com/SterbenXIII
* https://github.com/sprilukin
* https://github.com/harentius
* https://t.me/OlehPetryk

GUI: https://t.me/Va1b0rt

Docker: https://t.me/sergey_prilukin

Kubernates: https://github.com/saladar

Backend Dev: https://t.me/ivan_nnnnnnn

Technical support:
* https://t.me/Hazya
* https://t.me/xm1ls
* https://t.me/David_movs
* https://t.me/korpan_d_24
* https://t.me/adjeju
* https://t.me/nichiporchuk_d
* https://t.me/Djmelyarik
* https://t.me/Rob1280
* https://t.me/el_kuban
* https://t.me/dariy_vel
* https://t.me/OlexandrHorbatiuk

Helped with servers:
* https://t.me/geet_gud
* https://t.me/OlexandrHorbatiuk
* https://t.me/Hazya

Helped with a proxy:
* https://t.me/MSNNmusicName
* https://t.me/korpan_d_24
* https://t.me/Va1b0rt

Crosspatform UA Shield: https://github.com/opengs

И еще много воинов за свободу! Не обижайтесь, если кого не забыли. Благодарим всех, без вас бы ничего небыло!
