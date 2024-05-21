file = open('my_file.txt')
content = file.read()
print(content)
# 만약 계속 열고 있으면 컴퓨터의 리소스(메모리)가 할당되고 있는 거야.
file.close()