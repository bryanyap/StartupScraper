import lxml.html as lh
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from record_types import TechInAsiaRecord

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
file = open('./techinasia_results.txt', 'w')

for i in range(1, 2):
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

                driver.get('https://www.techinasia.com' + row[i][0].get('href'))
                details_html = driver.page_source
                details_doc = lh.document_fromstring(details_html)
                try:
                    details_text = details_doc.xpath('//*[@id="app"]/div/div/div[2]/div/text()')[0]
                except:
                    details_text = 'parsing error'

            elif i == 2:
                result_list.append(row[i][0][4][0].text)
            else:
                result_list.append(row[i].text)

        result_list.append(details_text)
        record = TechInAsiaRecord(result_list)
        file.write(record.getResults() + '\n')

driver.quit()
