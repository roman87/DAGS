from selenium import webdriver
import pandas as pd
from time import sleep
from lxml import html
import itertools

class Extract:
    
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def open_web(self):
        url = 'https://bank.gov.ua/control/uk/curmetal/currency/search/form/day'
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def get_data(self):

        element = self.driver.find_element_by_xpath('//*[@id="from"]')
        element.click()
        
        #select year
        element = self.driver.find_element_by_xpath('/html/body/div/div/div/select[2]')
        element.click()
        items = element.find_elements_by_tag_name("option")
        years = []
        for item in items:
            years += [item.text]
        a = years.index(str(self.year))
        items[a].click()

        #select month
        element = self.driver.find_element_by_xpath('/html/body/div/div/div/select[1]')
        element.click()
        mon = element.find_elements_by_tag_name("option")
        b = int(self.month) - 1
        mon[b].click()

        #select day
        element = self.driver.find_element_by_link_text(str(self.day))
        element.click()

        #get data
        element = self.driver.find_element_by_xpath('//input[@value="table"]')
        sleep(2)
        element.click()
        element = self.driver.find_element_by_xpath('//input[@value="Виконати"]')
        sleep(2)
        element.click()
        content = self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td[2]/div[4]/table[4]')
        table = '<table>' + content.get_attribute("innerHTML") + '</table>'
        dfs = pd.read_html(table, header=0)[0]
        dfs_pd = dfs.values.tolist()
        return dfs_pd

    def close_web(self):
        self.driver.close()
