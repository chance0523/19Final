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
            if(input()=='0'): break
            print("답 : " + line, end='')

        # 끝나면 break #
        if not line:
            break
        i += 1


# 여기에 text file의 이름을 적으시오 #
# "file_name/file_name/file_name.txt" #
f = open("train.txt", 'r', encoding='UTF8')
q(f)
# close #
f.close()
