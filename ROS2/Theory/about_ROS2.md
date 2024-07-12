ROS 는 robot operating system 이야 (미들웨어와 프레임워크의 중간정도?)

그래서 개발자들이 모든 로봇에 사용할 수있는 소프트웨어 표준을 만들고자 시작되었어.

### ros2 가 할 수 있는 것

- 작동을 세분화하고 서로 상호작용하도록 할 수 있어.
- 단순히 코드를 모두 짜는 것이 아니라 라이브러리를 다운 받아 기능을 사용할 수 있어.
- 개발 언어에 무관해, 통신을 돕는 시스템이기 때문에 언어가 다르더라도 상호작용이 가능해.


### ros2 설치

- 일단 배포 버전을 알아야해.
  - [버전 확인 사이트](https://docs.ros.org/en/rolling/Releases.html)
    - EOL 확인 (배포 종료일)
    - LTS 버전인지 확인 : 장기적 지원 여부, 얼마 주기로 업데이트 되는지
      - LTS 버전은 5년 기간동안 1년마다 업데이트 돼.
    - 그래서 최대한 최신버전을 사용하는 것이 좋아
      - 혹시 새로운 버전이 나왔다면, 내가 필요한 모든 기능이 포팅 되었는지 확인해 보긴 해야해
    - 어떤 os를 설치해야하는지 확인
      - ubuntu : 보통 학교에서 많이 사용, 셋업이나 도구에서 문제가 적어
        - [ubuntu cite](https://ubuntu.com/)
        - [virtualBox cite](https://www.virtualbox.org/)
        - virtualBox 를 통해 ubuntu.iso 파일로 가상환경 생성

- ubuntu 설치
  - 초기 시작
    - sudo apt update
    - sudo apt upgrade
    - sudo apt autoremove
  - 이후 터미널 실행할 때마다
    - sudo apt update

#### virtualBox 화면 스케일링 수정

- sudo apt install builid-essential gcc make perl dkms
- 장치 -> 게스트 확장 CD 삽입
- CD 클릭 -> 우클릭 -> open in terminal
- sudo ./VBoxLinuxAdditions.run
- 가상컴퓨터 끄고 다시 시작
- 만약 안되면 3번 부터 다시.