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

## 参考
[Leaflet](https://leafletjs.com/)  
[MapLibre GL JS](https://maplibre.org/maplibre-gl-js-docs/api/)  

