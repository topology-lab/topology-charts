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

