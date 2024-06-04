# CSS (cascading style sheet)

html 과 xml 같은 언어는 구조가 복잡해.

그래서 스타일을 넣기에 코드가 보기 어려울 수 있어.

그래서 스타일만 따로 저장하는 css 를 만들어서 관리해.

---

## 작성 방식

요소 { 속성 : 바꿀값; }

## html에 넣는 법

head 에서

```html

<link rel="stylesheet" href="styles.css">
```

이렇게 지정해 주면 됨

## 개별 지정하는 법

- class
    - css 에서 .클래스명 으로 지정
    - 여러 요소에 하나의 클래스명을 사용해도 괜찮음.
    - 그래서 동시에 여러 클래스를 한 요소에 적용할 수도 있음.

```html
<p class="circular huge" </p> <!--이렇게 하면 circular 클래스와 huge 클래스 속성이 모두 적용됨-->
```

- id
    - css 에서 #아이디명 으로 지정
    - 단 요소에 단 하나의 id만 사용 가능
    - 한 요소에 둘 이상의 아이디를 적용할 수 없음

- active
    - 속성에 : action명 으로 적용시킬 수 있음.

```css
img:hover { background-color : gold} / 이렇게 하면 이미지에 마우스를 올리면 배경이 금색이 됨/
```