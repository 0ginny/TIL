'''
시작 :  11 :41

0. 문제 이해
벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호의 칸이 있는 위치로 이동
 로봇은 컨베이어 벨트 위에서 스스로 이동할 수 있다
  1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"


순서 중요해

1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.


그러니까 밸트도 회전하고 로봇도 이동하는 거야.

그래서 내구도가 많으면 로봇은 2번 이동 할 수 있어.

단계는 밸트가 회전하는 단계를 의미해

1. 구현 방법

- 회전은 구현해야 할까?
    - 차라리 시작 위치와 종료 위치를 변경시키는 건 어떨까? -1 씩 하는 거지
- 로봇의 움직임은 어떻게 구현하지?
    - 시간 복잡도가 많으니, for 문 탐색, temp에 append 하면 될듯 으로 하면 될까?

            - 종료 위치면 없애기
            - 다음 칸 움직일 수 있으면 움직이기
                - 종료 위치면 없애기
                - 아니면 temp append
            - 아니면 temp append
        - robot = temp
        - 3단계에서 시작 위치를 기준으로 robot append
- 이후 컨베이어 내구도 0 chk - 종료 판단

'''

import sys
input = sys.stdin.readline

N,K = map(int,input().split())

belt = list(map(int,input().split()))


S = 0
E = N -1
robot = []
cnt = 0
while 1:

    cnt += 1

    # 1. 밸트의 회전
    if S > 0 :
        S -= 1
    else :
        S = 2 * N -1

    if E > 0 :
        E -= 1
    else :
        E = 2 * N -1

    # 2. 로봇의 움직임 (먼저 들어온 것부터 움직이기)
    temp = []
    for r in robot :
        # 2_1 종료 위치면 없애기
        if r == E :
            pass
        else :
            # 2_1 다음 단계가 움직일 수 있으면 움직이기
            if r == 2*N -1 :
                t = 0
            else : t = r + 1

            if belt[t] > 0 and t not in temp:
                belt[t] -= 1
                # 2_1_1 종료 위치면 종료
                if t == E :
                    pass
                else :
                    temp.append(t)
            else : # 못 움직이면 그대로
                temp.append(r)
    robot = temp

    # 3. start 가능하면 로봇 올리기
    if belt[S] > 0 :
        belt[S] -= 1
        robot.append(S)

    # 4. 종료 확인
    if belt.count(0) >= K :
        break

print(cnt)



