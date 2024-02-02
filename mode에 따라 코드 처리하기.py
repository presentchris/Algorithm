# 내 풀이1_mode==1, mode==0 으로 비교연산자를 사용하여 원하는 결과를 얻지 못하다가 할당연산자('=')를 통해 결과를 얻을 수 있었음
def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0:
            if code[i]!="1" and i%2==0:
                ret += code[i]
            elif code[i]=="1":
                mode = 1
        else:
            if code[i]!="1" and i%2==1:
                ret += code[i]
            elif code[i]=="1":
                mode = 0
    return "EMPTY" if ret=='' else ret

# 내 풀이2_int(not(mode))로만 써도 됨
def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if mode == 0 and code[i]!="1" and i%2==0:
            ret += code[i]
        elif code[i]=="1":
            mode = int(not bool(mode))
        elif mode == 1 and code[i]!="1" and i%2==1:
            ret += code[i]
    return "EMPTY" if ret=='' else ret

# 내 풀이3_리스트 초기화 및 append() 사용 후 join()
def solution(code):
    mode = 0
    ret = []
    for i in range(len(code)):
        if mode == 0 and code[i]!="1" and i%2==0:
            ret.append(code[i])
        elif code[i]=="1":
            mode = int(not bool(mode))
        elif mode == 1 and code[i]!="1" and i%2==1:
            ret.append(code[i])
    return "EMPTY" if ret=='' else ''.join(ret)

# 다른 사람의 풀이1
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"

'''다른 사람의 풀이2 _ '^=' 는 비트연산자 중에 xor을 뜻함. 두 비트가 서로 같으면 0 다르면 1. 따라서 mode가 0이면 결과는 1이되고, 1이면 같기 때문에 0. answer if answer else 'EMPTY'는 answer가 빈문자열이 아니면 answer를 리턴하고, 빈문자열이면 'EMPTY'를 리턴. if 뒤에 조건이 참이면 if 앞의 것을 반환하고, 거짓이면 else 뒤의 것을 반환.'''
def solution(code):
    answer = ''

    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode ^= 1
        else:
            if i % 2 == mode:
                answer += code[i]

    return answer if answer else 'EMPTY'
