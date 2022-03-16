[English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |

# <b1>Ukrainian:</b1>
**Увага! Використовуйте тільки в навчальних цілях. Ви можете спробувати DDOS-атаку лише на власний ресурс.<br/>
Використання DDOS-атак на інші сайти є незаконним і карається законом.**
<br />
<br />▪ Встановлюємо Python 3.8+ (Обов'язково ставимо галку "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Відкриваємо термінал(консоль), переходимо в корінь, куди розпакували нашу програму командою cd
<br />▪ В корені вводимо доступні команди:
```
1). run -> Запускає контейнери. Приклад: ./flood.sh run 3  #Де '3' - Кількість контейнерів
2). status -> Виводить статус, скільки контейнерів запущено. Приклад: ./flood.sh status
3). log -> Виводить лог першого запущеного контейнера. Приклад: ./flood.sh logs
4). net -> Показує поточний трафік через nload eth0. Приклад: ./flood.sh logs net
5). stop -> Зупиняє запущені контейнери. Приклад: ./flood.sh stop
```
Контейнери буде запущено, та вони будуть автоматично перевантажуватися та оновлятися.

Примітка: швидкість дуже залежить від поточних таргетів, чим повільніше сайти працюють, тим швидкість буде меншою. 
Чим більше їх лежить - тим швидкість теж може бути менше

<br />Якщо вибиває помилку пов'язану з **ModuleNotFoundError** aбо інші, спробуйте:
```
Windows: python -m pip install --upgrade pip
         pip install -r requirements.txt
         
macOS/Linux: python3 -m pip install --upgrade pip
             pip3 install -r requirements.txt
```

<br />Якщо виникнуть проблеми, я допоможу вам, звертайтесь через **Telegram:** @esen1n25

## Готовий образ `Docker`:
```shell
docker pull registry.gitlab.com/a_gonda/nowarddos:latest
```

## Розгортка на новому інстансі в хмарі:
```shell
https://gitlab.com/a_gonda/nowarddos.git && cd nowarddos/ && ./flood.sh run 3 
#запускає 3 контейнери з автоапдейтом та авторестартом
```
