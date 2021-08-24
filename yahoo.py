
import csv
import sys
import codecs
import math
import random
import requests
from time import sleep
import re
import pandas as pd
import urllib.parse


def main(keyword,count,min_price,max_price,csv):

    s_quote = urllib.parse.quote(keyword)

    url = f'https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch?appid=dj00aiZpPVdLMHFVS1dpTTMzVyZzPWNvbnN1bWVyc2VjcmV0Jng9MDQ-&query={s_quote}&results={count}&price_from={min_price}&price_to={max_price}'

    r = requests.get(url)
    resp = r.json()

    df = pd.DataFrame()

    for item in resp['hits']:
   
        name = item['name']
        price = item['price']
        url = item['url']
        shopname = item['seller']['name']
        caption = item['description']
        review_count = item['review']['count']
        review_average = item['review']['rate']

        # DataFrameに対して辞書形式でデータを追加する
        df = df.append(
            {"商品名": name, 
             "価格": price,
             "URL": url,
             "ショップ名": shopname,
             "キャプション": caption,
             "レビュー数": review_count,
             "レビュー平均": review_average
             }, 
            ignore_index=True)
    
    df.to_csv(csv,encoding="utf_8-sig")


if __name__ == "__main__":
    main()
