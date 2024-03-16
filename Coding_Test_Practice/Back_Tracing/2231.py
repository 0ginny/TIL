'''
1. 아이디어
- 생성자의 조건
  - 목표 자연수보다 작음
  - 자신 + 각 자리 숫자의 합(%10) = 목표 자연수
    - 각자리 숫자의 합 < 10 * 자리수(//10)
      - 아무리 최대에서도 60번만 반복하면 됨. 가능

논리
- 목표 자연수에서 1씩 빼가며 가능한 모든 경우의 수( 10* 자릿수 )를 고려
- 생성자 계산 함수 돌려서 목표값과 비교
- 맞으면 출력 전부 돌려도 맞지 않으면 0 출력
'''

t = int(input())

def tens(n):
  num = 0
  while(n<0)
    num += 1
    n = int(n/10)
  return num

def gen(n): # 생성 함수
  if n <10:
    return 2 * n
  else :
    total = n
    for _ in range(tens(n)+1):
      total += n % 10
      n //= 10
    return total

ans = 0
if t >= 10 : # 생성자 가능
  d = tens(t)
  repeat = 10*d -1
  print(repeat)

  for i in range(1,repeat):
    if t == gen(n-i):
      ans = n-i
      break
print(ans)
    