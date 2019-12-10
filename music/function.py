#----------------------------------#
# 반드시 home dir에서 실행시키시오
# 또는 file open의 dir을 변경하시오
#----------------------------------#


# 문제 & 답을 하는 함수 #
def q(f):
    i = 0
    while True:
        # line을 하나씩 읽습니다 #
        line = f.readline()
        # 문제 line #
        if i % 2 == 0:
            print(line, end='')

        # 답을 하는 line #
        elif i % 2 == 1:
            print("답 : ", end='')
            if input() == '0':
                break
            print("답 : " + line, end='')

        # 끝나면 break #
        if not line:
            break
        i += 1


print("1. music")
print("2. med")
print("3. renbar")
print("4. go")
print("5. nang")
print("6. train")

a = int(input())
if a == 1:
    f = open("1.music.txt", 'r', encoding='UTF8')
elif a == 2:
    f = open("2.med.txt", 'r', encoding='UTF8')
elif a == 3:
    f = open("3.renbar.txt", 'r', encoding='UTF8')
elif a == 4:
    f = open("4.go.txt", 'r', encoding='UTF8')
elif a == 5:
    f = open("5.nang.txt", 'r', encoding='UTF8')
elif a == 6:
    f = open("train.txt", 'r', encoding='UTF8')
q(f)
# close #
f.close()
