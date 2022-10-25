from bs4 import BeautifulSoup
from selenium import webdriver
import pprint
from unidecode import unidecode

pp = pprint.PrettyPrinter()


def start_selenium(url):
    # Settings of webdriver
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    try:
        driver.current_url
    except:
        print("The incorrect link")
        exit(0)
    return driver


driver = start_selenium(
    "https://aliexpress.ru/item/1005002841283056.html?spm=a2g2w.detail.seller_rcmd.4.482b2547QMaAK3&_evo_buckets=165609,165598,188873,194275,299287,224373&sku_id=12000022420107922&gps-id=pcDetailBottomMoreThisSeller&scm=1007.13339.291025.0&scm_id=1007.13339.291025.0&scm-url=1007.13339.291025.0&pvid=496dd18e-a026-4c37-a2ea-e3666b3ec68a&_t=gps-id:pcDetailBottomMoreThisSeller,scm-url:1007.13339.291025.0,pvid:496dd18e-a026-4c37-a2ea-e3666b3ec68a,tpp_buckets:21387%230%23233228%235_21387%239507%23434562%237")

info = {
    'name': '',
    'price': '',
    'delivery from': [],
    'models': [],
    'colors': [],
    'photo_links': [],
}

try:
    soup = BeautifulSoup(driver.page_source, 'lxml')
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
