from bs4 import BeautifulSoup
from selenium import webdriver
import pprint
from unidecode import unidecode
import os
import sys

pp = pprint.PrettyPrinter()
# the path for the geckodriver
geckodriver = ''
url = input()
info = {
    'name': '',  # the full name of product
    'price': '',  # the price with discount
    'delivery from': [],  # the countries from was delivered
    'models': [],  # all models, that allowed and not.
    'colors': [],  # allowed colors
    'photo_links': [],  # the link on photo
}

if sys.platform == "linux":
    geckodriver = os.getcwd() + os.sep + "linux_geckodriver"
elif sys.platform == "win32":
    geckodriver = os.getcwd() + os.sep + "win_geckodriver.exe"
else:
    print("The unknown OS")


def start_selenium(url, geckodriver=None):
    # Settings of webdriver
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    if geckodriver:
        driver = webdriver.Firefox(executable_path=geckodriver, options=options)
    else:
        driver = webdriver.Firefox(options=options)
    driver.get(url)
    try:
        driver.current_url
    except:
        print("The incorrect link")
        exit(0)
    return driver


driver = start_selenium(url, geckodriver)


try:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # 3 big table [0] is delivery from [1] is models [2] is colors
    soup_info = soup.find_all('div', class_="SnowSku_SkuPropertyItem__skuProp__g2xnf")

    info['name'] = soup.find('h1',
                             'snow-ali-kit_Typography__base__1shggo snow-ali-kit_Typography-Primary__base__1xop0e snow-ali-kit_Typography__strong__1shggo snow-ali-kit_Typography__sizeHeadingXXL__1shggo SnowProductDescription_ProductName__name__13aa7 SnowProductDescription_ProductName__name-lines-2__13aa7').getText()

    info['price'] = unidecode(soup.find('div', class_="snow-price_SnowPrice__mainS__ugww0l").getText())

    info['delivery_from'] = [i.getText() for i in soup_info[0].find_all("span",
                                                                        class_="snow-ali-kit_Typography__base__1shggo snow-ali-kit_Typography-Primary__base__1xop0e snow-ali-kit_Typography__strong__1shggo")]
    info['models'] = [i.getText() for i in soup_info[1].find_all("span",
                                                                 class_="snow-ali-kit_Typography__base__1shggo snow-ali-kit_Typography-Primary__base__1xop0e snow-ali-kit_Typography__strong__1shggo")]
    info['colors'] = [i.getText() for i in soup_info[2].find_all("span",
                                                                 class_="snow-ali-kit_Typography__base__1shggo snow-ali-kit_Typography-Primary__base__1xop0e snow-ali-kit_Typography__strong__1shggo")]
    info['photo_links'] = [i['src'] for i in soup.find("div", class_="gallery_Gallery__picList__re6q0q").find_all("img",
                                                                                                                  class_="gallery_Gallery__image__re6q0q")]
    pp.pprint(info)
except:

    driver.close()

driver.close()
