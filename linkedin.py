import json

import lxml.html as lh
from selenium import webdriver

from record_types import LinkedInRecord

urls = ['https://www.linkedin.com/in/sarah-mao-7b958a66', 'https://www.linkedin.com/in/shunhim',
        'https://www.linkedin.com/in/wenyapoh', 'https://www.linkedin.com/in/karen-sng-9908577b',
        'https://www.linkedin.com/in/ngvera', 'https://www.linkedin.com/in/joshuacheong']

driver = webdriver.PhantomJS('C:/phantomjs-2.1.1-windows/bin/phantomjs.exe')

results = list()

for url in urls:
    driver.get(url)
    html = driver.page_source
    doc = lh.document_fromstring(html)

    el_img = ''
    el_name = ''
    el_desc = ''
    el_locale = ''
    el_industry = ''

    try:
        el_img = doc.xpath('//*[@id="topcard"]/div[1]/div[1]/a/img/@src')[0]
        print el_img
    except:
        print 'no image'
    try:
        el_name = doc.xpath('//*[@id="name"]')[0].text
        print el_name
    except:
        print 'no name'

    try:
        el_desc = doc.xpath('//*[@id="topcard"]/div[1]/div[2]/div/p')[0].text
        print el_desc
    except:
        print 'no desc'

    try:
        el_locale = doc.xpath('//*[@id="demographics"]/dd[1]/span')[0].text
        print el_locale
    except:
        print 'no locale'

    try:
        el_industry = doc.xpath('//*[@id="demographics"]/dd[2]')[0].text
        print el_industry
    except:
        print 'no industry'

    results.append(LinkedInRecord([el_name, el_img, 'Position', url]))

print json.dumps([o.dump() for o in results], sort_keys=True, indent=4, separators=(',', ': '))

driver.quit()
