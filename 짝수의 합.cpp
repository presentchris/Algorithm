// 내 풀이1_ n이 짝수이면, n 자체가 n 이하의 가장 큰 짝수, n이 짝수이면, n 자체가 n 이하의 가장 큰 짝수 / 등차수열의 합 공식은 S = n * (a1 + an) / 2 => n은 항의 개수, a1은 첫 번째 항, an은 마지막 항
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int maxEven = (n % 2 == 0) ? n : n - 1;
    int sum = (maxEven / 2) * (2 + maxEven) / 2;
    return sum;
}


// 내 풀이2 _ for (초기화; 조건; 증감) { 반복할 코드 블록 }
int solution(int n) {
    int sum = 0;
    for (int i = 1; i <= n; ++i) { 
        if (i % 2 == 0) { 
            sum += i; 
        }
    }
    return sum;
}


// 다른 사람의 풀이1_실제로 계산해보니까 진짜 이 방식이 적용된다
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = n/2;
    answer *= answer + 1;
    return answer;
}


// 다른 사람의 풀이2_위 풀이의 비트 오른쪽 시프트 연산 버전. n >> 1은 n을 2로 나눈 것과 동일한 효과를 가짐. 예를 들어, n이 10(이진수로 1010)이면, n >> 1의 결과는 5(이진수로 0101). 정수 나눗셈의 결과와 같으므로, 소수점 이하를 버림.
int solution(int n) {return (n>>1) * ((n>>1) + 1);}

