from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.chrome.service import Service

"""proxy_ip_port = '124.40.251.146'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)"""

import scrap
import json
f2 = open('job_search.json')
f = open('user.json')
data = json.load(f)
title = json.load(f2)
email=data[0]['Email']
password=data[0]['Password']
#, desired_capabilities=capabilities
s = Service('C:\\Users\\ameer.hamza\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
## The csv file objects will come here
# t = 'Electrical Engineer'
# t.replace(' ','+')
# l = 'Sydney'
# l.replace(' ','+')
# for next page we will update p varaible
page=0
scrap.login(email,password)
for i in range(0,len(title)):
    t=title[i]['Departments']
    t.replace(' ', '+')
    l=title[i]["Locations"]
    l.replace(' ', '+')

    scrap.scrap_all(page,t,l)







