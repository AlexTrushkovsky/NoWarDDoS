[Ukrainian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README.md) | [Russian](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ru.md) | [Korean](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_ko.md) | [French](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_fr.md) | [English](https://github.com/AlexTrushkovsky/NoWarDDoS/blob/main/README_en.md)

# <b1>Japanese:</b1>

# UA Cyber Shield

<br />🔥戦いに備えた新しいクロスプラットフォーム ソフトウェア- https://github.com/opengs/uashield 🔥
<br /> ▪ macOS, Linux, Windows上で動作
<br /> ▪ 全てのプラットフォームで簡単にインストール、セキュリティを保証
<br /> ▪ ターゲットはDDoSのメインチャットで管理者と調整
<br /> ▪ プロキシに関しての連絡はこちら: @ esen1n25
<br /> ▪ 作者へのstarをお願いします :)

# NoWarDDoS

ロシアのウェブサイトへDDoS - ウクライナがこのハイブリッドな戦争に勝つために
<br />
<br />▪ Python 3.8以上をインストール  ("Add to path" が必須です)
![alt text](https://miro.medium.com/max/1344/0*7nOyowsPsGI19pZT.png)
<br />▪ ターミナルを起動しアーカイブを展開
<br />▪ ディレクトリに移動しコマンドを実行:
<br /> Windows: python attack.py $NUM_THREAD
<br /> macOS/Linux: python3 attack.py $NUM_THREAD
<br />
<br /> 実行例: python3 attack.py 500
<br />▪ 8コアのCPU、16GBのメモリの場合、スレッド数は500が最適です。プロキシは自動で有効化されます。
<br />▪ `-v`: 返答を有効化する
<br />▪ `-n`: ログをクリアしない
<br />▪ `-p`: 現在のプロキシを表示
<br />▪ 実行例: python3 attack.py 500 -v -n
<br />

#

<br />▪ 全ての動作はプロキシを介して行われます。
<br />▪ Telegramでサポートを受けることができます。: https://t.me/+wnvf4Dv8AQwxMjVi
<br />▪ ソフトウェアは自動で更新され、常に最新のサーバリストを取得します
<br />
<br />▪ `ModuleNotFoundError` などのエラーに遭遇した場合、以下を試してください: 
<br /> Windows: python -m pip install --upgrade pip
<br /> pip install -r requirements.txt
<br /> macOS/Linux: python3 -m pip install --upgrade pip
<br /> pip3 install -r requirements.txt
<br />
<br />
<br /> macOS ARM (M1) 上でも動作します
<br />
<br />**Slava Ukraine!**

## `Docker` imageをビルド:

1. [docker](https://www.docker.com/) をダウンロード
2. Docker imageを取得:

```shell
docker pull gcr.io/fuck-russia-342819/nowarddos:latest
```

3. 実行:

```shell
docker run --rm gcr.io/fuck-russia-342819/nowarddos:latest 500
```

##  `Kubernetes` をビルド:

https://github.com/saladar/bellaciao
