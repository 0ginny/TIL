#### 들어가기에 앞서 자주하는 실수
- mkdir 으로 폴더를 만들었다면 
  - 폴더에 git이 있는지 확인하기 위해 git init 를 해주자.

## What is commit?
- 커밋 == 체크포인트
- not save
  - save를 한 뒤에 commit을 하는 거야.
  - 여러 변경사항을 저장하는 것.
- 사용법
  - 여러 에디터로 할 수 있긴 함
  - git commit -m "내가 원하는 커밋명"

## what is git add
- 변경사항을 스테이지에 올리는 작업 (commit 전 작업)
- 만약 하지 않고 git status를 하면
  - untracked files 에러가 떠.
- git 에는 3가지 영역이 있어 (working dir, staging area, repository)
  - working dir : 실제 작업하는 공간
  - staging area :commit 전 변경사항을 올리는 곳.
  - repository : 저장소
- ((아마 변경사항을 그룹화해서 등록하기 위해 이렇게 하나봐.))
- 사용법
  - git add file1 file2 


## git log
- git 기록을 보는 곳? commit 기록?
- 