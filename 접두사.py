# 내 풀이1
def solution(my_string, is_prefix):
    return int(is_prefix==my_string[:len(is_prefix)])

# 내 풀이2
solution = lambda mystring, prefix: int(prefix==mystring[:len(prefix)])

# 다른 사람의 풀이1
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

# 다른 사람의 풀이2
def solution(my_string, is_prefix):
    return 1 if my_string.find(is_prefix) == 0 else 0

# 다른 사람의 풀이3
def solution(my_string, is_prefix):
    my_string = my_string.replace(is_prefix,"$")
    return (my_string[0] == "$") * 1
