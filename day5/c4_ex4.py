for num1 in range(9):
    if (num1+1)%2==0:
        continue
    for num2 in range(9):
        if (num1+1)*(num2+1)>50:
            break
        calc=(num1+1)*(num2+1)
        print(f'{calc},',end='')
    print('')
