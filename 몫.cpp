// 내 풀이
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    return num1/num2;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;

    if( ( (0 < num1) && (100 >= num1) ) &&
       ( ( 0 < num2 ) && (100 >= num2) ) )
    {
        answer = num1 / num2;
    }

    return answer;
}


// 다른 사람의 풀이2
#include <cmath>
long long int divide(long long int n1, long long int n2) {
    if (n1 == 0 || n2 == 0) return 0;
    long long int sign = (n1 < 0) ^ (n2 < 0);
    n1 = std::abs(n1);
    n2 = std::abs(n2);
    if (n2 == 1) return ((sign == 0) ? n1 : -n2);
    long long int ans = exp(log(n1) - log(n2)) + 0.0000000001;
    return ((sign == 0) ? ans : -ans);
}
int solution(int num1, int num2) {
    return divide(num1, num2);
}
