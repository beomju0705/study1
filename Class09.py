
for i in range(5): # 사각형별
    for j in range(5):
        print("*", end=" ")
    print()

lst = ["*"*5 for _ in range(5)]
print(lst)

for i in range(5):
    for j in range(5):
        if i >= j:
            print('*', end="")
        else:
            print()
            break
print()

lst = []
for i in range(5): # 계단식 별
    temp = ""
    for j in range(i+1):
        temp += "*"
    lst.append(temp)

for i in lst:
    print(i)
print(lst)

lst = ["*"*(i+1) for i in range(5)]

for i in lst:
    print(i)
print(lst)

lst = []
for i in range(5): #대각선 별
    temp = ""
    for j in range(5):
        if i==j:
            temp += "*"
            break
        else:
            temp += " "
    lst.append(temp)

for i in lst:
    print(i)
print(lst)


lst = [" "*i + "*" for i in range(5)]

for i in lst:
    print(i)
print(lst)


lst = ["*"*(5-i) for i in range(5)] #계단식 역순

for i in lst:
    print(i)
print(lst)

for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end="")
    print()

lst = []
for i in range(5):
    temp = ""
    for j in range(5):
        if i <= j: #(0:01234) (1:1234) (2:234) (3:34) (4:4) <- (5) (4) (3) (2) (1)
            temp += "*"
        else:
            temp += " "
    lst.append(temp)

for i in lst:
    print(i)
print(lst)

lst = [["*" for i in range(5-j)] for j in range(5)]
lst = ["*"*(5-i) for i in range(5)]
for i in lst:
    print(i)
print(lst)


lst = [" "*i + "*"*(5-i) for i in range(5)]
for i in lst:
    print(i)
print(lst)

lst = ["*"*(i+1) for i in range(5)]

for i in reversed(lst):
    print(i)
print(lst)

