# Вывести все НЕ уникальные элементы списка столько раз сколько они встречаются

l = [1, 2, 3, 1, 3, 4, 6, 3, 3, 3, 7, 7, 8, 8, 8]
s = []
n = False
for i in l:
    if l.index(i) == len(l)-1:
        break
    if i not in s:
        for j in l[l.index(i)+1:]:
            if j == i:
                s.append(j)
                n = True
        if n:
            s.append(i)
            n = False
print(s)