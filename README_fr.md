[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |

# <b1>Francais:</b1>
# NoWarDDoS
**Avertissement! Utiliser uniquement à des fins éducatives. Vous ne pouvez tenter une attaque DDOS que sur votre propre ressource.
L'utilisation d'attaques DDOS sur d'autres sites est illégale et punie par la loi.**
<br />
<br />▪ Installe Python 3.8+ (obligatoire sous windows: "Add to path")
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ Ouvre le terminal, unpack l'archive
<br />▪ A la racine, entrez les commandes disponibles:
```
1). run -> Lance des conteneurs. Exemple: ./flood.sh run 3 #Où '3' est le nombre de conteneurs
2). status -> Affiche l'état du nombre de conteneurs en cours d'exécution. Exemple: ./flood.sh status
3). log -> Affiche le journal du premier conteneur en cours d'exécution. Exemple: ./flood.sh logs
4). net -> Affiche le trafic actuel via nload eth0. Exemple: ./flood.sh logs net
5). stop -> Arrête l'exécution des conteneurs. Exemple: ./flood.sh stop
```
Les conteneurs seront lancés et automatiquement rechargés et mis à jour.

Remarque : la vitesse est très dépendante des objectifs actuels, plus les sites fonctionnent lentement, plus la vitesse sera lente.
Plus ils mentent - la vitesse peut aussi être moindre

<br />S'il génère une erreur liée à **ModuleNotFoundError** ou autres, essayez :
```
Windows: python -m pip install --upgrade pip
         pip install -r requirements.txt
         
macOS/Linux: python3 -m pip install --upgrade pip
             pip3 install -r requirements.txt
```

<br />Si vous rencontrez des problèmes, je vous aiderai, veuillez contacter via **Telegram:** @esen1n25
## Image terminée `Docker`:
```shell
docker pull registry.gitlab.com/a_gonda/nowarddos:latest
```

## Déployer sur une nouvelle instance dans le cloud:
```shell
https://gitlab.com/a_gonda/nowarddos.git && cd nowarddos/ && ./flood.sh run 3 
#démarre 3 conteneurs avec mise à jour automatique et redémarrage automatique
```
