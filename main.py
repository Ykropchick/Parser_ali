from bs4 import BeautifulSoup
from selenium import webdriver
import pprint
import os
import sys
import undetected_chromedriver as uc
import json

pp = pprint.PrettyPrinter()
# the path for the geckodriver
geckodriver = ''
url = "https://aliexpress.ru/item/1005001835330458.html?tt=MG&af=1954_10546_19&utm_campaign=1954_10546_19&aff_platform=api-new-link-generate&srcSns=sns_VK&utm_medium=cpa&cn=20rurktlyhifkd1isq13y0mxbpuri4fy&dp=20rurktlyhifkd1isq13y0mxbpuri4fy&aff_fcid=658d1071518e4b04a383355296e109a5-1667560553911-02769-_DmADAX5&cv=2&spreadType=socialShare&aff_fsk=_DmADAX5&sk=_DmADAX5&aff_trace_key=658d1071518e4b04a383355296e109a5-1667560553911-02769-_DmADAX5&businessType=ProductDetail&terminal_id=6c2cbdab3a43481d8e2bff50e4fc13ca&utm_source=aerkol&utm_content=2&sku_id=12000017796376430"
info = {
    'name': '',  # the full name of product
    'price': '',  # the price with discount
    'delivery from': [],  # the countries from was delivered
    'models': [],  # all models, that allowed and not.
    'colors': [],  # allowed colors
    'photo_links': [],  # the link on photo
}


def start_selenium(url):
    # Settings of webdriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--incognito')
    options.headless = True
    driver = uc.Chrome(options=options)
    driver.get(url)
    print("The browser was opened")
    try:
        driver.current_url
    except:
        print("The incorrect link")
        exit(0)
    return driver



driver = start_selenium(url)

try:

    soup = BeautifulSoup(driver.page_source, 'lxml')
    soup_json = soup.find("script", id="__AER_DATA__").text
    data = json.loads(soup_json)

    product_info = data['widgets'][3]['children'][0]['children'][0]['children'][0]['props']
    name = product_info['name']
    product_char = product_info['skuInfo']['propertyList']

    characteristics = {}

    characteristics['название'] = name
    characteristics['рейтинг'] = product_info['rating']['middle']

    for char in product_char:
        ls = []
        for value in char['values']:
            ls.append({
                value['name']: value['displayName']
            })
        characteristics[char['name']] = ls


    photos = []
    for photo in product_info['gallery']:
        photos.append(photo['imageUrl'])
    characteristics['ссылки на фото'] = photos

    pp.pprint(characteristics)


except Exception as e:
    print(e)
    driver.close()

driver.close()
