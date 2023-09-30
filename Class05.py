# s = {1,2,3}
#
# s.add(3)
# print(s)

#SET
#사람 3명이 각각 먹고 싶은 여러 개 음식이 있다라고 할 때, 어떤 메뉴를 시키는게 가장 좋을지 (교칩합)
human1 = {"치킨", "햄버거", "피자"}
human2 = {"치킨", "파스타", "밥", "피자","족발","보쌈"}
human3 = {"치킨", "콜라", "누들면", "초밥","족발","피자"}

menu1 = set(human1)
menu2 = set(human2)
menu3 = set(human3)

print(menu1 & menu2 & menu3)

#리스트 상태에서 3명의 공통음식찾기 - 숙제
for i in human1:
    for j in human2:
        for k in human3:
            if(i == j == k):
                print("공통음식 :", i)

for i in human1:
    if i in human2 and i in human3 :
        print("공통음식 :", i)

# 사람 3명이 각각 음식을 여러개 가지고 있다고 할 때, 두 명이 서로 음식을 교환해보자
while True:
    print(menu1)
    print(menu2)
    print(menu3)
    inputSet = int(input("1. 교환, 2. 종료"))

    if inputSet == 1:
        inputSet = int(input("누구와 교환하시겠습니까? 2. human2, 3.human3"))
        if inputSet == 2 :
            myfood = input("어떤 음식을 교환하시겠습니까?")
            yourfood = input("어떤 음식과 교환하시겠습니까?")
            if myfood in menu2 or yourfood in menu1:
                print('이미 가지고 있는 음식입니다. 교환할 수 없습니다.')
            elif myfood in menu1 and yourfood in menu2:
                menu1.add(yourfood)
                menu2.remove(yourfood)
                menu1.remove(myfood)
                menu2.add(myfood)
        else:
            print('가지고 있는 음식이 아닙니다. 교환할 수 없습니다.')