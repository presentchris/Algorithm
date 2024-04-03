# 내 풀이1_완벽히 맞지는 않다
def solution(price):
    if price >= 500000:
        return price * 0.8
    elif price >= 300000:
        return price * 0.9
    elif price >= 100000:
        return price * 0.95

  # 내 풀이2_채점했을 때 완벽한 답
  def solution(price):
    ans = 0
    if price >= 500000:
        ans = price * 0.8
    elif price >= 300000:
        ans = price * 0.9
    elif price >= 100000:
        ans = price * 0.95
    else:
        ans = price
    return int(ans)

# 다른 사람의 풀이1
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

# 다른 사람의 풀이2
def solution(price):
    return (100 - len([1 for k in [100000, 300000, 500000, 500000] if k<=price])*5) * price // 100

# 다른 사람의 풀이3
def solution(price):
    return int(price*0.8) if price>=500000 else int(price*0.9) if price>=300000 else int(price*0.95) if price>=100000 else price
