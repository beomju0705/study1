a = [[10,20], [30,40], [50,60]]
b = [[2,3], [4,5], [6,7]]
lst = []
temp = []

for i in range(len(a)):
    for j in range(len(a[i])):
        temp.append(a[i][j]*b[i][j])
    lst.append(temp)
    temp = []

print(lst)

# [[1,2], [3,4], [5,6]] 리스트 컴프리헨션으로 만들기
# b = [[j*10+i+1 for i in range(10)] for j in range(10)] 1부터 100까지
# print(b)
b = [[2*j+i+1 for i in range(2)] for j in range(3)]
print(b)
# b = [[i+1 for i in range(2)] for j in range(3)] j = 0 , 1, 2 i = [1,2] [3,4] [5,6]
# print(b)

# 2차원 10x10 리스트 0으로 채우기 컴프리헨션으로 만들기

a = [0,0,0,0,0,0,0,0,0,0]
b = [[0 for i in range(10)] for _ in range(10)]
print(b)

lst = []
num = 0
for i in range(10):
    temp = []
    for j in range(10):
        temp.append(num)
        num += 0
    lst.append(temp)
print(lst)

# 100이하의 소수(약수가 1과 자기자신)으로 이루어진 1차원 리스트 컴프리헨션으로 만들기
prime_number = []
for i in range(2, 101):
    for j in range(2, i):
        if i%j == 0:
            break
        elif i-1 ==j :
            prime_number.append(i)

print(prime_number)

# prime_number = [i for i in range(2,101) if i%j != 0 for j in range(2,i)]

#all함수, any함수
#여러 개의 조건 or 값이 있는 리스트, 튜플, set... 값의 조건에 따라 True or False 리턴하는 함수

#all함수 : 모든 값이 True일 때, True
#any함수 : 하나라도 True면 True 리턴한다.

number = [i+1 for i in range(10)] #1~10
lst = [x for x in number if x % 2 == 0]

res = all(x%2 == 0 for x in number)
print(lst)

res = all(x%2 == 0 for x in lst)
print(res)

res = any(x == 5 for x in number)
print(res)

res = any(x == 5 for x in lst)
print(res)

prime_number = [i for i in range(2, 101) if all(i&j !=0 for j in range(2,i))]
print(prime_number)


# a = [ i * j for i in range(0,5) for j in range(0,5)]

# print(a)


