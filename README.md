# ThreadBBS
## Requirements
* GAE/SE
* Python2.7
* Docker

## Installation
```
docker-compose build && docker-compose up
```

### Setup Dababase

```
docker-compose exec app python bin/db_create.py
docker-compose exec app python bin/db_migrate.py
```

## Usage
open http://localhost:8080

## TODO
* model validation
* ログイン機能
* migration機能
* テンプレートのパーシャル化
* テスト時に1テスト毎にロールバックしたい
* loggingの出力をファイルにも書き込む

### tools
#### maigure
* inspired by rails migration
* can't down, can up
