# <b1>Ukrainian:</b1> 
# UA Cyber Shield
<br />🔥Новий кроссплатформний софт вже готовий до бою - https://github.com/opengs/uashield🔥
<br />▪ Доступно на macOS, Linux, Windows
<br />▪ Легко встановити на всі доступні платформи, ручаюсь за безпеку!
<br />▪ Цілі координуюся адмінами основних чатів з DDoS
<br />▪ Бажаючі допомогти з проксі, все ще можуть писати в telegram: @esen1n25
<br />▪ Не забувайте ставити зірочки авторам за працю )

# NoWarDDoS
DDoS Russian websites to help Ukraine to win this hybrid war
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
<br />▪ Можна додати флаг -v щоб бачити коди відповідей
<br />▪ Можна додати флаг -n щоб логи не підтирало
<br />▪ Можна додати флаг -p щоб показувало проксі
<br />▪ Приклад: python3 attack.py 500 -v -n
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
## Інструкця для запуску у `Kubernetes`:
https://github.com/saladar/bellaciao

# <b1>English:</b1> 
# UA Cyber Shield
<br />🔥New cross-platform software ready for battle - https://github.com/opengs/uashield🔥
<br /> ▪ Available on macOS, Linux, Windows
<br /> ▪ Easy to install on all available platforms, I guarantee security!
<br /> ▪ Goals are coordinated by the administrators of the main chats with DDoS
<br /> ▪ Those who want to help with the proxy can still write in the telegram: @ esen1n25
<br /> ▪ Don't forget to put stars for authors' work)

# NoWarDDoS
DDoS Russian websites to help Ukraine to win this hybrid war
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
<br />▪ You can add the -v flag to see the answer codes
<br />▪ You can add the -n flag so that logs are not clear
<br />▪ You can add the -p flag to see proxy
<br />▪ Example: python3 attack.py 500 -v -n
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
## How-to build `Kubernetes`:
https://github.com/saladar/bellaciao
