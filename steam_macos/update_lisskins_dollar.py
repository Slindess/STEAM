""" Скрипт для обновления стоимости доллара в рублях
на сайте lis-skins.ru """
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Safari()
driver.get('https://lis-skins.ru/market/csgo/usp-s-cortex-well-worn/')
result = driver.find_element(By.TAG_NAME, "body").text.split('"rub":{"symbol":"\\u20bd","rate":')[1].split(",")[0]

driver.close()
f = open("configs/lisskins_dollar_ruble.txt", "w")
f.write(result)
f.close()
