# Merge

병합은 브랜치를 병합하는 거야.

특정 커밋과 커밋을 병합하는 것이 아니야

항상 HEAD를 기준으로 병합해.

그래서 병합을 하기 전에 반드시 원하는 곳으로 switch한 후에 병합해야해.

## 병합 종류
- 연결된 브랜치에서 병합시에는 그저 헤드 포인터를 바꾸기만 하면 돼.
  - fast forward merge

- 만약 여러 브랜치로 나누고 작업이 되었을 경우. 
  - 병합 커밋  - 부모를 두개 가짐  

## 병합 충돌
만약 둘 이상의 사용자가 같은 파일을 수정했을 경우

git은 무엇을 남기고, 무엇을 버려야하는지 몰라. 그래서 사용자가 이것을 지정해 줘야해.

### 충돌 해소 과정
1. 충돌이 생기면 git이 알려줘.
2. 충돌이 발생한 부분은 표시가 있어.
   - HEAD ==== >>>>
3. 표시된 부분을 수정해
   - 충돌 표시 제거
   - 원하는 것들만 남기기
4. 그 후 새로 커밋


# 명령어

- git merge 병합할브랜치
  - 이전에 미리 기준이 될 브랜치로 이동해야해.