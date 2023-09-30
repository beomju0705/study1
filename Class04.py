# a = str(input("이름을 입력해주세요 :"))
# b = int(input("나이를 입력해주세요 :"))
# c = int(input("연락처를 입력해주세요 :"))
# info = dict(name = a, age = b, number = c)
# print(info)

lst = []
while True:
    a = str(input("이름을 입력해주세요 :"))
    b = int(input("나이를 입력해주세요 :"))
    c = int(input("연락처를 입력해주세요 :"))
    if b == 0:
        break


    info = dict(name=a, age=b, number=c)
    lst.append(info)

print(lst)

