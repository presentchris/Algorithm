#내 풀이1
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            return answer

'''내 풀이2_for i in range(len())을 쓰는 이유는 인덱스로도 접근하기 위함이다. 
그리고 next를 빼고 []로 묶으면 큰 n보다 큰 k값들이 리스트에 차례로 저장되기 때문에 첫번째 요소를 뽑기 위해 next를 쓴다.
k<n을 하면 n보다 작은 값들만 저장되기 때문에 원하는 결과값이 나오지 않는다. 그러므로 k>n을 이용해야 한다.'''
def solution(num, n):
    return next(k for k in (sum(num[:i+1]) for i in range(len(num))) if k > n)

#내 풀이3
solution = lambda num, n: next(k for k in (sum(num[:i+1]) for i in range(len(num))) if k>n)

#다른 사람의 풀이1
def solution(numbers, n):
    answer = 0
    i=0
    while answer<=n:
        answer+=numbers[i]
        i+=1
    return answer

#다른 사람의 풀이2
def solution(numbers, n):
    sum = 0
    for elem in numbers:
        if sum > n:
            return sum
        else:
            sum += elem
    return sum

#다른 사람의 풀이3
def solution(numbers, n):
    answer, i = 0, 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer