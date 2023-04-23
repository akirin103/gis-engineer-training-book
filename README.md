# gis-engineer-training-book
書籍「位置情報エンジニア養成講座」の学習用リポジトリです。

<br />

## 備考
`fetch API`を使用して、ローカルのGeoJSONを読み込むサンプルの記載が書籍中に存在した。  
しかし、ブラウザのセキュリティ強度を下げないと`CORS`違反で実行できなかった。  
~~そのため、下記のコマンドで簡易サーバを立てて`CORS`違反を回避した。~~

```
$ python -m http.server
```

<追記>  
`Python`の`http.server`はデフォルトのエンコーディングが`ASCII`らしい。  
そのためマルチバイト文字が文字化けする可能性あり。  
この問題を解決するために`http.server`を拡張した`server.py`を実行して問題を回避。

```
$ python server.py
```

<br />

## 学習メモ
### ベクトルタイル化
ベクトルデータにタイル処理(大きな位置情報データをタイル状に分割)を行い、通信量を大幅に少なくすることが可能。  
tippecanoe(ティッピカノー)コマンドを使用して、以下のようにベクトルタイル化が可能。  

```
# 使用例
$ tippecanoe -e tiles ./geojson/N03-21_210101.geojson -l admin ab -z8 -pC -P

# -e tiles ... ベクトルタイルを出力するディレクトリのパス
# ./geojson/N03-21_210101.geojson ... 変換対象となるGeoJSONファイルのパス
# -l admin ab ... 出力されるベクトルタイルのレイヤー名。複数回使用することで複数のレイヤーを指定可能
# -z8	... ズームレベル8でタイルを生成
# -pC	... 圧縮アルゴリズムとしてgzipを使用。複数回使用することで、複数の圧縮アルゴリズムを指定可能
# -P ... 処理中に進捗状況を表示
```

<br />

## 参考
[Leaflet](https://leafletjs.com/)  
[MapLibre GL JS](https://maplibre.org/maplibre-gl-js-docs/api/)

