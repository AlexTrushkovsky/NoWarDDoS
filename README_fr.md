[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md)

# <b1>Francais:</b1>

# UA Cyber Shield

<br />🔥Nouveau programme cross-platform prêt à l'action - https://github.com/opengs/uashield 🔥
<br /> ▪ Disponible sur macOS, Linux, et Windows
<br /> ▪ Facile à installer sur toutes les platformes, je guarantee leur sécuritée!
<br /> ▪ les objectifs de DDoS sont coordonnés par les administrateurs du chat principal.
<br /> ▪ Ceux qui veulent aider avec le proxy peuvent écrire sur telegram: @ esen1n25
<br /> ▪ N'oubliez pas de mettre un étoile our le travail des devs :)

# NoWarDDoS

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

<br />▪ Tout passe au travers d'un proxy. Ne soyez pas timide!
<br />▪ Vous pouvez atteindre le support sur Telegram: https://t.me/+wnvf4Dv8AQwxMjVi
<br />▪ L´Application se met à jour automatiquement.
<br />
<br />▪ Si vous avez des erreurs comme ModuleNotFoundError etc. essayez:
<br /> Windows: python -m pip install --upgrade pip
<br /> pip install -r requirements.txt
<br /> macOS/Linux: python3 -m pip install --upgrade pip
<br /> pip3 install -r requirements.txt
<br />
<br />
<br /> macOS ARM (M1) supporting!
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
