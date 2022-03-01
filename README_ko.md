[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) |   [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md)

# <b1>Korean:</b1>

# UA Cyber Shield

<br />🔥 새로운 크로스플랫폼 소프트웨어으로 준비합니다 - https://github.com/opengs/uashield 🔥
<br /> ▪ 맥, 리눅스, 윈도우 운영체제에서 가능합니다
<br /> ▪ 모든 이용 가능한 플랫폼에 설치가 간편하고, 보안은 보장됩니다!
<br /> ▪ 목표는 DDoS와의 가장 중심이 되는 채팅 관리자가 조정합니다
<br /> ▪ 텔레그램에서도 도움을 줄 수 있습니다 @ esen1n25
<br /> ▪ 작성자들의 노고에 깃허브 별을 주는 것도 잊지마세요

# NoWarDDoS

우크라이나가 하이브리드 전쟁에서 승리할 수 있도록 돕는 디도스 러시아 웹사이트
<br />
<br />▪ 파이썬 3.8 이상을 설치 ("경로를 추가" 반드시 체크)
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ 터미널을 열고, 압축 풀기
<br />▪ 루트 디렉토리에서 다음 명령을 실행
<br /> Windows: python attack.py $NUM_THREAD
<br /> macOS/Linux: python3 attack.py $NUM_THREAD
<br />
<br /> 예시: python3 attack.py 500
<br />▪ 옥타코어 CPU 와 16 기가 RAM 구성에서 가장 좋습니다. 프록시가 포함되어 있어 자동으로 동작합니다.
<br />▪ -v 를 넣어서 로그를 볼 수 있습니다
<br />▪ -n 를 넣어서 로그를 지우지 않을 수 있습니다
<br />▪ -p 를 넣어서 프록시를 볼 수 있습니다
<br />▪ 예시: python3 attack.py 500 -v -n
<br />

#

<br />▪ 모든 동작은 프록시를 통합니다. 겁내지 마세요!
<br />▪ 텔레그램에서 지원을 받을 수 있습니다: https://t.me/+wnvf4Dv8AQwxMjVi
<br />▪ 이 프로그램은 자동으로 업데이트하며 가장 최신 사이트 목록을 가져옵니다
<br />
<br />▪ ModuleNotFoundError 등등... 같은 에러를 보면 다음을 시도하세요:
<br /> Windows:
<br /> python -m pip install --upgrade pip
<br /> pip install -r requirements.txt
<br /> macOS/Linux:
<br /> python3 -m pip install --upgrade pip
<br /> pip3 install -r requirements.txt
<br />
<br />
<br /> M1 기반 맥북도 지원합니다!
<br />
<br />**우크라이나를 응원합니다!**

## `Docker` 이미지 빌드 방법:

1. 다운로드 [docker](https://www.docker.com/)
2. 이미지 빌드:

```shell
docker pull gcr.io/fuck-russia-342819/nowarddos:latest
```

3. 실행:

```shell
docker run --rm gcr.io/fuck-russia-342819/nowarddos:latest 500
```

## `Kubernetes` 빌드 방법:

https://github.com/saladar/bellaciao
