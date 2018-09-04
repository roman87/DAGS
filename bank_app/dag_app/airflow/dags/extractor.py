from requests import get
from xml.etree import ElementTree as ET
from datetime import datetime

class ExchangeRate:
    def __init__(self, date):
        self.date = date

    def currency_extractor(self):
        url = 'https://api.privatbank.ua/p24api/exchange_rates?date=' + self.date
        page = get(url)
        root = ET.fromstring(page.content)
        dict_base = root.attrib
        matrix = []
        for ex_rate in root.findall('exchangerate'):
            dict_val = dict(ex_rate.attrib)
            if 'currency' in dict_val:
                l = []
                d = dict_base['date']
                s = d.split('.')
                dt = datetime(int(s[2]), int(s[1]), int(s[0]))
                day = str(dt.day)
                month = str(dt.month)
                year = str(dt.year)
                da = day + '-' + month + '-' + year
                l += [da]
                l += [dict_val['currency']]
                l += [dict_val['baseCurrency']]
                l += [float(dict_val['purchaseRateNB'])]
                l += [float(dict_val['saleRateNB'])]
                l += [dict_base['bank']]
                matrix += [l]
        return matrix
        
