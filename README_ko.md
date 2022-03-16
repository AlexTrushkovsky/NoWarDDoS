[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) |   [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md) | [Portuguese](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_pt.md) |

# <b1>Korean:</b1>
# NoWarDDoS

**경고! 교육 목적으로만 사용하십시오. 자신의 리소스에 대해서만 DDOS 공격을 시도할 수 있습니다.
다른 사이트에서 DDOS 공격을 사용하는 것은 불법이며 법으로 처벌받을 수 있습니다.**
<br />
<br />▪ 파이썬 3.8 이상을 설치 ("경로를 추가" 반드시 체크)
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ 터미널을 열고, 압축 풀기
<br />▪ 루트에서 사용 가능한 명령을 입력합니다.
```
1). run -> 컨테이너를 시작합니다. 예: ./flood.sh run 3 #여기서 '3'은 컨테이너 수입니다.
2). status -> 실행 중인 컨테이너 수의 상태를 표시합니다. 예시: ./flood.sh status
3). log -> 실행 중인 첫 번째 컨테이너의 로그를 표시합니다. 예시: ./flood.sh logs
4). net -> nload eth0을 통한 현재 트래픽을 표시합니다. 예시: ./flood.sh logs net
5). stop -> 컨테이너 실행을 중지합니다. 예시: ./flood.sh stop
```
컨테이너가 시작되고 자동으로 다시 로드되고 업데이트됩니다.

참고: 속도는 현재 대상에 따라 크게 달라지며 사이트가 느리게 작동할수록 속도가 느려집니다.
그들 중 더 많은 거짓말 - 속도도 더 낮을 수 있습니다

<br />**ModuleNotFoundError** 또는 기타 관련 오류가 발생하면 다음을 시도하세요.
```
Windows: python -m pip install --upgrade pip
         pip install -r requirements.txt
         
macOS/Linux: python3 -m pip install --upgrade pip
             pip3 install -r requirements.txt
```

<br />문제가 있으면 도와드리겠습니다 **Telegram:** @esen1n25
## 완성된 이미지 `Docker`:
```shell
docker pull registry.gitlab.com/a_gonda/nowarddos:latest
```

## 클라우드의 새 인스턴스에 배포:
```shell
https://gitlab.com/a_gonda/nowarddos.git && cd nowarddos/ && ./flood.sh run 3 
#자동 업데이트 및 자동 재시작으로 3개의 컨테이너를 시작합니다.
```
