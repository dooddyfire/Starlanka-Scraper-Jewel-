from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By

start = int(input("Enter your start page : "))
end = int(input("Enter your end page : "))

title_lis = []
cat_lis = []
price_lis = []
desc_lis = []
prod_link = []

driver = webdriver.Chrome(ChromeDriverManager().install())
for i in range(start,end+1):
    url = 'https://www.starlanka.com/gemstones/page/{}/'.format(i)

    
    driver.get(url)


    soup = BeautifulSoup(driver.page_source,'html.parser')

    prod_link_lis = [ c['href'] for c in soup.find_all('a',{'class':'woocommerce-loop-product__link'})]
    print(prod_link_lis)

    for c_link in prod_link_lis:
        prod_link.append(c_link)

    for link in prod_link_lis:

        driver.get(link)
        soupx = BeautifulSoup(driver.page_source,'html.parser')
        
        title = soupx.find('h1',{'class':'product-title'}).text.strip()
        print(title)
        title_lis.append(title)

        cat = soupx.find('nav',{'class':'woocommerce-breadcrumb'}).text.replace('HOME','').strip()
        print(cat)
        cat_lis.append(cat)

        price = soupx.find('span',{'class':'woocommerce-Price-amount'}).text 
        price_lis.append(price)
        print(price)

        desc = soupx.find('div',{'class':'product-short-description'}).text 
        print(desc)
        desc_lis.append(desc)
    

df = pd.DataFrame()

df['Name'] = title_lis 
df['Category'] = cat_lis 
df['Price'] = price_lis 
df['Description'] = desc_lis 
df['Product Link'] = prod_link


# File Output Name
df.to_excel("Jewel.xlsx")