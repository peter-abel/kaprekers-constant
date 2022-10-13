
a= []
for i in range(0,6):
    a.append(i)
print(a)

for j in a:
    if j==2 or j==3 or j==0:
        a.remove(j)

print(a)
print(a[1])        
