# 1~99까지의 숫자로 369게임을 표기하시오. 3,6,9가 한 번 들어갈 때는 짝, 두 번 들어갈 때는 짝짝으로 표기하시오. 10의 단위로 줄바꿈하시오.
lst = []
for i in range(1,100):
    msg = ''
    if i // 10 > 0 and (i // 10 % 3 == 0 or i // 10 % 6 == 0 or i // 10 % 9 == 0) :
        msg = '짝'
    if i % 10 != 0 and (i % 10 % 3 == 0 or i % 10 % 6 == 0 or i % 10 % 9 == 0) :
        msg += '짝'
    if msg == '' :
        lst.append(i)
    else :
        lst.append(msg)

count = 1
for i in range(len(lst)):
    print(lst[i], end='\t\t')
    if count % 10 == 0 :
        print()
    count += 1
