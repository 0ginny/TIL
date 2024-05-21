
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# 4. 1~3의 과정을 invited name for 문 안에서 진행해.
with open('./Input/Names/invited_names.txt', mode='r') as names:
    for name in names.readlines():
        name = name.rstrip('\n')

        # 1. 형식 데이터를 readline으로 불러와
        with open('./Input/Letters/starting_letter.txt', mode='r') as format:
            lines = format.readlines()
            # print(lines)

            # 2. 그 중 첫먼째 줄의 [name]을 다른 이름으로 바꿔.
            # name = 'YongJin'
            print(lines[0])
            lines[0] = lines[0].replace('[name]', name)

            # 3. 바뀐 내용을 기반으로 output 폴더에 이름을 저장해
            with open(f'./Output/ReadyToSend/{name}.txt', mode='w') as mail:
                for line in lines:
                    mail.write(line)
