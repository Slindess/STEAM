""" Скрипт записывает результаты поиска по данным из файла
 ./configs/to_search.txt в файл results/auto_result.txt """

from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import update_lisskins_dollar

def compare(item_name, dollar, driver):
    """ steam part """
    steam_name = item_name.encode('UTF-8')
    url = ""
    for b in steam_name:
        url += "%" + hex(b)[2:].upper()

    driver.get('https://steamcommunity.com/market/listings/730/' + url)
    result = driver.find_element(By.ID, "market_commodity_buyrequests").text.split(
        '<span class="market_commodity_orders_header_promote">')
    result = result[0].split("Начальная цена: $")[1]
    steam_price = dollar * float(result)

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

    output = "|{:^10.1f}|{:^10}|{:^10.3f}|{:^10.5g}|".format(steam_price, str(lis_skins_price), diff, prc) + "  " + item_name + "\n"
    output += "-" * 45 + "\n"

    return output


def main():
    # Получение курса доллара lis-skins.ru
    with open("./configs/lisskins_dollar_ruble.txt") as f:
        dollar = float(f.read())

    f_in = open("configs/to_search.txt", "r")
    f_out = open("results/auto_result.txt", "w")
    header = "-" * 45 + "\n"
    header += "|{:^10}|{:^10}|{:^10}|{:^10}|".format("steam", "lisSkins", "Разница", "%") + "\n"
    header += "-" * 45 + "\n"
    f_out.write(header)
    f_out.close()

    item_name = f_in.readline()
    while item_name:
        driver = webdriver.Safari()
        f_out = open("results/auto_result.txt", "a")
        output = compare(item_name.rstrip("\n"), dollar, driver)
        f_out.write(output)
        f_out.close()
        item_name = f_in.readline()
        driver.close()
        time.sleep(30)

    f_in.close()

if __name__ == "__main__":
    main()

