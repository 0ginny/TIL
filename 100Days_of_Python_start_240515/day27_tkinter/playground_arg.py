def add(*num):
    total = 0
    for n in num:
        total += n
    return total
print(add(1,2,34,5,3,2))

def calculate(**kwargs):
    for (key, value) in kwargs.items():
        print(key, value)

calculate(add= 3, multyply = 5)

