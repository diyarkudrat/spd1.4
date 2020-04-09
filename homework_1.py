a = [1, 2, 2, 3, 3, 4, 4]

b = []
for i in a:
    for j in a[i+ 1]:
        if i ==j:
            b.append(i)

print(b)