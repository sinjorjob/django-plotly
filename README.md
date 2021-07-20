# Creating a sales analysis dashboard with django+plotly




## デモデータの生成

```python
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
``` 

製品(Product)テーブルにマニュアルで5～10個ほどサンプルデータを登録した後に以下のコマンドを実行。

```python
python create_demo_data.py
```


`http://127.0.0.1:8000/dashboard/`にアクセスすると以下のようなダッシュボードが表示される。

![demo](https://github.com/sinjorjob/django-plotly/blob/master/images/django-plotly-001.gif)

![demo](https://github.com/sinjorjob/django-plotly/blob/master/images/django-plotly-002.gif)

