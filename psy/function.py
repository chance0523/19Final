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

def n(f):
    i=1
    while True:
        line = f.readline()
        if i%2==1:
            print(line,end='')
            i-=1
        elif i%2==0:
            print("답 : ",end='')
            if input()=='0':
                break
            print("답 : "+line,end='')
            i+=2

        if not line:
            break

print("1. bio")
print("2. sensation_and_perception")
print("3. learning")
print("4. memory")
print("5. emotion")
print("6. train")
print("7. new")

a = int(input())
if a == 1:
    f = open("1.bio.txt", 'r', encoding='UTF8')
elif a == 2:
    f = open("2.sensation_and_perception.txt", 'r', encoding='UTF8')
elif a == 3:
    f = open("3.learning.txt", 'r', encoding='UTF8')
elif a == 4:
    f = open("4.memory.txt", 'r', encoding='UTF8')
elif a == 5:
    f = open("5.emotion.txt", 'r', encoding='UTF8')
elif a == 6:
    f = open("train.txt", 'r', encoding='UTF8')
elif a == 7:
    f = open("7.new.txt", 'r', encoding='UTF8')
q(f)
#n(f)
# close #
f.close()

