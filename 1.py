'''Перед началом создания программы для оптимизации поиска препаратов, необходимо удалить из списка ученых, которые выдают препарат за свой. 
Определить злоумышленника очень просто: оригинальный препарат имеет самую раннюю дату создания. 
Все что идет позже - фейк. 
Создайте новый файл с названием scientist_origin.txt (данные должны быть отсортированы по дате в порядке возрастания). 
Вам также необходимо срочно найти всех подельников препарата Аллопуринол, так как их рецептура неверна и из-за этого пострадало много людей. 
Отправьте отчет полиции в формате:'''            

with open('scientists.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    #Отфильтруем данные по Аллопуринол
    data = [i for i in data if 'Аллопуринол' in i]
    #Убираем разделители в data '#'
    data = [i.replace('#', ',') for i in data]
    #Отсортировываем по дате создания
    data = sorted(data, key=lambda x: x.split(',')[2])
    print('Разработчиками Аллопуринола были такие люди:')
    #<ФИО ученого> - <Дата создания>
    for i in data:
        print(i.split(',')[0], '-', i.split(',')[2])
    print('Оригинальный рецепт принадлежит:', data[0].split(', ')[0].split(',')[0])

#Сохраняем данные из data в файл scientist_origin.txt 
with open('/home/user/Документы/it-megapolis-potencial/scientist_origin.txt', 'w', encoding='utf-8') as f:
    f.write(data[0].split(',')[0].split(',')[0])
