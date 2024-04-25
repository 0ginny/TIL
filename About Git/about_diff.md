# what is diff?

어떤 것들이 변했는지 비교해보고 싶을 때 사용해.

head나 log에 영향없이 그저 정보를 주는 명령어

근데 처음하면 매우 복잡할 수 있어.

q 를 이용해 빠져나올 수 있어.

git add 하기 전에 무엇이 바꼈는지 확인하는 명령어야.

## what's the simbols, how to read?

- 맨 위에는 다른 파일 명.
- 중요하지 않음. 그냥 메타데이터 ( 해시데이터)
- ---, +++ 구분 인덱싱?
- 내용 : 
  - context
  - 변화된 내용
  - @ 청크 헤더,  @@ -3,4 +3,5 @@
    - 숫자 의미 : 코드 줄 위치, 몇줄을 가져왔는지

## various usage of git diff / commands
```python
# 스테이지(add) 되지 않은 상태 확인하기
# 기존 파일에서 바뀐 부분이 있을 때, add 하기 전에 확인
git diff 
# 워킹 디렉토리와 스테이지 사이 변화 비교
# 마지막 commit과 어디가 다른지
# add 후에도 확인 가능 (commit 전까지 가능)
# 이건 파일을 추가하거나 해도 확인 가능
git diff HEAD
```