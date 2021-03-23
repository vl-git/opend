"""import pandas as pd
df = pd.read_excel('data_mvd.xls', names=['Регион', 'Количество'], sheet_name=0, usecols=[2, 3], skiprows=4)
df = df['Регион'].str.strip()
df.to_csv('data_mvd.csv', index=False)
fin = open('data_mvd.csv', 'r', encoding='utf8')
fout = open("data_mvd_sorted.csv", 'w', encoding='utf8')
exceptions = ['федеральный округ', 'Российская Федерация']"""
f_l_t = open('low_tyazh.csv', 'r', encoding='utf8')
f_m_t = open('mid_tyazh.csv', 'r', encoding='utf8')
f_o_t = open('os_tyazh.csv', 'r', encoding='utf8')
f_t = open('tyazh.csv', 'r', encoding='utf8')
f_nas = open('население.csv', 'r', encoding='utf8')
fout = open('население1.csv', 'w', encoding='utf8')


def replacer(file):
    for row in file:
        row = row.replace('автономный округ', 'АО').strip()
        print(row, file=fout)


replacer(f_nas)
f_nas.close()
fout.close()



# TODO: коэф безопасности (4 частных + общий); коэф силовиков