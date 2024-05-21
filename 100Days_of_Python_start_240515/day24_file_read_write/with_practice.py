# file = open('my_file.txt')
# content = file.read()
# print(content)
# # 만약 계속 열고 있으면 컴퓨터의 리소스(메모리)가 할당되고 있는 거야.
# file.close()

# with를 써도 좋아. with 밖에선 할당이 끝나는 거야.
# with open('my_file.txt') as file:
#     content = file.read()
#     print(content)
# 이후 아래처럼 참조 불가.
# print(file.read())

# open mode / r : read / w : write / a : add
with open('my_file.txt', mode= 'a') as file:
    file.write("\nNew Text")