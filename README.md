
# <b1>Ukrainian:</b1> 
# NoWarDDoS
DDoS Russian websites to help Ukraine to win this hybrid war
<br />
**❗️❗️❗️Якщо хтось може допомогти з десктопним застосунком mac/windows, велкам в телеграм❗️❗️❗️**
<br />
<br />▪ Встановлюємо Python 3.8+ (Обов'язково ставимо галку "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Відкриваємо термінал(консоль), переходимо в корінь, куди розпакували нашу програму командою cd
<br />▪ В корені вводимо наступну команду: 
<br />  Windows: python attack.py КІЛЬКІСТЬ_ПОТОКІВ
<br />  macOS/Linux: python3 attack.py КІЛЬКІСТЬ_ПОТОКІВ
<br />  
<br />▪ На 8 CPU і 16 гігів оперативки ставим 500 потоків. Проксі встановлюється автоматично. 
<br />▪ Експерементуйте, обтирайте оптимальну кількість потоків, щоб проц в сотку довбився ))
<br />▪ Приклад: python3 attack.py 500
<br />
#
<br />▪ Все працює через проксі, не бійтесь!
<br />▪ Якщо виникнуть проблеми, 24/7 відповідаємо та координуємо через чат Telegram: https://t.me/+SP0EVc4cr4VjNjAy
<br />▪ Програма оновлюється автоматично, вона сама оновиться та знову запустить атаку, оновленния перевіряються кожну хвилину
<br />▪ Якщо помітили в чаті оновлення яке я не виклав, повідомте в тг
<br />
<br />▪ Якщо вибиває помилку пов'язану з ModuleNotFoundError aбо інші, спробуйте:
<br />    Windows: python -m pip install --upgrade pip
<br />             pip install -r requirements.txt
<br />    macOS/Linux: python3 -m pip install --upgrade pip
<br />                 pip3 install -r requirements.txt
<br />
<br />    ~~macOS з ARM (M1) тимчасово не підтримується, очікуйте оновлення в найближчі години~~
<br />    macOS ARM (M1) все працює!
<br />
<br />▪ Якщо щось зламалося вводимо наступну команду:
<br />  Windows: python updater.py КІЛЬКІСТЬ_ПОТОКІВ
<br />  macOS/Linux: python3 updater.py КІЛЬКІСТЬ_ПОТОКІВ
<br />▪ Якщо не допомагає, обов'язково пишіть в тг!
<br />**Слава Україні!**

## Інструкця для запуску у `Docker`:
1. Ставимо [докер](https://www.docker.com/)
2. Білдимо імадж
```shell
docker build . -t nowarddos
```
3. Запускаємо
```shell
docker run --rm nowarddos 500
```


# <b1>English:</b1> 


# NoWarDDoS
DDoS Russian websites to help Ukraine to win this hybrid war
<br />
**❗️❗️❗️For additional assist please reply in telegram channel❗️❗️❗️**
<br />
<br />▪ Install Python 3.8+ (mandatory enable "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Open terminal, unpack archive
<br />▪ In root directory run next command: 
<br />  Windows: python attack.py $NUM_THREAD
<br />  macOS/Linux: python3 attack.py $NUM_THREAD
<br />  
<br />  For example: python3 attack.py 500
<br />▪ Best for 8 CPU and 16 RAM configuration is 500 threads . Proxy included and working automaticaly. 
<br />
#
<br />▪ All working via proxy. Don't be shy!
<br />▪ You can reach support in Telegram: https://t.me/+SP0EVc4cr4VjNjAy
<br />▪ Application updating automaticaly and will pull all last site list
<br />
<br />▪ If you have errors like ModuleNotFoundError etc. just try:
<br />    Windows: python -m pip install --upgrade pip
<br />             pip install -r requirements.txt
<br />    macOS/Linux: python3 -m pip install --upgrade pip
<br />                 pip3 install -r requirements.txt
<br />
<br />  
<br />    macOS ARM (M1) supporting!
<br />
<br />**Slava Ukraine!**

## How-to build `Docker` image:
1. Download [docker](https://www.docker.com/)
2. Run to build image: 
```shell
docker build . -t nowarddos
```
3. Run:
```shell
docker run --rm nowarddos 500
```
