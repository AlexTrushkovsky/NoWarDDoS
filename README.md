[English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |

# <b1>Ukrainian:</b1>
**Увага! Використовуйте тільки в навчальних цілях. Ви можете спробувати DDOS-атаку лише на власний ресурс.<br/>
Використання DDOS-атак на інші сайти є незаконним і карається законом.**
<br />
<br />▪ Встановлюємо Python 3.8+ (Обов'язково ставимо галку "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Відкриваємо термінал(консоль), переходимо в корінь, куди розпакували нашу програму командою cd
<br />▪ В корені вводимо наступну команду:
<br /> Windows: python attack.py КІЛЬКІСТЬ*ПОТОКІВ
<br /> macOS/Linux: python3 attack.py КІЛЬКІСТЬ*ПОТОКІВ
<br />
<br />▪ На 8 CPU і 16 гігів оперативки ставим 500 потоків. Проксі встановлюється автоматично.
<br />▪ Експерементуйте, обтирайте оптимальну кількість потоків, щоб проц в сотку довбився ))
<br />▪ Можна додати флаг -v щоб бачити коди відповідей
<br />▪ Можна додати флаг -n щоб логи не підтирало
<br />▪ Можна додати флаг -p щоб показувало проксі
<br />▪ Приклад: python3 attack.py 500 -v -n
<br />

#

<br />▪ Якщо виникнуть проблеми, я допоможу вам, звертайтесь через Telegram: @esen1n25
<br />
<br />▪ Якщо вибиває помилку пов'язану з ModuleNotFoundError aбо інші, спробуйте:
<br /> Windows: python -m pip install --upgrade pip
<br /> pip install -r requirements.txt
<br /> macOS/Linux: python3 -m pip install --upgrade pip
<br /> pip3 install -r requirements.txt
<br />
<br />**Слава Україні!**

## Інструкця для запуску у `Docker`:

1. Ставимо [докер](https://www.docker.com/)
2. Пулаєм імадж (при обновах репи запускати те саме щоб стягнути апдейт)

```shell
docker pull gcr.io/fuck-russia-342819/nowarddos:latest
```

3. Запускаємо

```shell
docker run --rm gcr.io/fuck-russia-342819/nowarddos:latest 500
```

## Інструкця для запуску у `Kubernetes`:

https://github.com/saladar/bellaciao
