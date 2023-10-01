# WebAppp
Webアプリの練習帳です。

## ぴぇぴぇ〜
入力に対して「ぴぇぴぇ」と返します。「ぴぇぴぇ」と入力した時だけ、「キュェー」と鳴きます。

## 動かし方
1. ターミナルでアプリケーションを実行しておきます。
```
$ python application.py
```
2. ブラウザで `http://localhost:5000` を開きます。
3. 入力ボックスが現れるので、何かを入力して [送信] を押します。

## メモ
- Python と Flask を使います。 `requirements.txt`
- `.ebextensions` と `.elasticbeanstalk` は、AWSで動かすための設定ファイルです。`.elasticbeanstalk` は空（非公開）です。
- Webページのデザインは `templates/index.html` で決めます。
- 応答は `response.py` で決めます。
