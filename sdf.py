for i in range(1,100):
    if i // 10 > 0 and ('3' in str(i)[-2] or '6' in str(i)[-2] or '9' in str(i)[-2]):
        print('짝')

        if '3' in str(i)[-1] or '6' in str(i)[-1] or '9' in str(i)[-1] :
            print('짝짝')

    else :
        print(i)
