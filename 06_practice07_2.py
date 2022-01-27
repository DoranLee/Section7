# 임의의 양수를 입력받아 1부터 해당 수까지의 합을 구하시오.
no = int(input('임의의 양수를 입력 > '))
total = 0

for i in range(1, no + 1) :
    total += i

print(f'1부터 {no}사이 모든 정수의 합계는 {total}입니다.')