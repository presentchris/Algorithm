# 첫 번째로 시도해 본 코드
# str = input()
# for i in str:
#     if i.isupper():
#         print(i.lower(), end='')
#     else:
#         print(i.upper(), end='')

# 두 번째로 시도해 본 코드. 리스트를 사용하여 append 해 봄. result_list를 사용하여 초기화할 때 for문에 들어가 있는지, 밖에 있는지의 위치에 따라 다른 결과가 출력됨.
# str = input()
# for i in str:
#     result_list= []
#     result_list.append(i.lower() if i.isupper() else i.upper())
#     result = ''.join(result_list)
#     print(result, end='')

# 세 번째로 시도해 본 코드
# str = input()
# for i in str:
#     result = ""
#     result += i.lower() if i.isupper() else i.upper()
#     print(result, end='')

# 네 번째로 시도해 본 코드. 삼항 연산자를 사용함. 
str = input()
result = ''.join(i.lower() if i.isupper() else i.upper() for i in str)
print(result)

# 다섯 번째로 시도한 코드. 삼항 연산자를 사용하되, join을 빼면 출력은 되지만 리스트 형태로 출력됨. join을 넣어서 결과적으로 위와 같이 나옴.
# str = input()
# result = ''.join([i.lower() if i.isupper() else i.upper() for i in str])
# print(result)


# 다른 사람의 풀이1
# print(input().swapcase())

# 다른 사람의 풀이2
# print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
