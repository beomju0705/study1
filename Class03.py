# x = int(input("찾고자 하는 값을 입력해주세요 : "))
#
# a = [1,1,2,2,3,3]
# print(a.count(x))
#
# #count 함수 원리 구현해보기
# for i in range(len(a)):
#
#  a = [1,2,3]
# # a.reverse() #[3,2,1]
#
# #reverse 함수 원리 구현해보기
# b = []
# for i in range(len(a)-1, -1, -1): #for(int i=a.length-1; i>-1; i--)
#     b.append(a[i])
#
# print(b)
#
# start, end = 0, len(a)-1
# temp = 0
# while end > start:
#     temp = a[start]
#     a[start] = a[end]
#     a[end] = temp
#     start += 1
#     end -= 1
#
# print(a)
#
# for i in range(len(a)//2):
#     temp = a[i]
#     a[i] = a[len(a)-i-1]
#     a[len(a) - i - 1] = temp

# print(a)

#2x5 이차원 리스트 만들어서 1~10까지 채우기
lst = [
         [1,2],
         [3,4],
         [5,6],
         [7,8],
         [9,10]
       ]

print(len(lst))
print(len(lst[0]))

for i in range(len(lst)) :
    for j in range(len(lst[0])) :
        lst[i][j] = 2*i+j+1

for i in range(len(lst)) :
    for j in range(len(lst[0])) :
        print(lst[i][j], end=" ")
    print()

lst = []
num = 1

for i in range(5):
    temp  = []
    for j in range(2):
        temp.append(num)
        num += 1
    lst.append(temp)

print(lst)


s = 123456
lst = []

while s > 0:
    #lst.insert(0, s%10)
    lst.append(s%10)
    s = s // 10
lst.reverse()
print(lst)

s = 123456
num = 10
count = 1

while s > num:
    num *= 10
    count += 1

print(count)
print(s//10**count)

while s > 0:
        lst.append(s//10**count)
        s = s % 10**count
        count -= 1

print(lst)


# 3번
#list 함수 원리 구현해보기 (숫자로)
# s = 123456
# lst = list(s)
# print(lst)
#오답
#1. s="123456"
#2. s=[1,2,3,4,5,6]
#3. s2=str[s]

# (1) [3,6,9,20,-7,5] 리스트를 sort와 같은 함수를 사용하지 말고 for문을 활용하여 오름차순으로 정렬하세요.