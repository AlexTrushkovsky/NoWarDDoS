[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) 

# <b1>English:</b1>
# NoWarDDoS
**Warning! Use only for educational purposes. You can try a DDOS attack only on your own resource.<br/>
Using DDOS attacks on other sites is illegal and punishable by law.**
<br />
<br />▪ Install Python 3.8+ (mandatory enable "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Open terminal, unpack archive
<br />▪ In root directory run next command:
<br /> Windows: python attack.py $NUM_THREAD
<br /> macOS/Linux: python3 attack.py $NUM_THREAD
<br />
<br /> For example: python3 attack.py 500
<br />▪ Best for 8 CPU and 16 RAM configuration is 500 threads . Proxy included and working automaticaly.
<br />▪ You can add the -v flag to see the answer codes
<br />▪ You can add the -n flag so that logs are not clear
<br />▪ You can add the -p flag to see proxy
<br />▪ Example: python3 attack.py 500 -v -n
<br />

#

<br />▪ You can reach support in Telegram: https://t.me/+wnvf4Dv8AQwxMjVi
<br />
<br />▪ If you have errors like ModuleNotFoundError etc. just try:
<br /> Windows: python -m pip install --upgrade pip
<br /> pip install -r requirements.txt
<br /> macOS/Linux: python3 -m pip install --upgrade pip
<br /> pip3 install -r requirements.txt
<br />
## How-to build `Docker` image:

1. Download [docker](https://www.docker.com/)
2. Pull image:

```shell
docker pull gcr.io/fuck-russia-342819/nowarddos:latest
```

3. Run:

```shell
docker run --rm gcr.io/fuck-russia-342819/nowarddos:latest 500
```

## How-to build `Kubernetes`:

https://github.com/saladar/bellaciao
