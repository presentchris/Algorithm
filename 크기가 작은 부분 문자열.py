# 내 풀이1
def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer

# 내 풀이2
def solution(t, p):
    return sum(1 for i in range(len(t) - len(p)+1) if int(t[i:i+len(p)]) <= int(p))

# 다른 사람의 풀이1
def solution(t, p):
    answer = 0
    n = len(p)
    li = []

    for i in range(0, len(t)-n+1):
        li.append(t[i:i+n])

    for s in li:
        if int(s) <= int(p):
            answer += 1

    return answer


# 다른 사람의 풀이2
def solution(t, p):

    try:

        if len(p)>=1 and len(p)<=18:

            if len(p)<=len(t) and len(t)<=10000:


                num_t = int(t)
                num_p = int(p)

                numlist = []

                for i in range(0, len(t)-(len(p)-1)):

                    numlist.append(t[i:i+len(p)])

                count = 0
                for num in numlist:
                    num = int(num)
                    if num <= num_p:
                        count += 1

                answer = count

    except Exception as e:
        answer = "Error"

    return answer
