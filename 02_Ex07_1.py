# is~함수 : ~인지 check

pwd = input('비밀번호를 입력하세요 > ')
ch_count = 0
num_count = 0

sp_count = 0
sp_str = '~!@#$%^&*()-+[]{}/;'

for ch in pwd :
    if ch.isalpha() :  #isalpha : 알파벳이면 True
        ch_count += 1
    elif ch.isnumeric() :  #isnumeric : 숫자면 True
        num_count += 1
    elif ch in sp_str :
        sp_count += 1

if ch_count > 0 and num_count > 0 and sp_count >0 :
    print('가능한 비밀번호입니다.')
else :
    print('불가능한 비밀번호입니다.')