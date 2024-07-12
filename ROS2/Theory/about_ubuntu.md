### ubuntu 설치
  - 초기 시작
    - sudo apt update
    - sudo apt upgrade
    - sudo apt autoremove
  - 이후 터미널 실행할 때마다
    - sudo apt update

### 처음 실행시 에러에 대해서

- [terminal이 안열릴 때](https://code-lab1.tistory.com/309)
  - korea로 바꿔도 되긴 했음
- [username is not in the sudoers file.](https://veganwithbacon.tistory.com/496)

#### virtualBox 화면 스케일링 수정

- sudo apt install builid-essential gcc make perl dkms
- 장치 -> 게스트 확장 CD 삽입
- CD 클릭 -> 우클릭 -> open in terminal
- sudo ./VBoxLinuxAdditions.run
- 가상컴퓨터 끄고 다시 시작
- 만약 안되면 3번 부터 다시.

### 유용한 도구 모음

#### terminater

터미널을 분할해서 여러 터미널을 한번에 볼 수 있어.

sudo apt install terminator

[단축키](https://shanepark.tistory.com/313)

#### pip

sudo apt install python3-pip

#### gedit

터미널에서 문서를 확인할 수 있도록 하는 명령어

