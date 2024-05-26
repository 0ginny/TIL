api키나 주소나 비밀번호 같은 것은 코드로 공개되면 안되는 것들이야.

그래서 숨길 때, env 안에 넣어놔

### 방법

terminal 에서 export [변수명] = [숨길 변수값]

그러면 env에 저장이 됨. 따라서 코드가 없어도 쓸 수 있음.

사용할 때는 [로컬 변수명] = os.environ.get("[저장했던 변수명]")

특히 pythonanywher 같은 사이트를 쓸 때, 시작할 때 변수를 지정해주고, 코드에선 제외하고 쓰면 돼

#### pythonanywher 에선

run 뒤에 terminal로 하면 돼. 

export ~~~; export ~~~; python3 main.py

이렇게 하면 작동 돼 