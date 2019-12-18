def n(f):
    while True:
        line = f.readline()
        print(line.split(' ')[0])
        print("-> ",end='')
        if input()=='0':
            break
        print("-> " +line,end='')

        if not line:
            break

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

f = open("train.txt", "r", encoding='UTF8')
q(f)
f.close()