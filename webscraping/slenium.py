from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep


df = pd.DataFrame(columns=['appid','name','price','tags'])

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://store.steampowered.com/tags/en/RPG/#p=0&tab=TopSellers")

for i in range (0,1501):

    if i == 1:
        cookiesbtn = driver.find_element(by=By.ID,value="rejectAllButton")
        cookiesbtn.click()

    topsellers = driver.find_element(by=By.ID,value="tab_content_TopSellers")
    allgames = topsellers.find_elements(by=By.CLASS_NAME,value="tab_item")

    for element in allgames:
        appid = element.get_attribute("data-ds-appid")
        name = element.find_element(by=By.CLASS_NAME,value="tab_item_name")
        price = element.find_element(by=By.CLASS_NAME,value="discount_final_price")
        tagslist = element.find_elements(by=By.CLASS_NAME,value="top_tag")
        tags = ""
        for i in range(0,len(tagslist)):
            tag = element.find_elements(by=By.CLASS_NAME,value="top_tag")[i]
            tags = tags + tag.text
            i = i + 1



        df.loc[len(df)] = [appid,name.text,price.text,tags]
    
    print(df)
    nextbtn = driver.find_element(by=By.ID,value="TopSellers_btn_next")
    nextbtn.click()
    sleep(10)