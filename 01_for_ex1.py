# list에 저장된 데이터를 하나씩 꺼내서 n에 저장 -> 반복
lst = [3,5,4,7,1]
for n in lst :
    print(n, end='\t')
print('\n-----------------')

# set에 저장된 데이터를 하나씩 꺼내서 n에 저장 -> 반복
s = {1,1,3,2,5}
for n in s :
    print(n, end='\t')
print('\n-----------------')

# 문자열을 한 글자씩 꺼내서 반복
str = 'Hello World'
for n in str :
    print(n, end='\t')
print('\n-----------------')

# dictionary의 키값을 하나씩 꺼내서 반복
d = {'a':1, 'b':2, 'c':3}
for n in d :
    # print(n, end='\t')
    print(f'{n} - {d[n]}', end='\t')
print('\n-----------------')

# tuple
tu = (1,2,3,4,5)
for n in tu :
    print(n, end='\t')