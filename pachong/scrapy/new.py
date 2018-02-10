from bs4 import BeautifulSoup
import lxml
import requests
import re
#url = "https://www.javbus.info/SCOP-490"
url = "https://www.javbus.info/ajax/uncledatoolsbyajax.php?gid=36424242572&lang=zh&img=https://pics.javcdn.pw/cover/6dx6_b.jpg&uc=0&floor=153"
#url = "https://www.javbus.info/ajax/uncledatoolsbyajax.php?gid=36232306927&lang=zh&img=https://pics.javcdn.pw/cover/6dx6_b.jpg&uc=0&floor=153"
#url = "https://www.javbus.info/ajax/uncledatoolsbyajax.php?gid=36417994212&lang=zh&img=https://pics.javcdn.pw/cover/6f58_b.jpg&uc=0&floor=280"
header ={
    'authority':'www.javbus.info',
    'method':'GET',
    'path':'/ajax/uncledatoolsbyajax.php?gid=36417994212&lang=zh&img=https://pics.javcdn.pw/cover/6f58_b.jpg&uc=0&floor=280',
    'scheme':'https',
    'accept':'*/*',
    #'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'cookie':'__cfduid=dbc14b3bc854c776636d1035548a5f54e1516261025; HstCfa3288802=1516261062336; HstCmu3288802=1516261062336; __dtsu=2DE7B66BC84E605AC20C3E85029CA511; PHPSESSID=4jvt428b36d9jjd4npc5vism55; HstCla3288802=1518094188397; HstPn3288802=1; HstPt3288802=19; HstCnv3288802=4; HstCns3288802=6',
    'referer':'https://www.javbus.info/BSTC-017',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'x-requested-with':'XMLHttpRequest'
}

response = requests.get(url,headers=header)
resp = response.text
soup = BeautifulSoup(resp,'lxml')
# href = soup.select('body > script:nth-of-type(3)')[0]
#
# id = re.compile(r'\d+')
# pat = id.findall(str(href))[0]
# #for link in soup:
#print(pat)
print(soup.contents)
