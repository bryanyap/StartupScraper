import random
import time
from sys import argv

import lxml.html as lh
from progressbar import ProgressBar
from selenium import webdriver

from record_types import TechInAsiaRecord
from startupdetails import StartupDetailsScraper

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

    driver = webdriver.Firefox()

    file = open('./techinasia_results.txt', 'w')
    file.write('name\tlocation\tindustries\tstage\tlatest_funding\tfunded_date\tdesc\turl\tjson' + '\n')

    bar = ProgressBar(max_value=(args[1] - args[0]) * 20)
    progress_counter = 0
    bar.update(progress_counter)

    print 'Scraping'
    for i in range(args[0], args[1]):
        url = 'https://www.techinasia.com/startups?page=' + str(i) + '&sort=+'

        driver.get(url)
        html = driver.page_source
        doc = lh.document_fromstring(html)
        rows = doc.xpath('//*[@id="app"]/div/div/div[2]/div[2]/div/table/tbody/tr')

        details_scrapers = []
        records = []

        for j in range(len(rows)):
            row = rows[j]
            record = TechInAsiaRecord()
            records.append(record)

            for k in range(6):
                if k == 0:
                    record.set_name(row[k][0].text)
                    startup_url = 'https://www.techinasia.com' + row[k][0].get('href')
                    record.set_url(startup_url)

                    startup_api_url = 'https://www.techinasia.com/api/2.0' + row[k][0].get('href')
                    details_scraper = StartupDetailsScraper(startup_api_url)
                    details_scrapers.append(details_scraper)

                    time.sleep(random.random())
                    details_scraper.start()
                    details_scraper.join()

                    progress_counter += 1
                    bar.update(progress_counter)

                elif k == 1:
                    try:
                        record.set_location(row[k].text)
                    except:
                        pass
                elif k == 2:
                    try:
                        record.set_industries(row[k][0][4][0].text)
                    except:
                        pass
                elif k == 3:
                    try:
                        record.set_stage(row[k].text)
                    except:
                        pass
                elif k == 4:
                    try:
                        record.set_latest_funding(row[k].text)
                    except:
                        pass
                elif k == 5:
                    try:
                        record.set_funded_date(row[k].text)
                    except:
                        pass

        for j in range(len(details_scrapers)):
            details_scrapers[j].join()

            records[j].set_desc(details_scrapers[j].get_pitch())
            records[j].set_json(details_scrapers[j].get_json())

            file.write(records[j].get_results() + '\n')

    driver.quit()
    file.close()
    bar.finish()

    print 'Done'
