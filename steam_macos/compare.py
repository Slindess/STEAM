""" Скрипт возвращает результат сравнения по одному
заданному предмету """
from selenium.webdriver.common.by import By
from selenium import webdriver 
import update_lisskins_dollar
with open("./configs/lisskins_dollar_ruble.txt") as f:
    dollar = float(f.read())

driver = webdriver.Safari()

item_name = input("Введите название предмета: ")

""" steam part """
steam_name = item_name.encode('UTF-8')
url = ""
for b in steam_name:
    url += "%"+hex(b)[2:].upper()

driver.get('https://steamcommunity.com/market/listings/730/'+url)
#time.sleep(20)
result = driver.find_element(By.ID, "market_commodity_buyrequests").text.split('<span class="market_commodity_orders_header_promote">')
result = result[0].split("Начальная цена: $")[1]
steam_price = dollar*float(result)


""" lis skins part """
lis_skins_name = item_name.lower().replace(" | ", "-")
lis_skins_name = lis_skins_name.replace(" (", "-")[:-1]
lis_skins_name = lis_skins_name.replace(" ", "-")
driver.get(f'https://lis-skins.ru/market/csgo/{lis_skins_name}')

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
print("|{:^10.1f}|{:^10}|{:^10.3f}|{:^10.5g}|".format(steam_price, str(lis_skins_price), diff, prc))
print("-"*45)
