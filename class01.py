import random

for i in range(0,10):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(10):
    print(i)
#range(1.처음, 2.끝, 3.중간)
#1. 어디부터 시작할래?
#2. 어디까지 할래?
#3. 어떻게 진행할래?

# a = int(input("몇단을 출력할까 : "))
# for i in range(1,10):
#     print(a, "X" , i, " = " , a*i)
#
# for i in range(2,10):
#     print("--------------", i, "단------------")
#     for j in range(1, 10):
#         print(str(i) + " X " + str(j) + " = " + str(i*j))
#     print("%d X %d = %d" %(i,j,i*j))
#
# q = 1
# sum = 0
# while(q != 0):
#     q = int(input("값을 입력해주세요:"))
#     sum += q
#
# print("합계는 ? ",sum)
#
# q = 1
# sum = 0
# while (True):
#     q = int(input("값을 입력해주세요:"))
#     sum += q
#     if q == 0:
#         break
#
# print("합계는 ? ", sum)

a = int(input("몇단을 출력할까 : "))
# for i in range(1,10):
#     print(a, "X" , i, " = " , a*i)

for i in range(3,10,2):
    print("--------------", i, "단------------")
    for j in range(1, 10):
        print(str(i) + " X " + str(j) + " = " + str(i*j))
    print("%d X %d = %d" %(i,j,i*j))

if(a == 1) :
    for i in range(3,10,2):
        print("--------------", i, "단------------")
        for j in range(1, 10):
            print(str(i) + " X " + str(j) + " = " + str(i*j))
        print("%d X %d = %d" %(i,j,i*j))
        print()
elif(a==2) :
    for i in range(2, 10, 2):
        print("--------------", i, "단------------")
        for j in range(1, 10):
            print(str(i) + " X " + str(j) + " = " + str(i * j))
        print("%d X %d = %d" % (i, j, i * j))
        print()




# random = int(input())
# x = int(input())
# for i in range(1,10):
#     print("가위(1), 바위(2), 보(3) 을 입력하세요 : ", random)
#     if(x > 3) :
#         print("게임종료")
