#Hello world -> Hell wrld
s = "Hello world"
print(s.replace("o",""))

lst = list(s)
print(lst)

for i in lst:
    if(i == 'o'):
        continue
    print(i, end='') #print(im end="\n

print()
print(lst[:4] + lst[5:7] + lst[8:len(lst)-1])
#lst[0:4] = "Hell"
#lst[5:7] = "w"
#lst[8:len(lst)

s = ""
for i in lst[:4] + lst[5:7] + lst[8:]:
    s += i

print(s)

s = ""
for i in lst:
    if(i == 'o'):
        continue
    s += i
print(s)

print(lst[:4] + lst[5:7] + lst[8:len(lst)-1])

lst2 = []
start = 0
for i in range(len(lst)):
    if lst[i] == 'o':
        lst2 += lst[start:i] #(0,4) (5,7) (8,len-1)
        start = i+1

print(lst2)

lst = list('helloooooo woorld')

i = 0
while(True):
    if(i == (len(lst))):
        break

    # if lst[i] == 'o':
    # else :
    # print(i)

lst = list('ooooooooooooooooo')





print(lst)

