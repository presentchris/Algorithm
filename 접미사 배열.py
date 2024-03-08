# 내 풀이1_처음에 for i in my_string으로 시도했다가 my_string[i:]를 사용한다는 사실을 알아 차리고 range(len(my_string))으로 바꿈
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
        answer.sort()
    return answer

'''내 풀이2_처음에 sorted(my_string[i:])를 해서 리스트컴프리헨션 안에 넣었다. 
하지만 원하는 결과는 my_string의 글자 하나하나인 i를 차례로 정렬하여 리스트로 나타내는 것이 아니라(결과가 ['e','s'~],['m','e','s'~]~ 와 같은 형식으로 나옴) 리스트 안의 결과 요소들을 정렬하는 것이기 때문에 리스트컴프리헨션 전체를 sorted로 감싸 정렬해야 한다.
그리고 sort()는 해당 리스트 자체를 정렬하고, 새로운 리스트를 반환하지 않고, None을 반환하는 메서드이고, sorted()함수는 어떤 반복 가능한 객체도 받아서 정렬된 새 리스트를 반환하기 때문에 여기서는 sorted를 써야 None이 나오지 않는다.''' 
solution = lambda my_string: sorted([my_string[i:] for i in range(len(my_string))])

# 다른 사람의 풀이1_answer.sort()가 다르다. 항상 들여쓰기에 주의해야 한다. my_string[-i:]처럼 표현하면 글자를 뒤에서부터 i번째 인덱스를 표현하게 된다. 하지만 문제에서 원하는 결과에는 차이가 없다.
def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    answer.sort()
    return answer

# 다른 사람의 풀이2_Python에서 ~는 비트 NOT 연산자. 비트 NOT 연산은 모든 비트를 반전시킴. 예를 들어, ~0은 -1이 됩니다. 정수 n에 대해 ~n은 -n-1과 같음.
def solution(my_string):
    return sorted(my_string[~i:] for i in range(len(my_string)))
