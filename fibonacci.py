def fibonacci(n):
    if n < 2:
        return(n)
    else:
        return(fibonacci(n-2)+fibonacci(n-1))

n = int(input('¬вед≥ть число: '))
print(n,' число посл≥довност≥: ',fibonacci(n))