---

fastAPI vs. flask

fastAPI는 비동기 처리가 가능하지만, flask는 동기처리만 가능

---

get과 post 차이

get : url에서 입력

post : 데이터를 변수에 할당하고 입력시킬 수 있음.

---

머신러닝 웹 서비스

클라이언드 - 웹 서버 - 분석서버

이런식으로 통신해. 

웹 서버와 분석서버는 api를 통해 request 하는 거야. 

---

port 를 지정해서, 각각 기능들에 할당해. 

ex)192.168.110.11:9999/predict

/predict는 실행 기능 이름

---

[ngrok](https://ngrok.com/)

로컬 서버 공개 (로컬개발서버를 인터넷에 공개)

클라우드를 집에서 구축하는 느낌.

코랩은 클라우드여서 서버 주소가 보안되어있어.

그래서 해당 서버의 주소를 우회해서 공개하는 방식인거야.

---

ngrok 으로 서버를 개설했을 때,

도중에 colab 코드를 수정했을 경우,

업데이트가 안되는 경우가 있어.

그 경우, 해당 코드 전체를  다시 돌려주면 작동해.

---

[postman](https://web.postman.co/home)

가상으로 데이터는 던지는 

서버 테스트용.

---

jmeter

[사용법](https://effortguy.tistory.com/164)

서버 부하 테스트

---

웹 껍데기는 chatgpt로도 구현이 가능해.

