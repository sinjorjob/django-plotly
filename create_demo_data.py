import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

import random
from faker import Factory
from app1.models import Product, OrderItem
from random import randint
from datetime import datetime


fakegen = Factory.create('ja_JP')

def select_product():
    count = Product.objects.count()
    product = Product.objects.all()[randint(0, count - 1)]
    return product


def auto_gen_demo_data(num):

    for _ in range(num):
        # 製品をランダムに選択
        product = select_product()

        # 2018/1/1～202/12/31までの間の日付をランダムに生成
        date = fakegen.date_between_dates(date_start=datetime(2020,1,1), date_end=datetime(2020,7,31))

        # 注文データを生成
        order_item = OrderItem.objects.get_or_create(
                product=product, created_date=date)

# コードの実行
if __name__ == "__main__":
    print('Start create demo data ...')
    auto_gen_demo_data(300)
    print('Demo data generation is complete.')
