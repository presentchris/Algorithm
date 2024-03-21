// 내 풀이1
#include <string>
#include <vector>
#include <numeric> // std::gcd 함수를 사용하기 위해 필요

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    // 공통 분모를 구하기 위해 두 분모의 곱을 계산합니다.
    int commonDenom = denom1 * denom2;
    // 분자를 공통 분모에 맞게 조정합니다.
    int commonNumer = numer1 * denom2 + numer2 * denom1;

    // 기약분수로 만들기 위해 분자와 분모의 최대공약수(GCD)를 구합니다.
    int gcd = std::gcd(commonNumer, commonDenom);

    // 최대공약수로 나누어 기약분수를 얻습니다.
    vector<int> answer = {commonNumer / gcd, commonDenom / gcd};
    return answer;
}


// 내 풀이2
#include <vector>
#include <numeric> // gcd 함수 사용을 위해

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    // 공통 분모를 계산합니다.
    int lcm = denom1 * denom2 / gcd(denom1, denom2);
    
    // 분자를 공통 분모에 맞게 조정하고 합산합니다.
    int sumNumer = numer1 * (lcm / denom1) + numer2 * (lcm / denom2);

    // 합산된 분수를 기약분수로 만들기 위해 분자와 분모의 최대공약수를 구합니다.
    int commonGCD = gcd(sumNumer, lcm);

    // 최대공약수로 분자와 분모를 나누어 기약분수를 얻습니다.
    return {sumNumer / commonGCD, lcm / commonGCD};
}



// 내 풀이3
#include <vector>
#include <numeric> // gcd 함수 사용을 위해

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    int sumNumer, sumDenom;

    // 분모가 같은 경우
    if (denom1 == denom2) {
        sumNumer = numer1 + numer2;
        sumDenom = denom1; // 또는 denom2, 둘은 같으므로
    } else {
        // 분모가 다른 경우
        sumDenom = denom1 * denom2 / gcd(denom1, denom2); // 최소공배수를 분모로 사용
        sumNumer = numer1 * (sumDenom / denom1) + numer2 * (sumDenom / denom2);
    }

    // 합산된 분수를 기약분수로 만들기 위해 최대공약수를 구함
    int commonGCD = gcd(sumNumer, sumDenom);

    // 최대공약수로 분자와 분모를 나누어 기약분수로 만듦
    sumNumer /= commonGCD;
    sumDenom /= commonGCD;

    return {sumNumer, sumDenom};
}



// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int denum1, int num1, int denum2, int num2) {
    vector<int> answer;
    int denum = (denum1 * num2) + (denum2 * num1);
    int num = num1 * num2;

    for(int i = min(denum, num); i >= 2 ; i--)
    {
        if(denum % i == 0 && num % i == 0)
        {
            denum /= i;
            num /= i;
            break;
        }
    }
    answer.push_back(denum);
    answer.push_back(num);

    return answer;
}



// 다른 사람의 풀이2
#include <string>
#include <vector>
using namespace std;
int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }
vector<int> solution(int denum1, int num1, int denum2, int num2) {
    vector<int> answer;
    int lcm = num1 * num2 / gcd(num1, num2);
    denum1 *= lcm / num1;
    denum2 *= lcm / num2;
    denum1 += denum2;
    int g = gcd(denum1, lcm);
    if(g == 1) {
        answer.push_back(denum1);
        answer.push_back(lcm);
    }
    else {
        answer.push_back(denum1 / g);
        answer.push_back(lcm / g);
    }
    return answer;
}



// 다른 사람의 풀이3
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int denum1, int num1, int denum2, int num2) {
    vector<int> answer;
    denum1 *= num2;
    denum2 *= num1;
    num1 *= num2;
    int top = denum1 + denum2;
    int bottom = num1;
    for(int i = 2; i <= bottom;){
        if(bottom == 1) break;
        if((top % i == 0) && (bottom % i == 0)){
            top /= i;
            bottom /= i;
        }
        else
            i++;
    }
    answer.push_back(top);
    answer.push_back(bottom);
    return answer;
}