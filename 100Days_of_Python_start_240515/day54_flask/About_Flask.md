Full stack = front end + back end

back-end란?

client + server +database

Flask 란?

python 기반 웹 개발 framework

Framework란?

라이브러리와 비슷하지만, 다른 점은 코드를 실행할 때, framework에서 설계된 대로 코드를 호출해야해.

### FE 렌더링

html은 templates 폴더에 넣어야 하고

css, src 파일을 static 폴더에 넣어야 인식이 가능해.

당연히 이런 경우 html의 경로도 수정해 줘야겠지?

#### 크롬에서 static 파일들

크롬에서는 캐시를 저장해 놓기 때문에 

페이지를 띄우고 static 폴더 안에 있는 소스를 변경하고 새로고침을 해도 그대로야

정적 파일은 변경될 일이 적어서, 캐시로 관리해

이걸 변경하고 싶으면 shift+리로드 버튼을 클릭하면 hard reload가 되서 정적 파일도 다시 받아.

