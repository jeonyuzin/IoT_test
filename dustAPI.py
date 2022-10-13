from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus,unquote
import requests


url= 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
queryParams='?'+urlencode({quote_plus('serviceKey'):'vk43nIgoL/ro1eIOFEx5Ta4DlhoaT8072DeItGhU4a2yzGMzlPs+hD7N3hLQnmhYKUfInHtvU7gg6fDfVp909A=='
        ,quote_plus('returntype'):'xml'
        ,quote_plus('numOfRows'):'10'
        ,quote_plus('pageNo'):'1'
        ,quote_plus('stationName'):'주안'
        ,quote_plus('dataTerm'):'DAILY'
        ,quote_plus('ver'):'1.0'})


print('작동중\n')
res=requests.get(url+queryParams)
soup=BeautifulSoup(res.content,'html.parser')
data=soup.find_all('item')
print(data)

for item in data:
    dataterm=item.find('datatime')
    pm25value=item.find('so2grade')
    print(dataterm.get_text())
    print(pm25value.get_text())

