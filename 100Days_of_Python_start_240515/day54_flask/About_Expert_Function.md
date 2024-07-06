
### Argument로 function을 쓸 때

```python
def add(n1,n2):
    return n1 + n2

def calculate(func,n1,n2)
    return    func(n1,n2)

calculate(add,2,3) # 5
```

### nested function (함수 안에 함수)

```python
def outter():
    print('out')
    
    def inner():
        print('in')
# 여기에 호출하면 안됨
    inner()

outter() # 출력 'out\nin'
```

```python
def outter():
    print('out')
    
    def inner():
        print('in')
# 여기에 호출하면 안됨
    return inner

inner_func = outter() # 출력 : out
inner_func() # 출력 : in
```

### Decorator

클래스나 모듈에 있는 함수에 기능을 추가하고 싶을 때

```python
import time
def delay_decorator(func):
    def inner():
        # 함수 실행 전 실행
        time.sleep(5)
        # 실행 함수
        func()
        # 함수 실행 후 실행할 것 
    return inner

@delay_decorator
def say_hello():
    print('Hello')

# @는 아래와 같은 동작
# decorator_func = delay_decorator(say_hello)
# decorator_func()
     
say_hello() # 5초뒤에 Hello 출력
```