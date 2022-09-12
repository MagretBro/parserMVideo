import requests
import json

def get_data():
    """Получаем куки методом copy curl в listing и преобразуем на https://curlconverter.com/python/ """
    cookies = {
        '__hash_': 'c1b855edb68345cc136ff448ca1b878a',
        '__lhash_': '5cce4f9483af28bbe31fff1db0b3619c',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '21429614582',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '2',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'flacktory': 'no',
        'searchType2': '1',
        '_gid': 'GA1.2.533121166.1662888993',
        '_sp_ses.d61c': '*',
        '_ym_uid': '1662888994403804847',
        '_ym_d': '1662888994',
        '_ym_isad': '2',
        'SMSError': '',
        'authError': '',
        'tmr_lvid': '4c83f00b8b04678610d5f31350608967',
        'tmr_lvidTS': '1662888998881',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'a48f4e2d-70f1-4b6d-bda5-353e148088f9',
        'advcake_track_id': '88161039-8fcf-6de0-bc6e-e3f7b63afee8',
        'advcake_session_id': 'a6b565aa-bd71-58b2-8533-fbc9d3bfb6f9',
        'st_uid': '3dae6b21bf253848a363d1b8e02b6425',
        'uxs_uid': '3d16a810-31b5-11ed-937d-95945957e595',
        'flocktory-uuid': 'fba97d48-793f-40ba-97a9-cba10757a842-8',
        'afUserId': '3e313b78-30fa-4b01-ae53-1733da65cddf-p',
        'AF_SYNC': '1662889000918',
        'BIGipServeratg-ps-prod_tcp80': '1912921098.20480.0000',
        'bIPs': '155255760',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'cSYMjdnPB6bJ2zQyr9Bxy2114X7qrhH20L5yjwKQZRTvtS3msF3s!-267150821',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '1912921098.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VcXhY6IXsfP1VbfxsnYzJINSxhT1RdPkJxIzB8L1V3SVk7SCYPSEA6OyEXaRsqDiAIV3A+GjhnI2ZIXh9LV05qJh8XeXMrWAwMZEZJb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStDbSZkSWIjSFVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=wj+NUw==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VcXhY6IXsfP1VbfxsnYzJINSxhT1RdPkJxIzB8L1V3SVk7SCYPSEA6OyEXaRsqDiAIV3A+GjhnI2ZIXh9LV05qJh8XeXMrWAwMZEZJb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStDbSZkSWIjSFVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=wj+NUw==',
        'cfidsgib-w-mvideo': 'WjOu9ZrUZ6r020KLRx2QjsQcbhnDOZtdmlAPUB+XAD9AwthKHqP2HEbL85jXoZBe2TE0LCn7MHk+cR9VjfOlbe/KEa2ZiL0bv2zQZK5JGH70at5AtHPF0Iiiu/iOIj44Prkw9BfehzZuCSf2v37LmciMO7E0RZLa0Yv9',
        'cfidsgib-w-mvideo': 'WjOu9ZrUZ6r020KLRx2QjsQcbhnDOZtdmlAPUB+XAD9AwthKHqP2HEbL85jXoZBe2TE0LCn7MHk+cR9VjfOlbe/KEa2ZiL0bv2zQZK5JGH70at5AtHPF0Iiiu/iOIj44Prkw9BfehzZuCSf2v37LmciMO7E0RZLa0Yv9',
        'gsscgib-w-mvideo': 'ZxX6Ts++wwFuNlqsRU+xj+DsBjtHMDXq5N9eSHXWXqgtgFibyMTi5yQqrA1Llb3OnTsOZSl26fJYEapdT8BpHQg4jrxMv9TtOoLnuxCxaPnxaBIiycPl66IY6hEH7TpCmR9qaqAiIACiZX10tHT8vNv1hyNxMv6jf6wWM5BRbD1mAsQ+grvlxoLVVKBmeIbQLPiQqqyUWmqGNPVAlIepIKo62dV2IIYSCxrcXP+GW7mnqH9pPvqGHNfCQmyT8A==',
        'gsscgib-w-mvideo': 'ZxX6Ts++wwFuNlqsRU+xj+DsBjtHMDXq5N9eSHXWXqgtgFibyMTi5yQqrA1Llb3OnTsOZSl26fJYEapdT8BpHQg4jrxMv9TtOoLnuxCxaPnxaBIiycPl66IY6hEH7TpCmR9qaqAiIACiZX10tHT8vNv1hyNxMv6jf6wWM5BRbD1mAsQ+grvlxoLVVKBmeIbQLPiQqqyUWmqGNPVAlIepIKo62dV2IIYSCxrcXP+GW7mnqH9pPvqGHNfCQmyT8A==',
        'fgsscgib-w-mvideo': 'TCvJ27da7b6f07d1a2b9e38ef7d376603e32d758',
        'fgsscgib-w-mvideo': 'TCvJ27da7b6f07d1a2b9e38ef7d376603e32d758',
        'cfidsgib-w-mvideo': 'pntBHuBBrZgtSmliyeoFHChA4v5AkrDVEz9UgBhC2ciznEDwynjqD9eqqZ2ganDwGSaXju+WHRNm72+3D0Yka3OXpjXSU6x50eq71TZdiZLdMXc3fF+vV2jD93apHc25wG1RaLuHL/J1VXnRxKnonLNbebqqpb8VAxGL',
        'CACHE_INDICATOR': 'false',
        '_sp_id.d61c': 'a43b1426-3afb-4745-a67e-ab308db7b1e4.1662888994.1.1662889536..3c1e97e6-8cd5-472c-89d6-c478b4f7fb3a..06724bec-d372-4bbb-81a8-9338b1a96f5a.1662888993600.8',
        '_ga': 'GA1.2.831528810.1662888993',
        'MVID_ENVCLOUD': 'prod2',
        'tmr_detect': '0%7C1662889545973',
        'tmr_reqNum': '97',
        '_ga_CFMZTSS5FM': 'GS1.1.1662888993.1.1.1662889567.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1662888993.1.1.1662889567.13.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,cy;q=0.6',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=510c3d9794ee406ebfe492b4756ba730,sentry-sample_rate=0%2C5',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__hash_=c1b855edb68345cc136ff448ca1b878a; __lhash_=5cce4f9483af28bbe31fff1db0b3619c; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=21429614582; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=2; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_SMART_BANNER_BOTTOM=true; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; flacktory=no; searchType2=1; _gid=GA1.2.533121166.1662888993; _sp_ses.d61c=*; _ym_uid=1662888994403804847; _ym_d=1662888994; _ym_isad=2; SMSError=; authError=; tmr_lvid=4c83f00b8b04678610d5f31350608967; tmr_lvidTS=1662888998881; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=a48f4e2d-70f1-4b6d-bda5-353e148088f9; advcake_track_id=88161039-8fcf-6de0-bc6e-e3f7b63afee8; advcake_session_id=a6b565aa-bd71-58b2-8533-fbc9d3bfb6f9; st_uid=3dae6b21bf253848a363d1b8e02b6425; uxs_uid=3d16a810-31b5-11ed-937d-95945957e595; flocktory-uuid=fba97d48-793f-40ba-97a9-cba10757a842-8; afUserId=3e313b78-30fa-4b01-ae53-1733da65cddf-p; AF_SYNC=1662889000918; BIGipServeratg-ps-prod_tcp80=1912921098.20480.0000; bIPs=155255760; wurfl_device_id=generic_web_browser; JSESSIONID=cSYMjdnPB6bJ2zQyr9Bxy2114X7qrhH20L5yjwKQZRTvtS3msF3s!-267150821; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1912921098.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VcXhY6IXsfP1VbfxsnYzJINSxhT1RdPkJxIzB8L1V3SVk7SCYPSEA6OyEXaRsqDiAIV3A+GjhnI2ZIXh9LV05qJh8XeXMrWAwMZEZJb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStDbSZkSWIjSFVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=wj+NUw==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VcXhY6IXsfP1VbfxsnYzJINSxhT1RdPkJxIzB8L1V3SVk7SCYPSEA6OyEXaRsqDiAIV3A+GjhnI2ZIXh9LV05qJh8XeXMrWAwMZEZJb2UlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeStDbSZkSWIjSFVJa2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=wj+NUw==; cfidsgib-w-mvideo=WjOu9ZrUZ6r020KLRx2QjsQcbhnDOZtdmlAPUB+XAD9AwthKHqP2HEbL85jXoZBe2TE0LCn7MHk+cR9VjfOlbe/KEa2ZiL0bv2zQZK5JGH70at5AtHPF0Iiiu/iOIj44Prkw9BfehzZuCSf2v37LmciMO7E0RZLa0Yv9; cfidsgib-w-mvideo=WjOu9ZrUZ6r020KLRx2QjsQcbhnDOZtdmlAPUB+XAD9AwthKHqP2HEbL85jXoZBe2TE0LCn7MHk+cR9VjfOlbe/KEa2ZiL0bv2zQZK5JGH70at5AtHPF0Iiiu/iOIj44Prkw9BfehzZuCSf2v37LmciMO7E0RZLa0Yv9; gsscgib-w-mvideo=ZxX6Ts++wwFuNlqsRU+xj+DsBjtHMDXq5N9eSHXWXqgtgFibyMTi5yQqrA1Llb3OnTsOZSl26fJYEapdT8BpHQg4jrxMv9TtOoLnuxCxaPnxaBIiycPl66IY6hEH7TpCmR9qaqAiIACiZX10tHT8vNv1hyNxMv6jf6wWM5BRbD1mAsQ+grvlxoLVVKBmeIbQLPiQqqyUWmqGNPVAlIepIKo62dV2IIYSCxrcXP+GW7mnqH9pPvqGHNfCQmyT8A==; gsscgib-w-mvideo=ZxX6Ts++wwFuNlqsRU+xj+DsBjtHMDXq5N9eSHXWXqgtgFibyMTi5yQqrA1Llb3OnTsOZSl26fJYEapdT8BpHQg4jrxMv9TtOoLnuxCxaPnxaBIiycPl66IY6hEH7TpCmR9qaqAiIACiZX10tHT8vNv1hyNxMv6jf6wWM5BRbD1mAsQ+grvlxoLVVKBmeIbQLPiQqqyUWmqGNPVAlIepIKo62dV2IIYSCxrcXP+GW7mnqH9pPvqGHNfCQmyT8A==; fgsscgib-w-mvideo=TCvJ27da7b6f07d1a2b9e38ef7d376603e32d758; fgsscgib-w-mvideo=TCvJ27da7b6f07d1a2b9e38ef7d376603e32d758; cfidsgib-w-mvideo=pntBHuBBrZgtSmliyeoFHChA4v5AkrDVEz9UgBhC2ciznEDwynjqD9eqqZ2ganDwGSaXju+WHRNm72+3D0Yka3OXpjXSU6x50eq71TZdiZLdMXc3fF+vV2jD93apHc25wG1RaLuHL/J1VXnRxKnonLNbebqqpb8VAxGL; CACHE_INDICATOR=false; _sp_id.d61c=a43b1426-3afb-4745-a67e-ab308db7b1e4.1662888994.1.1662889536..3c1e97e6-8cd5-472c-89d6-c478b4f7fb3a..06724bec-d372-4bbb-81a8-9338b1a96f5a.1662888993600.8; _ga=GA1.2.831528810.1662888993; MVID_ENVCLOUD=prod2; tmr_detect=0%7C1662889545973; tmr_reqNum=97; _ga_CFMZTSS5FM=GS1.1.1662888993.1.1.1662889567.0.0.0; _ga_BNX5WPP3YK=GS1.1.1662888993.1.1.1662889567.13.0.0',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '510c3d9794ee406ebfe492b4756ba730-b67a93663e60ca26-0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-set-application-id': '70b272f3-a94f-430b-ae73-d36cd95648b8',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    #print(response)

    products_ids = response.get('body').get('products')
    """создаем переменную products_ids и записываем в файл id из products"""

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    #print(products_ids)
    """создаем словарь"""
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        """создание списка []"""
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)
    #print(len(response.get('body').get('products')))

    """преобразование строки с разделителем ,"""
    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()
    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}
    material_prices = response.get('body').get('materialPrices')

    """цикл для получения id, цены, скидки, бонуса по всему списку"""
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')
        """присваиваем к item_id (id продукта) словари с ценой и скидкой, бонусом"""
        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)
"""функция обработки файлов для формирования результирующего файла"""
def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False )


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
