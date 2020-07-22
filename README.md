topology-charts
===============

graph app with HighCharts



## Update
- 2020/07/19
  - 何作るか、構成考えたりした結果、引き続きpythonの勉強も兼ねてDjango試してみる。
  - 元のプロジェクトは使ってないし全部捨てる。
  - 慣れるためにdockerで。
  - docker officalの手順で色々動かない。
    - https://docs.docker.jp/compose/django.html
  - コマンドとエラー
    - docker-compose run web django-admin.py startproject composeexample .
    - composeexample/wsgi.py already exists, overlaying a project or app into an existing directory won't replace conflicting files
  - 色々自動生成されるファイルがあって、それらが邪魔するようだったから消したり実行したりした。
    - https://qiita.com/breakthrough/items/9929eefd11eefa255530
  - postgresql起動時にエラー
    - Error: Database is uninitialized and superuser password is not specified.
    - メッセージ通りdocker-compose.ymlに環境変数設定追加。
  - ココまで来て英語のほうが最新化できているようだったので参照先を変える。
    - https://docs.docker.com/compose/django/
- 2020/07/20
  - 参考にHeroku化にする
    - https://tksmml.hatenablog.com/entry/2019/04/19/000000
- 2020/07/21
  - オフィシャルのチュートリアルでDjango学習中
    - https://docs.djangoproject.com/ja/3.0/intro/tutorial02/
  - /admin/のログイン後にCSRFチェックのエラー
    - Docker環境で動かしてるからか、そもそものDjangoのテンプレートが悪いのでは？と疑っている。
    - 以下類似
      - https://stackoverflow.com/questions/41343643/django-forbidden-403-csrf-verification-failed-request-aborted-in-docker-p
      - https://qiita.com/kenji0302/items/6976041827e03d3b2b3c
    - adminのデフォルトテンプレートをoverride出来ると思うので、方法を検索中
      - https://stackoverflow.com/questions/49533814/customize-django-admin-template
      - https://torina.top/detail/232/
      - https://qiita.com/Daisuke0209/items/059b0c53283dcf6536e8
- 2020/07/22
  - Heroku上だとadminページでログイン出来た。Dockerコンテナが原因っぽい？一旦無視してチュートリアルを進める。
    - 
  - ステージングとはいえ戻すのが面倒なのでbranchきった。＞feature
- テンプレ
  - あ
    - い

