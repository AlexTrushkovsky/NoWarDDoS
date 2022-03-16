[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) |   [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md)

# NoWarDDoS
**Внимание! Используйте только в обучающих целях. Вы можете попробовать DDOS-атаку только на свой ресурс.
Использование DDOS-атак на другие сайты является незаконным и наказуемым законом.**

* Установите Python версии 3.8 или больше (обязательно отметить галочку "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
* Октройте терминал (консоль), переходите в каталог, в которую распаковали нашу програму (с помощью cd)
* В корне вводим доступные команды:
```
1). run -> Запускает контейнеры. Пример: ./flood.sh run 3 #Где '3' - Количество контейнеров
2). status -> Выводит статус, сколько контейнеров запущено. Пример: ./flood.sh status
3). log -> Выводит лог первого запущенного контейнера. Пример: ./flood.sh logs
4). net -> Показывает текущий трафик через nload eth0. Пример: ./flood.sh logs net
5). stop -> Останавливает запущенные контейнеры. Пример: ./flood.sh stop
```
Контейнеры будут запущены и автоматически перегружаться и обновляться.

Примечание: скорость очень зависит от текущих таргетов, чем медленнее работают сайты, тем скорость будет меньше.
Чем больше их лежит – тем скорость тоже может быть меньше

<br />Если выбивает ошибку связанную с **ModuleNotFoundError** или другие, попробуйте:
```
Windows: python -m pip install --upgrade pip
         pip install -r requirements.txt
         
macOS/Linux: python3 -m pip install --upgrade pip
             pip3 install -r requirements.txt
```

<br />Если возникнут проблемы, я помогу вам, обращайтесь через **Telegram:** @esen1n25

## Готовый образ `Docker`:
```shell
docker pull registry.gitlab.com/a_gonda/nowarddos:latest
```

## Развертка на новом инстансе в облаке:
```shell
https://gitlab.com/a_gonda/nowarddos.git && cd nowarddos/ && ./flood.sh run 3 
#запускает 3 контейнера с автоапдейтом и авторестартом
```
