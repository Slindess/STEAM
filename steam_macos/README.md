# Сравнение цен в STEAM и LIS-SKINS
___
## Mac OS VERSION
___

```
Требуемые библиотеки для установки:
1. selenium -> pip3 install selenium 
```

### Устройство каталога
```
.
| - auto_search.py -> Скрипт для автоматического поиска предметов из файла
| - compare.py -> Скрипт для поиска одного заданного предмета
| - update_lisskins_dollar.py -> Скрипт для обновления курса доллара
| - configs/ |
             | - lisskins_dollar_ruble.txt -> Файл с курсом доллара
             | - to_search.txt -> Файл со списком предметов для автоматического поиска

| - results/ | 
             |- auto_result.txt -> Файл с выходными данными auto_search.py
```
___
### auto_search.py ###
Скрипт принимает на вход данные из файла `./configs/to_search.txt` <br>

Пример входного файла:
```
★ Falchion Knife | Night (Field-Tested)
★ Driver Gloves | Overtake (Field-Tested)
AWP | Wildfire (Battle-Scarred)
```

Во входной файл необходимо записать нужные предметы. Каждый на **ОТДЕЛЬНОЙ** строке. <br>
Названия предметов следует брать с торговой площадки [steam](https://steamcommunity.com/market/).
<br>

1. Перейдите на страницу предмета. Пример:
[AK-47 | Slate (Field-Tested)](https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Slate%20%28Field-Tested%29).
2. В первой строке `Counter-Strike: Global Offensive > AK-47 | Slate (Field-Tested)`
скопируйте название предмета, т.е. `AK-47 | Slate (Field-Tested)`. 
   **ВАЖНО**, чтобы в названии предмета не было пробелов в начале и конце.
   Если в названии предмета есть `★`, ее тоже нужно скопировать.
   
3. Вставьте это название в файл `./configs/to_search.txt`
</br>
---
---
После работы скрипта все данные будут в файле `./result/auto_result.txt` в виде: </br>

```
---------------------------------------------
|  steam   | lisSkins | Разница  |    %     |
---------------------------------------------
|  6834.0  |  5944.8  | 889.171  |  1.1496  |  ★ Falchion Knife | Night (Field-Tested)
---------------------------------------------
|  7188.1  | 6248.58  | 939.490  |  1.1504  |  ★ Driver Gloves | Overtake (Field-Tested)
---------------------------------------------
|  2132.5  | 1884.43  | 248.050  |  1.1316  |  AWP | Wildfire (Battle-Scarred)
---------------------------------------------
```

---
---
### compare.py ###
Скрипт запросит лишь название предмета. Как найти название предмета описано выше.

---
### update_lisskins_dollar.py ###
Скрипт обновляет данные о курсе доллара, используемого сайтом lis-skins.ru
Его не требуется запускать самостоятельно, так как он является служебным скриптом.
Данные о курсе хранятся в `./configs/lisskins_dollar_ruble.txt`

---
_SLINDESS 2022_
