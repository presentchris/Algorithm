// 내 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    if (n%7==0){
        answer += n/7;
    }
    else{
        answer += (n/7)+1;
    }
    return answer;
}


// 내 풀이2
#include <cmath> // ceil 함수 사용을 위해 포함
using namespace std;

int solution(int n) {
    // 사람 수 n을 7로 나누고, 그 결과를 올림하여 필요한 피자의 수를 계산
    return ceil(n / 7.0);
}


// 내 풀이3
#include <cmath> // ceil 함수 사용을 위해 필요

int solution(int n) {
    // n을 7.0으로 나눈 값에 대해 ceil을 사용하여 올림 처리
    return static_cast<int>(ceil(static_cast<double>(n) / 7.0));
}


// 내 풀이4
#include <vector>

using namespace std;

int solution(int n) {
    // 필요한 최소 피자 수 계산
    int pizza = n / 7;
    
    // 나머지가 있다면, 한 개의 피자를 더 추가
    if (n % 7 > 0) {
        pizza += 1;
    }
    
    return pizza;
}


// 다른 사람의 풀이1
int solution(int n) {
    return n % 7 == 0 ? n / 7 : n / 7 + 1;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = (n+6)/7;
    return answer;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(int n) {
    int answer = ceil(n/7.f);
    return answer;
}


// 다른 사람의 풀이4
#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer;

    answer = n / 7;
    if(n % 7 != 0) {
        answer++;
    }

    return answer;
}
