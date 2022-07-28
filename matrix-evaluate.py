n =int(input("Enter a frist number: "))
m =int(input("Enter a second number: "))
add = []
lis = []
lis1 = [1]
tem = 1 
for i in range(n):
    lis.append([])
    lis1.append(lis1[i]+tem)
    if tem<m:
        tem+=1
for i in range(len(lis1)-1):
    lis[i].append(lis1[i])
val = 2
val1 = 2
for j in range((m//2)+1):
    for i in range(m-1):
        if (val1-1)*2 < m:
            add.append(val)
            if val<n:
                val+=1
        else:
            if i < (m-1)//2:
                add.append(val)
                if val<n:
                    val+=1
            else:
                add.append(val)
                val-=1
    for i in range(1,m):
        if (add[0]-1)*2 < m:
            lis[add[0]-2].append(lis[add[0]-2][i-1] + add[i-1])
            lis[-(add[0]-1)].append(lis[-(add[0]-1)][i-1] + add[-i])
        else:
            lis[add[0]-2].append(lis[add[0]-2][i-1] + add[i-1])
    val = add[1]
    val1 = add[1]
    add = []
print(lis)
for i in lis:
    print(' '.join(map(str, i)))
