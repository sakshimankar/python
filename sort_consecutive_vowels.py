x=(input('enter sentence:  '))
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
    print("Invalid input")
    print("Sentence does not have any vowels")
else:
    print("The words with consecutive vowels are: ")
    print(ans)

