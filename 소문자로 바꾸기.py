#내 풀이1
def solution(myString):
    return myString.lower()

#내 풀이2
solution = lambda myString : myString.lower()

#다른 사람의 풀이1
def solution(myString):
    answer = ''
    for i in myString:
        answer+=i.lower()
    return answer

#다른 사람의 풀이2
def solution(myString):
    answer = ""
    for i in myString:
        if ord(i) < 95:
            i = ord(i) + 32
            answer += str(chr(i))
        else:
            answer += i

    return answer