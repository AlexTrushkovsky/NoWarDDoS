[English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |
# <b1>Português:</b1>
# NoWarDDoS
**Atenção! Use apenas para fins educacionais. Você pode tentar um ataque DDOS apenas em seu recurso. 
Usar ataques DDOS em outros sites é ilegal e punível por lei.**
<br />
<br />▪ Instale o Python 3.8+ (Certifique-se de marcar a caixa "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Abra o terminal (console), vá até a raiz, onde descompactamos nosso programa com o comando cd
<br />▪ Na raiz, digite os comandos disponíveis:
```
1). run ->Lança contêineres. Exemplo: ./flood.sh run 3 #Onde '3' - Número de contêineres
2). status -> Exibe o status de quantos contêineres estão em execução. Exemplo: ./flood.sh status
3). log ->Exibe o log do primeiro contêiner em execução. Exemplo: ./flood.sh logs
4). net -> Mostra o tráfego atual por meio de nload eth0. Exemplo: ./flood.sh logs net
5). stop -> Interrompe a execução de contêineres. Exemplo: ./flood.sh stop
```
Os contêineres serão lançados e recarregados e atualizados automaticamente.

Nota: a velocidade depende muito dos alvos atuais, quanto mais lentos os sites funcionarem, mais lenta será a velocidade.
Quanto mais eles mentem - a velocidade também pode ser menor

<br />Se lançar um erro relacionado a **ModuleNotFoundError** ou outros, tente:
```
Windows: python -m pip install --upgrade pip
         pip install -r requirements.txt
         
macOS/Linux: python3 -m pip install --upgrade pip
             pip3 install -r requirements.txt
```

<br />Se você tiver algum problema, eu te ajudarei, entre em contato via **Telegram:** @esen1n25

## Imagem finalizada `Docker`:
```shell
docker pull registry.gitlab.com/a_gonda/nowarddos:latest
```

## Implantar em uma nova instância na nuvem:
```shell
https://gitlab.com/a_gonda/nowarddos.git && cd nowarddos/ && ./flood.sh run 3 
#starts 3 containers com atualização e reinicialização automáticas
```
