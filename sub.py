"""import pandas as pd
df = pd.read_excel('data_mvd.xls', names=['Регион', 'Количество'], sheet_name=0, usecols=[2, 3], skiprows=4)
df = df['Регион'].str.strip()
df.to_csv('data_mvd.csv', index=False)
fin = open('data_mvd.csv', 'r', encoding='utf8')
fout = open("data_mvd_sorted.csv", 'w', encoding='utf8')
exceptions = ['федеральный округ', 'Российская Федерация']"""
f_l_t = open('low_tyazh.csv', 'r', encoding='utf16')
f_m_t = open('mid_tyazh.csv', 'r', encoding='utf16')
f_o_t = open('os_tyazh.csv', 'r', encoding='utf16')
f_t = open('tyazh.csv', 'r', encoding='utf8')
f_nas = open('население1.csv', 'r', encoding='utf8')


# set1 = set()
# set2 = set()
def set_parser(file, set):
    for row in file.readlines()[1:]:
        row = row.split(',')
        set.add(row[0].strip())
    return set


#
#
# set1 = set_parser(f_nas, set1)
# set2 = set_parser(f_l_t, set2)
# for i in (set1 ^ set2):
#     print(i)
dict = {}
for row in f_nas.readlines()[1:]:
    row = row.split(',')
    dict[row[1]] = [int(float((row[3])))]
f_nas.close()


def crime_handler(file):
    for row in file.readlines()[1:]:
        if type(row) is not None:
            row = row.split(',')
            dict.get(row[1].strip()).append(int(row[0]))
    return dict


crime_handler(f_l_t)
crime_handler(f_m_t)
crime_handler(f_t)
crime_handler(f_o_t)

f_l_t.close()
f_m_t.close()
f_o_t.close()
f_t.close()

cfs = {}
for k, v in dict.items():
    people = v[0]
    cfs[k] = [people]
    for c in v[1:]:
        cfs.get(k).append(float('%.4f' % (c / people)))

fieldnames = ['Регион', 'Количество человек', 'Преступлений небольшой тяжести',
              'Преступлений средней тяжести', 'Тяжких преступлений',
              'Особо тяжких преступлений']
with open('crime_per_person.csv', 'w', encoding='utf8') as f:
    print(','.join(fieldnames), file=f)
    for k, v in cfs.items():
        row = [k]
        for value in v:
            row.append(value)
        print(','.join(list(map(str, row))), file=f)
    f.close()

cfs_final = {}
for k, v in cfs.items():
    people = v[0]
    l_t = v[1]
    m_t = v[2]
    t = v[3]
    o_t = v[4]
    cfs_final[k] = [people, '%.5f' % (0.15 * l_t), '%.5f' % (0.35 * m_t), '%.5f' % (0.2 * t), '%.5f' % (0.2 * o_t)]

fieldnames1 = ['Регион', 'Количество человек', 'Коэффициент небольшой тяжести',
               'Коэффициент средней тяжести', 'Коэффициент тяжких',
               'Коэффициент особо тяжких преступлений']

with open('crime_coefs.csv', 'w', encoding='utf8') as f:
    print(','.join(fieldnames1), file=f)
    for k, v in cfs_final.items():
        row = [k]
        for value in v:
            row.append(value)
        print(','.join(list(map(str, row))), file=f)
    f.close()

fieldnames2 = ['Регион', 'Количество человек', 'Коэффициент безопасности']
with open('crime_final_coef.csv', 'w', encoding='utf8') as f:
    print(','.join(fieldnames2), file=f)
    for k, v in cfs_final.items():
        n = 0
        for value in v[1:]:
            n += float(value)
        row = [k, v[0], '%.4f' % n]
        print(','.join(list(map(str, row))), file=f)
    f.close()
