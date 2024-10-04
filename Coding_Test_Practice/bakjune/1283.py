'''
22:03

단어의 첫글자가 단축키 인지 - 즉 2단어이면 2번 탐색
이건 그냥 하면 되네
'''

import sys

input = sys.stdin.readline

# chk = [chr(n) for n in range(ord('a'),ord('z')+1)]
# print(chk)
chk = []

N = int(input())

words = []
indexs = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)
    l = [ w.lower() for w in word.split()]
    idx = -1
    chk2 = True
    # 첫 글자 확인
    for i, s in enumerate(l):
        if s[0] not in chk :
            chk.append(s[0])
            idx = (i,0)
            chk2 = False
            break
    if chk2 :
        chk3 = False
        for i, s in enumerate(l):
            for j, w in enumerate(s[1:]):
                if w not in chk:
                    chk.append(w)
                    idx = (i,j+1)
                    chk3 = True
                    break
            if chk3 :
                break
    indexs.append(idx)
#     print(chk)
# print(indexs)


ans = []
for c,word in enumerate(words):
    temp =''
    if indexs[c] != -1 :
        for i,wo in enumerate(word.split()):
            for j,w in enumerate(wo):
                if (i,j) == indexs[c] :
                    w = '[' +w +']'
                temp += w
            temp += ' '
    else : temp = word

    ans.append(temp)
for a in ans :
    print(a)