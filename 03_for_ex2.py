# (1) range(n) : 0 ~ n-1 숫자를 하나씩 뽑아냄
for i in range(5) :
    print(i, end=',')
print('\n------------------')

# (2) range(n,m) : n ~ m-1 숫자를 하나씩 뽑아냄
for i in range(1,10) :
    print(i, end=',')
print('\n------------------')

# (3) range(n,m,x) : n ~ m-1 숫자를 x간격으로 뽑아냄
for i in range(1,10,2) :
    print(i, end=',')
print('\n------------------')