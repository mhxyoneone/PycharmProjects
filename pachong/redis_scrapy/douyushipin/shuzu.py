from selenium import webdriver
import re
from bs4 import BeautifulSoup
import lxml
import time
import requests
# web = webdriver.Chrome()
# web.get("https://www.douyu.com/t/0227sansanjiuH5")
#
# soup = BeautifulSoup(web.page_source,'lxml')
# time.sleep(10)
# hot = web.find_element_by_class_name("hot-v-con")
# #hot = soup.find_all('span',{"class":"hot-v"})
# print(hot.text)


# str1 = '<OPTION value="TBD">TBD</OPTION>OPTION'
# res = re.compile('value="(.*?)"')
# print(res.findall(str1))

url = 'https://kingston.tmall.com/p/rd315834.htm?spm=a220o.1000855.w5001-15088576993.18.37f1d940ublHFT&scene=taobao_shop'
res = requests.get(url)
re_text = re.compile('href="(.*?)/search.htm')
compare = re_text.findall(res.text)
print(compare)