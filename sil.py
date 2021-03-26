from sub import set_parser
f1 = open('crime_final_coef.csv', 'r', encoding='utf8')
f_sil = open('численность сотрудников мвд.csv', 'r', encoding='utf8')
# set1 = set()
# set2 = set()
# set_parser(f1, set1)
# set_parser(f_sil, set2)
# for i in (set1 ^ set2):
#     print(i)
dict_people = {}
dict_mvd = {}

for row in f1.readlines()[1:]:
    row = row.split(',')
    dict_people[row[0]] = int(row[1])

for row in f_sil.readlines()[1:]:
    row = row.split(',')
    dict_mvd[row[0]] = int(row[1])

print(dict_people)
print(dict_mvd)

dict_final = {}
fieldnames = ['Регион', 'Количество силовиков на человека']
with open('mvd_coef.csv', 'w', encoding='utf8') as f:
    for k, v in dict_people.items():
        dict_final[k] = '%.4f' % (dict_mvd[k]/v)
    print(','.join(fieldnames), file=f)
    for k, v in dict_final.items():
        print(f'{k},{v}', file=f)
