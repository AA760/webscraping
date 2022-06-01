from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from time import sleep
import lxml

df = pd.DataFrame(columns=['appid','name','price','tags'])


for i in range (1,1501):
    url = 'https://store.steampowered.com/tags/en/RPG/#p=%d&tab=TopSellers'%i

    req = requests.get(url)
    content = req.text

    soup = BeautifulSoup(content, features="lxml")

    topsellers = soup.find(id="tab_content_TopSellers")
    allgames = topsellers.findAll(class_='tab_item')
   
    for i in range(0,len(allgames)):
        game = topsellers.findAll(class_='tab_item')[i]
        appid = game['data-ds-appid']
        name = game.find(class_='tab_item_name').string
        price = game.find(class_='discount_final_price').string

        def tags():
            tags = ""
            allTags = game.findAll(class_='top_tag')
            for i in range(0,len(allTags)):
                tags = tags + game.findAll(class_='top_tag')[i].string
            return tags

        tags = tags()

        df.loc[len(df)] = [appid,name,price,tags]

    print(df)
    sleep(10)


print(df)