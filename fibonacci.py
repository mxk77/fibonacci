def fibonacci(n):
    if n < 2:
        return(n)
    else:
        return(fibonacci(n-2)+fibonacci(n-1))

n = int(input('������ �����: '))
print(n,' ����� �����������: ',fibonacci(n))