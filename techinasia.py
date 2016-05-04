from sys import argv

import lxml.html as lh
from progressbar import ProgressBar
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from record_types import TechInAsiaRecord

if len(argv) != 3:
    print 'Please key in the necessary inputs'
else:
    args_input = argv
    try:
        args = [int(args_input[1]), int(args_input[2]) + 1]
    except:
        raise ValueError('Please key in numbers')

    if int(args_input[1]) <= int(args_input[2]):
        print 'Scraping pages ' + str(args[0]) + ' to ' + str(args[1] - 1)
    else:
        raise ValueError('Please key in the starting and ending pages in the right order')

    binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    file = open('./techinasia_results.txt', 'w')
    file.write('name\tlocation\tindustries\tstage\tlatest_funding\tfunded_date\tdesc\turl' + '\n')

    bar = ProgressBar(max_value=(args[1] - args[0]) * 20)
    progress_counter = 0
    bar.update(progress_counter)

    for i in range(args[0], args[1]):
        url = 'https://www.techinasia.com/startups?page=' + str(i) + '&sort=+'

        driver.get(url)
        html = driver.page_source
        doc = lh.document_fromstring(html)
        rows = doc.xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/table/tbody/tr')

        for row in rows:
            progress_counter += 1
            bar.update(progress_counter)

            result_list = []
            details_text = ''
            url_string = ''

            for i in range(6):
                if i == 0:
                    result_list.append(row[i][0].text)
                    url_string = 'https://www.techinasia.com' + row[i][0].get('href')

                    driver.get(url_string)
                    details_html = driver.page_source
                    details_doc = lh.document_fromstring(details_html)
                    try:
                        details_text = details_doc.xpath('//*[@id="app"]/div/div/div[2]/div/text()')[0]
                    except:
                        details_text = 'empty'

                elif i == 2:
                    try:
                        result_list.append(row[i][0][4][0].text)
                    except:
                        result_list.append('empty')
                else:
                    try:
                        result_list.append(row[i].text)
                    except:
                        result_list.append('empty')

            result_list.append(details_text)
            result_list.append(url_string)
            record = TechInAsiaRecord(result_list)

            file.write(record.getResults() + '\n')

    driver.quit()
    file.close()
    bar.finish()
