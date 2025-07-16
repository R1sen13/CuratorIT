#Перед решением надо сделать два файлика, в которых в первом столбике будет буква программы для разделения листов
#Первый файл - до изменения русского, второй с новым русским
f = open('26.1.txt')
listA, listB, listC = [],[],[]

for s in f: #Формирование матрицы для каждого листа 
    x = [x for x in s.split()]
    res = x
    if len(res)==5: #Проверка на первую строчку
        res = [int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[2])+int(x[3])+int(x[4])] #Переводим в целочисленные и добавляем конкурсные баллы
    if x[0]=='A':
        listA.append(res)
    elif x[0] == 'B':
        listB.append(res)
    else:
        listC.append(res)
        
znachA = listA[0] #Создаем отдельный массив со значениями для листа А
znachA = znachA[1:] #Избавляемся от определителя листа
listA = listA[1:] #Делаем срез для удобства в дальнейшем переборе и сортировке
znachB = listB[0] #Создаем отдельный массив со значениями для листа B
znachB = znachB[1:] 
listB = listB[1:] #Делаем срез для удобства в дальнейшем переборе и сортировке
znachC = listC[0] #Создаем отдельный массив со значениями для листа C
znachC = znachC[1:] 
listC = listC[1:] #Делаем срез для удобства в дальнейшем переборе и сортировке

budgeA, budgeB, budgeC = [],[],[]
listA.sort(key = lambda x:[x[4], x[int(znachA[1])]], reverse = True) #Сортировку по ИД можно не делать, так как в задаче она уже отсортирована
listB.sort(key = lambda x:[x[4], x[int(znachB[1])]], reverse = True)
listC.sort(key = lambda x:[x[4], x[int(znachC[1])]], reverse = True)
for i in range(int(znachA[2])-int(int(znachA[2])*0.1)): #Перебираем места на бюджет с учетом 10% для льготников
    budgeA.append(listA[i])
for i in range(int(znachB[2])-int(int(znachB[2])*0.1)):
    budgeB.append(listB[i])
for i in range(int(znachC[2])-int(int(znachC[2])*0.1)):
    budgeC.append(listC[i])
    
kA,kB,kC=0,0,0
sA,sB,sC=0,0,0
for s in budgeA: #Начинаем перебирать значения и искать финальный результат
    if int(s[0]) == 387:
        kA=-1
        sA=-387
    kA+=1
    sA+=int(s[0])
for s in budgeB:
    if int(s[0]) == 387:
        kB=-1
        sB=-387
    kB+=1
    sB+=int(s[0])
for s in budgeC:
    if int(s[0]) == 387:
        kC=-1
        sC=-387
    kC+=1
    sC+=int(s[0])
    
if kC == len(budgeC): #Проверка был ли у нас на бюджете Ваня, если не был, то сумму ИД обнуляем для рещультата
    sC=0
    kC=10**10
if kA == len(budgeA):
    sA=0
    kA=10**10
if kB == len(budgeB):
    sB=0
    kB=10**10
    
res1, res2 =min(kA,kB,kC), max(sA,sB,sC)
if res1 == kA: #Вывод ответа с учетом программы 
    print('A'+str(res1))
if res1 == kB:
    print('B'+str(res1))
if res1 == kC:
    print('C'+str(res1))
if res2 == sA:
    print('A'+str(res2))
if res2 == sB:
    print('B'+str(res2))
if res2 == sC:
    print('C'+str(res2))
#сначала проверяем первый результат на файле 1, а затем используем файл 2 с изменённым русским для второго ответа



    
