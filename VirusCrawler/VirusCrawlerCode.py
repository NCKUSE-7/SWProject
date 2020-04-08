#from __future__ import unicode_literals
import bs4
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen


def crawler():
    tStart = time.time()
    option = webdriver.ChromeOptions()
    option.headless = True
    browser = webdriver.Chrome(options=option)
    url = "https://www.taoyuan-airport.com/main_ch/revised_flight.aspx?uid=159&pid=12"
    unloaded = True
    while unloaded:
        try:
            browser.get(url)
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'tt_body')))
            unloaded = False
            html_source = browser.page_source
            browser.quit()
        except TimeoutException:
            print("timeout! auto retry!")
            unloaded = True
    root = bs4.BeautifulSoup(html_source, "html5lib")
    flights = root.find("tbody", class_="tt_body").findAll("tr")
    flight_info = {

    }
    count = 0
    for flight in flights:
        raw_flight_table_infos = flight.findAll("td", class_="flight-table-info")
        temp = ""
        if raw_flight_table_infos:
            airline_logos = raw_flight_table_infos[2].findAll("img")
            airline_names = raw_flight_table_infos[2].findAll("span")
            flight_numbers = raw_flight_table_infos[3].findAll("span")
            temp0 = raw_flight_table_infos[0].get_text()
            temp1 = raw_flight_table_infos[1].get_text()
            for airline_logo in airline_logos:
                temp2 = "https://www.taoyuan-airport.com" + airline_logo['src'] + " "
            temp2 = temp2.rstrip()
            for airline_name in airline_names:
                temp3 = airline_name.get_text() + " "
            temp3 = temp3.rstrip()
            for flight_number in flight_numbers:
                temp4 = flight_number.get_text() + " "
            temp4 = temp4.rstrip()
            temp5 = raw_flight_table_infos[4].get_text()
            temp6 = raw_flight_table_infos[8].get_text()
            flight_info['flight'+str(count)] = [ temp0, temp1, temp2, temp3, temp4, temp5, temp6 ]
            count += 1
            if count == 100:
                break
    flight_info_jason = json.dumps(flight_info, ensure_ascii=False, separators=(',\n', ' : '))
    print(flight_info_jason)
    with open('fi_out.json', 'w') as file:
        file.write(flight_info_jason)
    tEnd = time.time()
    print("It cost %.2f sec" % (tEnd - tStart))
    return flight_info_jason

crawler()