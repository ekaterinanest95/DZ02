# Реализуйте алгоритм перемешивания списка.

elements = list()
for i in range(5):
     a = int(input('Введите элемент списка: '))
     elements.append(a)
print(elements)
elements1 = elements.copy()
elements1.reverse()
elements1.sort()
print(elements1)
