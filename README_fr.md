[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |

# <b1>Francais:</b1>
# NoWarDDoS
**Avertissement! Utiliser uniquement à des fins éducatives. Vous ne pouvez tenter une attaque DDOS que sur votre propre ressource.
L'utilisation d'attaques DDOS sur d'autres sites est illégale et punie par la loi.**

DDoS les sites russes pour aider l'Ukraine dans cette guerre hybride
<br />
<br />▪ Installe Python 3.8+ (obligatoire sous windows: "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Ouvre le terminal, unpack l'archive
<br />▪ Dans le dossier root lance cette commande:
<br /> Windows: python attack.py $NUM_THREAD
<br /> macOS/Linux: python3 attack.py $NUM_THREAD
<br />
<br /> Par exemple: python3 attack.py 500
<br />▪ La meilleure config pour 8 CPU et 16 Gb de RAM est 500 threads. Le proxy est inclu et se lance automatiquement.
<br />▪ Vous pouvez ajouter le flag -v pour voir les code de réponses
<br />▪ Vous pouvez ajouter le flag -n flag pour ne pas effacer les prints dans le terminal
<br />▪ Vous pouvez ajouter le flag -p flag pour voir le proxy
<br />▪ Exemple: python3 attack.py 500 -v -n
<br />

#

<br />▪ Vous pouvez atteindre le support sur Telegram: https://t.me/+wnvf4Dv8AQwxMjVi
<br />▪ L´Application se met à jour automatiquement.
<br />
<br />▪ Si vous avez des erreurs comme ModuleNotFoundError etc. essayez:
<br /> Windows: python -m pip install --upgrade pip
<br /> pip install -r requirements.txt
<br /> macOS/Linux: python3 -m pip install --upgrade pip
<br /> pip3 install -r requirements.txt
<br />
<br />**Slava Ukraine!**

## Build l'image `Docker`:

1. Telechargez [docker](https://www.docker.com/)
2. Pull:

```shell
docker pull gcr.io/fuck-russia-342819/nowarddos:latest
```

3. Lancer le programme:

```shell
docker run --rm gcr.io/fuck-russia-342819/nowarddos:latest 500
```

## How-to build `Kubernetes`:

https://github.com/saladar/bellaciao
