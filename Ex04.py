# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


# data = open('file.txt', 'r+') # код для удаления данных из файла
# data.seek(0)
# data.truncate()
# data.close()

# exit()
n = int(input('Введите размер списка: '))
list_number = list(range(-n, n+1))
print(list_number)

composition = 1
for i in range(n):
    composition = list_number[i] * composition
    str(composition)
    data = open('file.txt', 'a')
    data.write(f'{composition}\n')
    data.close()
    int(composition)
    n += 1
    print(composition)