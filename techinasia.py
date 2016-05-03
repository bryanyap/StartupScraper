import lxml.html as lh
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from record_types import TechInAsiaRecord

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')

driver = webdriver.Firefox(firefox_binary=binary)

for i in range(1, 3):
    url = 'https://www.techinasia.com/startups?page=' + str(i) + '&sort=+'

    driver.get(url)

    html = driver.page_source

    doc = lh.document_fromstring(html)

    rows = doc.xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/table/tbody/tr')

    for row in rows:

        result_list = []
        details_text = ''

        for i in range(6):
            if i == 0:
                result_list.append(row[i][0].text)

                details_driver = webdriver.Firefox(firefox_binary=binary)
                details_driver.get('https://www.techinasia.com' + row[i][0].get('href'))
                details_html = details_driver.page_source
                details_doc = lh.document_fromstring(details_html)
                details_text = details_doc.xpath('//*[@id="app"]/div/div/div[2]/div/text()')[0]
                details_driver.quit()

            elif i == 2:
                result_list.append(row[i][0][4][0].text)
            else:
                result_list.append(row[i].text)

        result_list.append(details_text)
        result = TechInAsiaRecord(result_list)

# driver.quit()
