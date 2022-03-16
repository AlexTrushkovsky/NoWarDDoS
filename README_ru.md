[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) |   [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |

# NoWarDDoS
**Внимание! Используйте только в обучающих целях. Вы можете попробовать DDOS-атаку только на свой ресурс.
Использование DDOS-атак на другие сайты является незаконным и наказуемым законом.**

* Установите Python версии 3.8 или больше (обязательно отметить галочку "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
* Октройте терминал (консоль), переходите в каталог, в которую распаковали нашу програму (с помощью cd)
* В этом каталоге вводим команду:

Windows: `python attack.py количество_потоков`

macOS/Linux: `python3 attack.py количество_потоков`

* К примеру на 8 CPU і 16 ГБ оперативной памяти ставим 500 потоков.
* Прокси устанавливаются автоматически
* Эксперементируйте с количесвом потоков чтобы загрузить свою машину на полную
* С помощью флага `-v` можно увидить [HTTP коды](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP) ответов
* Чтобы не подтирать логи используйте флаг `-n`
* Если вы хотите увидить прокси укажите флаг `-p`
* Пример: `python3 attack.py 500 -v -n`


В случае возникновения проблем обращайтесь в телеграм чат Telegram: https://t.me/+wnvf4Dv8AQwxMjVi

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
