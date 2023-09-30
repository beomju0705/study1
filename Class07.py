a = [i for i in range(10)]
#a = [i] a에 [i]를 넣겠다.
#i가 뭔데?
#for i in range(10) : 0부터 ~ 9까지
#a에 = [0....9]

print(a)

a = [i for i in range(10) if i%2 == 0]
#a = [i] a에 [i]를 넣겠다.
#i가 뭔데?
#for i in range(10) i는 0~9야
#if i%2 == 0 i는 2로 나눈 나머지가 0이야
#a = [0,2,4,6,8]

print(a)

a = [i*j for i in range(2,10) for j in range(1,10)]
#a = [i*j] a에 i*j를 넣겠다.
#i가 뭔데?
#for i in range(2,10) i는 2~9까지야
#j가 뭔데?
#for j in range(1,10) j는 1~9까지야

print(a)

a = [i * 0 for i in range(10)]

print(a)


word = ["school", "game", "piano", "science", "hotel", "mountain"]
a = [i for i in word if len(i) >= 6]
a = [word[i] for i in range(len(word)) if len(word[i]) >= 6]

a = [len(i) for i in word]
print(a)