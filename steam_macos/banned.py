import requests
from selenium.webdriver.common.by import By
from selenium import webdriver 

item_name = input("Введите название предмета: ")

""" steam part """
steam_name = item_name.encode('UTF-8')
url = ""
for b in steam_name:
    url += "%"+hex(b)[2:].upper()


r = requests.get("https://steamcommunity.com/market/listings/730/"+url)
item_id = r.text.split("Market_LoadOrderSpread( ")[1].split(" ")[0]

r = requests.get(f'https://steamcommunity.com/market/itemordershistogram?\
                 country=RU&language=russian&currency=5&item_nameid={item_id}&two_factor=0')

try:
    steam_price = int(r.json()["lowest_sell_order"]) / 100

except:
    steam_price = 0
    print("ВРЕМЕННЫЙ БАН ОТ СТИМА")

""" lis skins part """
lis_skins_name = item_name.lower().replace(" | ", "-")
lis_skins_name = lis_skins_name.replace(" (", "-")[:-1]
lis_skins_name = lis_skins_name.replace(" ", "-")
driver = webdriver.Safari()
driver.get(f'https://lis-skins.ru/market/csgo/{lis_skins_name}')

response = r.text

try:
    result = driver.find_element(By.CLASS_NAME, "min-price-value").text
    lis_skins_price = float(result.split(".cls")[0].lstrip("\n").lstrip("\t").replace(" ", ""))
    diff = steam_price - lis_skins_price
    prc = steam_price / lis_skins_price
    
except:
    lis_skins_price = None
    diff = 0
    prc = 0

driver.close()


print("-"*45)
print("|{:^10}|{:^10}|{:^10}|{:^10}|".format("steam", "lisSkins", "Разница", "%"))
print("-"*45)
print("|{:^10}|{:^10}|{:^10.5g}|{:^10.5g}|".format(str(steam_price), str(lis_skins_price), diff, prc))
print("-"*45)
