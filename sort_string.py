s = input('Введите слова через пробел');
parts = s.split(" ");
newParts = [];
for i in parts:
    if len(i) <= 3: newParts.append(i) 
print('Вы ввели : ',parts);
print('Отсортированный список :',newParts);