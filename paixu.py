a=[33,44,55,22,34,78,99]

j = 0
while(j<6):
        i = 0
        while(i<6):
                if a[i]>a[i+1]:
                	temp = a[i+1]
                	a[i+1] = a[i]
                	a[i] = temp
                i = i+1
        j = j+1
i = 0
print(a[2:5])
