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
      - [ubuntu 설치](about_ubuntu.md)
    - 원하는 버전 클릭 -> installation 클릭
      - Debian packages 클릭
      - 설명해주는 스텝을 따라가

### ROS2 SETUP

- terminal : gedit ~/.bashrc
- 맨 밑에 작성 : source /opt/ros/{내가다운받은 ROS}}/setup.bash
  - ros 명 모르겠으면 cd /opt/ros/ 로 들어가서 확인해.

### ros2 실행 확인

- test용 예제
  - 터미널 : ro2 run demo_nodes_cpp talker
    - 신호 생성 코드
  - 터미널 : ros2 run demo_nodes_cpp listener
    - 신호 수신 코드

### 본격적인 ros2 시작

#### colcon install

- 자동 완성을 도와주는 툴이래

- sudo install python3-colcon-common-extensions
- gedit ~/.bashrc
  - source /urc/share/colcon_argcomplet/hook/cocln-argcomplete.bash

#### Create Workspace
