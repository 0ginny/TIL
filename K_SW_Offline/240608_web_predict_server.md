처음 

---

리눅스 node 패키지

- express
  - web 환경을 구성하기 위한 framework
- pm2 (process manager)
  - 내가 실행할 프로세스 관리
- cors 
  - 웹 통신(cross over) 문제 방지
- net-tools
  - 통신 확인 

---

라우터 (실습의 app.js)

html 같은 걸 연결해주는 것.

----

vi editor

- 검색 
  - /(찾을내용)
  - enter 후 n 으로 원하는 내용 찾고 enter 후 작업
  
---
리눅스 명령어

- ps -ef |grep (찾고 싶은 것)
  - ps -ef |grep node : node 라는 프로세스를 찾아볼래 (실행 프로그램 찾아볼때)
- kill (프로세스 넘버) : 해당 프로세스를 죽이겠다.
  - kill -9 : 강제로 죽이겠다.
- nohup (프로세스) : 끊기지 않고 프로세스 실행
  - & : 백그라운드에서 실행
  + ex) nohup python app.py & : app.py 를 백그라운드에서 python으로 실행하겠다.

---

노드 패키지ㅣ