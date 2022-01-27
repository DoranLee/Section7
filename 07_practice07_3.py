# 보관할 과일의 갯수를 입력받고, 해당 갯수만큼의 과일을 입력받아 출력하시오.
# sol1
lst = []
no = int(input('몇 개의 과일을 보관할까요? > '))
for i in range(1, no+1):
    lst.append(input(f'{i}번째 과일을 입력하세요 > '))

print('입력받은 과일들은 {}입니다.'.format(lst))

# sol2
lst2 = []
no2 = int(input('몇 개의 과일을 보관할까요? > '))
while no2 != len(lst2):
    lst2.append(input(f'{len(lst2+1)}번째 과일을 입력하세요'))
print('입력받은 과일들은 {}입니다.'.format(lst2))

# sol3 (my sol)
lst1=[]
x=1
while x <= no :
    lst1.append(input(f'{x}번째 과일 입력'))
    x+=1
print(lst1)