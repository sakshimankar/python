x=(input('enter string'))
lt=[]
lw=[]
ans=""
vow=['a','e','i','o','u']
lt=x.split()
for i in lt:
    l = len(lt)
    for j in range(l-1):
        if i[j] in vow and i[j+1] in vow:
            ans += i+" "
            j = j+1
            break
if ans=="":
    print("invalid input")
else:
    print(ans)
