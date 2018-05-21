# -*- coding: UTF-8 -*-
from selenium import webdriver
import json

# 这是中文 UTF-8 文件
products = []

# read config
with open("series.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)

# get product list
driver = webdriver.Chrome()
driver.get('https://www.watchguard.com/wgrd-products/appliances-compare')

for s in json_data[u'series']:
    newOptions = driver.find_elements_by_css_selector('#p1 optgroup[label="' + s + '"] option')
    for option in newOptions:
        products.append(option.text)

# iterate over all product and get compare url
for x in range(0,len(products),3):
    driver.get('https://www.watchguard.com/wgrd-products/appliances-compare')

    print type(products[x])
    print "xpath is %s" % '//select[@id="p1"]/*/option[text()="' + products[x].encode("utf-8") + '"]'
    driver.find_element_by_xpath('//select[@id="p1"]/*/option[text()="' + products[x].encode("utf-8") + '"]').click()
    driver.find_element_by_xpath('//select[@id="p2"]/*/option[text()="' + products[x+1].encode("utf-8") + '"]').click()
    driver.find_element_by_xpath('//select[@id="p3"]/*/option[text()="' + products[x+2].encode("utf-8") + '"]').click()

    # submit our compare request
    driver.find_element_by_xpath('//form[@id="products_select_form"]/input').click()
    print "url after we submit =  %s" % driver.current_url

driver.quit()
