#내 풀이1
def solution(num_list):
    if int(num_list[-1]) > int(num_list[-2]):
        num_list.append(int(num_list[-1]) - int(num_list[-2]))
    else:
        num_list.append(int(num_list[-1])*2)
    return num_list

#다른 사람의 풀이1
def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l

#다른 사람의 풀이2
def solution(num_list):
    return num_list + [num_list[-1]-num_list[-2]] if num_list[-1] > num_list[-2] else num_list + [num_list[-1]*2]

#다른 사람의 풀이3
def solution(num_list):
    if num_list[-1]>num_list[-2]: return num_list+[num_list[-1]-num_list[-2]]
    return num_list+[num_list[-1]*2]