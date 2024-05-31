*** 흘러가는 개발자 이야기 ***

[교수님 유튜브](https://www.youtube.com/@waynehwang/playlists)

개발은 크게 embeded, standard, enterprise

최근 10년간의 sw 트렌드,가상화

클라우드 aws 엄청 싸진 않아. 오히려 돈을 더 내야할 수 있어.

그래서 대용량으로 사서 판매하는 서비스도 있어.

---

일단 이렇게 개발 분야도 정하고

domain도 정해야해. (제조, 국방 등)

이런 것들을 정해야. 내 적성에 뭐가 맞는지 알 수 있어.

---

요즘 chat gpt 도 있어서 단순 반복이 중요한 게 아니라 여러가지를 알고 잘 조합하는 능력이 중요해.

우리나라는 FE > BE > DB > SNL/TL 이런 수준으로 힘들어

왜냐하면 고객과 가까워지니까 맞추기가 너무 어려워.

---
요즘은 자격증은 없어도, 조그만 프로젝트라도 실제로 자기가 이루어 낸 사람이 좀 더 각광받아.

그래서 github나 aws 사이트를 한 번 화도 좋아.

그리고 node modules 는 없애도 좋아. package.json 만 있으면 알아서 다운로드 받아.

---
git 을 왜 쓰는가?

팀프로젝트 할 때 형상 관리 하려고

---

FE 와 BE 의 ip 가 같아야해.

같지 않으면 방어하는 apt 이 cors 야. (npm install cors)

---

맨처음 서버에 적용할 때,

port 개방 신청서를 작성해. 그런 것들 오늘 해보는 거야.

---

코딩 테스트 사실 문해력을 판단하는 거야.

문해력이 좋아야 새로운 프레임워크, 새로운 언어에 적응할 수 있어.

그래서 그렇게 새로운 언어에 적응 할 수 있는 사람을 찾아.

---

조금 코딩을 할 줄 안다면

design pattern 을 배우면
좋겠다. [디자인 패턴들 참조](https://m.hanbit.co.kr/channel/category/category_view.html?cms_code=CMS8616098823)

그것이 완료되었다면 architecture pattern 을 공부해라.

---

FE 개발자라면 [POSTMAN](https://hyunki99.tistory.com/93)
을 사용해야할 수도 있어.

## AWS 대시보드

- 인스턴스 :
    - 가상환경
- 로드밸런서
    - 카푸카 같은 것 (?)
- 키 페어 :
    - 로그인 할 때 인증서
- 볼륨 :
    - 하드디스크 같은 것.

## 리눅스 운영체제

쿠버네티스가 트렌드야.

web으로 하면 과금이 되니 virtual box 로 내 pc에 적용해도 좋아.

### 이정도만 알자

내가 편집을 할 수 있는지 확인.

### 명령어

- 맨 앞 d : directory , - : file, l : link
- _________ : 3개씩 owner 가 할 수 있는 일, group 이 할 수 있는 일, other 가 할 수 있는 일
- rwx : 파일의 oner가 할수 있는 일, read, write, excute(실행)
    - 2진수로 표현
        - ex) 400 : 읽을수만 있음. / 421 : 읽고 쓰고 실행 가능
- 파일의 주인 이름
- 파일 소유 그룹명

- chmod : 권한 부여
    - ex) ehmod g-w aaa : 그룹의 쓰기 권한 제거 => but 문자가 아닌 숫자로 들어가
    - ex) chmod 530 aaa

- ls : list 목록 출력
    - ls -al : 숨김까지 다 보여줘. === ll (in ubuntu)
- clear : 화면 클리어
- pwd : print walking directory
    - 내 위치가 안나오기 때문에 이렇게 directory를 확인해줘야해.
- cd : change directory
    - cd (이동 위치)
    - cd .. : 윗 directory
    - cd ~ : home 으로 이동.
- cp (복사할 파일 경로) (복사 위치)
- curl (url) : 해당 url 접속 요청
- wget (url) : 해당 url 다운로드

### modules

- express
  - express 방식으로 서버를 열 거야.
- cors
  - crossover(?) 문제를 해결할 거야. 
- pm2 :
    - app.js 를 실행하고 오류시 강제로 실행해줘.
    - 항시적으로 서버를 켜놓기 위해
    - pm2 start (실행.js)
    - pm2 stop (실행.js)
## aws instance

- 껐다 키면 ip가 바뀜. 알아둬.
-

## 실행에 대해서

1. aws instance 생성
2. putty 로 터미널 접속
    - [putty 란?](https://dololak.tistory.com/24)
    - 정보는 instance 속성, 보안(security)에서 확인.
    - 만약 putty로 접속이 안된다면?
        - osi 7 layer, [참조](https://velog.io/@hkh9601/OSI-7%EA%B3%84%EC%B8%B5-%ED%95%B5%EC%8B%AC-%EC%A0%95%EB%A6%AC)
            1. Application Layer : chorme, putty etc.
            2. Pressentation Layer : jpeg mpeg html css
            3. Session L : SSL/TLS (기밀성)
            4. Transport L : port (*L4) ⭐
            5. Network L
            6. Datalink L : ip (*L2)
            7. Physical L
        - cmd 로 ping ip 연결 L2 확인
            - 안되면
                - cmd 로 telnet ip port 연결
                    - window 에서는 "윈도우 기능 켜기/끄기"에서 텔넷을 체크해야해.
                - 이게 되는 거면 port까지는 연결 되어 있다. L4 까지는 연결이 된다는 의미.
    - 해쉬 경고가 들어와.
        - 조금이라도 서버가 달라지면 해쉬값이 달라져서 경고창이 뜰거야. 근데 이게 무슨 의미가 있는 거야?

## port 에 대해서

서버에 관문 같은 거야. 각각 관문의 용도가 다른 거지

한 서버에도 여러 관문이 있는데 용도에 따라 port를 다르게 쓰는 거지.

항상 network 통신은 port 를 통해 나가고 port 를 통해 들어와.

- 80 port : HTTP port

- 443 port : 인증서 적용

## node

Framework의 한 종류야

### 명령어

- sudo passwd root :
    - sudo : super user do (admin)
    - passwd : 패스워드 설정
    - root : root라는 관리자.
    - root의 비밀번호를 설정하겠다.
- su - (root)
    - switch user
- apt-get update
    - 그냥 apt을 업데이트 하겠다.
- apt install tree
    - tree 란 app을 설치하겠다.

#### node 와 spring

- spring 은 자바로 사용됨
- node는 자바스크립트
    - pip 대신 npm
- start-up에선 node를 많이 써, 인건비가 부족하니, FE와 BE와

##### react 와 vue.js

-[참조](https://80000coding.oopy.io/f27f6183-0523-43e1-ab90-8f8175bd4a88)

# 용어

-SSH : Secure SHell (22)
-해쉬 : 단방향 암호화

- FTP : File Transfer Protocol
