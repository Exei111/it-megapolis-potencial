#Открываем файл и читаем его в список со словарями
with open(r'scientists.txt', encoding='utf-8') as file:
    reader = file.readlines()
    data = [i.replace('#', ',') for i in reader]
    #Сортируем данные по столбцу с датой
    data = sorted(data, key=lambda x: x.split(',')[2])
    for x in range(len(data)):
        data[x] = data[x].replace('-', '.')
    
date = input()

while date != 'эксперимент':
    for row in data:
        if row.split(',')[2] == date:
            surname, name, patronymic = row['ScientistName'].split(' ')
            print(f'Ученый {surname} {name[0]}. {patronymic[0]}.  создал препарат: {row["preparation"]} - {row["date"]}')
            break
    else:
        print("Ничего не найдено")
    date = input()
