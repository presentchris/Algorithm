# 1. 거스름돈 계산하기
saving_money = 34200
tenthousand = saving_money // 10000
rest = saving_money % 10000
print('1만원:' , tenthousand, '장 , 남은금액 :', rest)
# print('1만원: {0} 장 , 남은금액 : {1}'.format(tenthousand,rest))
# print(f'1만원: {tenthousand} 장 , 남은금액 : {rest}')


# 2. 이등변 삼각형 넓이 구하기
a = int(input('밑변의 길이를 입력하세요'))
h = int(input('높이를 입력하세요'))
s = a * h * 1/2
print(s)
print('이등변 삼각형 넓이는 = ', h, '*', a, ' * 1/2 = ', s)
# print(f'이등변 삼각형 넓이는 = {h} * {a} * 1/2 = {s}')


# 3. 자동 판매기 프로그램
money = int(input('투입할 돈: '))
price = int(input('물건값: '))
change = money - price
coin500 = change // 500
coin500_rest = change % 500
coin100 = coin500_rest // 100
print('거스름돈: ', change)
print('거스름돈 500원: ' ,coin500 )
print('거스름돈 100원 ', coin100)


# 4. 성적처리 프로그램
kor = int(input('국어 점수를 입력하세요 : '))
eng = int(input('영어 점수를 입력하세요 : '))
math = int(input('수학 점수를 입력하세요: '))
print('과목별 성적')
print('='*35)
print(f' 국어 : {kor} , 영어 : {eng} , 수학 : {math}')
print('='*35)
sum = kor + eng + math
avg = sum / 3
print('총점 : ', sum)
print('\n%%연산자-평균 : %.2f' % avg)
# print('format함수-평균 : {:.2f}'.format(avg))
# print(f'f문자-평균 : {avg:.2f}')


# 5. BMI 지수 구하기
height = int(input('키를 입력하세요'))
weight = int(input('몸무게를 입력하세요'))
bmi = weight / ((height /100)**2)
print('당신의 BMI 지수는 ', round(bmi,2), '입니다')


# 6. 주민번호 처리하기
pin = '921324-1068934'
yy = pin[:2]
sex = pin[7]
print(yy,'년생')
print(sex)
