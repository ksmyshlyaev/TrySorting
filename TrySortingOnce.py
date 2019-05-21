# Вывести все НЕ уникальные элементы списка по одному разу каждый

l = [1, 2, 3, 1, 3, 4, 6, 3, 3, 3, 7, 7, 8, 8, 8]
s = []
for i in l:
    if l.index(i) == len(l)-1:
        break
    if i not in s:
        if i in l[l.index(i)+1:]:
            s.append(i)
print(s)