#PROJECT NO.1 (PASSWORD GENERATOR)

import random
print("Enter number of passwords")
n=int(input())
print("Enter number of words required in password")
w=int(input())

print("\nPasswords are:\n")

for step in range(n):
    z=''
    for step in range(w):
      s=random.randint(97,122)
      p=chr(s)
      z=z+p

    print(z)
print("\n")

