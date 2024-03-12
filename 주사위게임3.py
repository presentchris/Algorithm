# gpt 도움 풀이
from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = Counter(dice)
    values = list(counts.values())
    keys = list(counts.keys())
    
    if len(counts) == 1:
        # 모든 주사위가 같은 숫자
        return 1111 * keys[0]
    elif 3 in values:
        # 세 주사위가 같은 숫자
        p = keys[values.index(3)]
        q = keys[values.index(1)]
        return (10 * p + q) ** 2
    elif 2 in values and len(values) == 2:
        # 두 쌍의 주사위가 같은 숫자
        p, q = keys
        return (p + q) * abs(p - q)
    elif 2 in values and len(values) == 3:
        # 두 주사위가 같은 숫자, 나머지 두 주사위 각각 다른 숫자
        p = keys[values.index(2)]
        q = keys[values.index(1)]
        r = keys[values.index(1, values.index(1)+1)]  # 두 번째로 등장하는 1의 인덱스
        return q * r
    else:
        # 모든 숫자가 다름
        return min(dice)

# gpt의 다른 풀이
from collections import Counter

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = Counter(dice)
    
    if len(counts) == 1:
        # 모든 주사위가 같은 숫자
        return 1111 * dice[0]
    elif 3 in counts.values():
        # 세 주사위가 같은 숫자
        for num, count in counts.items():
            if count == 3:
                p = num
            else:
                q = num
        return (10 * p + q) ** 2
    elif 2 in counts.values():
        nums = list(counts.keys())
        counts_vals = list(counts.values())
        if len(nums) == 2:
            # 두 쌍의 주사위가 같은 숫자
            return (nums[0] + nums[1]) * abs(nums[0] - nums[1])
        else:
            # 두 주사위가 같은 숫자, 나머지 두 주사위 각각 다른 숫자
            twice = [num for num, count in counts.items() if count == 2][0]
            ones = [num for num, count in counts.items() if count == 1]
            return ones[0] * ones[1]
    else:
        # 모든 숫자가 다름
        return min(dice)


# 다른 사람의 풀이1_지독한 문제인만큼 지독한 풀이..
def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=1111*a
    elif a==b==c:
        answer=(10*a+d)**2
    elif a==b==d:
        answer=(10*a+c)**2
    elif a==c==d: 
        answer=(10*a+b)**2
    elif b==c==d:
        answer=(10*d+a)**2
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b:
        answer=c*d
    elif a==c:
        answer=b*d
    elif a==d:
        answer=b*c
    elif b==c:
        answer=a*d
    elif b==d:
        answer=a*c
    elif c==d:
        answer=a*b
    else:
        answer=min(a,b,c,d)

    return answer


# 다른 사람의 풀이2_제일 간결, 깔끔한 로직 같음
def solution(a, b, c, d):
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)


# 다른 사람의 풀이3_sort를 했기 때문에 b>=c가 성립해서 abs를 할 필요가 없다고 함
def solution(a, b, c, d):
    dice=[a,b,c,d]
    dice.sort()
    a,b,c,d=dice
    s=set(dice)
    if len(s)==1:
        return 1111*a
    elif len(s)==4:
        return min(a,b,c,d)
    elif len(s)==2:
        if a==b==c:
            return (10*a+d)**2
        elif b==c==d:
            return (10*b+a)**2
        else:
            return (b+c)*(abs(b-c))
    else:
        if a==b: return c*d
        elif b==c: return a*d
        else: return a*b

    answer = 0
    return answer


# 다른 사람의 풀이4
from collections import Counter

def solution(a: int, b: int, c: int, d: int):
    dice_counter = Counter([a, b, c, d])

    size = len(dice_counter)

    if size == 1:
        return int(str(a) * 4)
    elif size == 2:
        p, q = sorted(dice_counter.keys(), key=lambda x: -dice_counter[x])

        if dice_counter[p] == 2:
            return (p + q) * abs(p - q)
        else:
            return (10 * p + q) ** 2
    elif size == 3:
        q, r = "", ""

        for dice_num, cnt in dice_counter.items():
            if cnt != 2:
                if q == "":
                    q = dice_num
                else:
                    r = dice_num

        return q * r
    else:
        return min(a, b, c, d)


# 다른 사람의 풀이5
def solution(a, b, c, d):
    answer = 0

    count = {}
    for x in (a, b, c, d):
        count[x] = count.get(x, 0) + 1

    count_list = sorted(list(count.items()), key=lambda x: x[1])
    if len(count_list) == 1:
        answer = count_list[0][0] * 1111
    elif len(count_list) == 2:
        p, c = count_list.pop()
        q = count_list[0][0]
        if c == 3:
            answer = (10 * p + q) ** 2
        else:
            answer = (p + q) * abs(p - q)
    elif len(count_list) == 3:
        q, r = count_list[0][0], count_list[1][0]
        answer = q * r
    else:
        answer = min(a, b, c, d)

    return answer
