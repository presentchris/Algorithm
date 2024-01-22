# 첫 번째 시도_n은 정수이고 문자열이 아니라서 for문을 사용했을 때 에러가 남, range를 써야 함. sum(), range()를 고려해 볼 수 있었음, GPT를 통해 수학적 공식을 이용하여 푸는 방법도 있었으나 실행해보니 결과가 다름
# def solution(n):
#     if n%2!=0:
#         answer = 0
#         for i in n:
#             answer += i%2!=0
#         else:
#             answer += i%2==0
#     return answer

# 내 풀이1_return 등 들여쓰기 순서 중요, answer 초기화 위치, for문 활용
def solution(n):
    answer = 0
    if n % 2 != 0:
        for i in range(1, n + 1, 2):
            answer += i
    else:
        for i in range(2, n + 1, 2):
            answer += i**2
    return answer
  
# 두 번째 시도_pow() 함수에 range 객체를 전달할 수 없기 때문에 에러가 발생한 코드, pow() 함수는 숫자(정수 또는 실수)를 인자로 받아야 하는데, 
# 여기서는 range 객체를 사용하고 있기 때문에 pow() 함수 대신 ** 연산자를 사용하거나 리스트 컴프리헨션과 sum() 함수를 활용할 수 있음.
# def solution(n):
#     answer = 0
#     if n % 2 != 0:
#         answer = sum(range(1, n+1, 2))
#     else:
#         answer = sum(pow(range(2, n+1, 2),2))
#     return answer

# 내 풀이2_GPT 참고
def solution(n):
    if n % 2 != 0:
        answer = sum(range(1, n+1, 2))
    else:
        answer = sum(i**2 for i in range(2, n+1, 2))
    return answer

# 다른 사람의 풀이1_제곱의 합 공식을 사용하면 for문을 안 써도 된다고 하는데 거기까진 모르겠다. 엄청난 사고력의 차이와 창의성이 느껴진다.
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

# 다른 사람의 풀이2_n % 2는 n이 홀수일 때 True가 되므로, 이 경우 홀수의 합을 계산하고 n이 짝수라면 False가 되어 else 블록이 실행. else가 if문밖에 있는 return.
def solution(n):
    if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])


