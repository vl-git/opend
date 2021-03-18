import bs4
import pandas as pd
file = open('data1.xml', 'r', encoding='utf8')
soup = bs4.BeautifulSoup(file)
lst = []
for row in soup.find_all('row'):
    l1 = []
    if row.find('report_period_begin').text.startswith('2020-01-01')\
            and row.find('report_period_end').text.startswith('2020-12-01')\
            and not (('ФО' in row.find('region_name').text) or ('Российская федерация' in row.find('region_name').text)):
        l1.append(row.find('region_name').text.strip())
        l1.append(row.find('value').text.strip())
        lst.append(l1)
pd.DataFrame(lst, columns=['субъект', 'количество преступлений']).sort_values('субъект').to_csv('output1.csv', encoding='utf-16', index=False)