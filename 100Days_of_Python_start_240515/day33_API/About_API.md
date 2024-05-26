API 는 인터페이스?

외부 시스템과 내 시스템을 연결하는 것.

마치 메뉴판 같은 거야.

외부 시스템이 메뉴판을 공개하면,

내가 그 메뉴판에서 필요한 것들을 요청하지 그러면 그 요청한 걸 받는 거고

메뉴에 없는 걸 요청하면 받을 수 없는 거고

## 개념

### END POINT

api의 주소? 정도로 생각하면 될 거 같아.

데이터를 찾을 수 있는 위치야.

### API Request

마치 내가 금고에 돈을 빼가려고 요청하는 것과 같아.

근데 마구잡이로 빼갈 수 없으니까. 요청을 하는데 안내처 역할이 api 인 거지

우리가 request를 하면 api를 통해 respond가 오는 거지

*** 보통 JSON 형태로 많이 관리돼.

### API response code

1xx : hold on (wait)

2xx : Here you ho (success)

3xx : go away (fail)

4xx : you screwed up (wrong)

5xx : i screwed up (sever wrong)