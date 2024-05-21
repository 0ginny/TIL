
```python
def add(*args):
    for n in args :
        print(n)
```

*args 는 파라미터를 내가 원하는 만큼 받겠다는 의미야.

```python
def calculate(**kwargs):
    for (key, value) in kwargs.items():

calculate(add= 3, multyply = 5)
```

**kwargs 의 경우 key와 value를 동시에 입력받으며 dictionary 형태로 저장이 됨