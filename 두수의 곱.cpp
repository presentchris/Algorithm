// 내 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1*num2;
    return answer;
}


// 내 풀이2
int solution(int num1, int num2) {
    return int(num1) * int(num2);
}


// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    return num1 * num2;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;

    if( ( ( 0 <= num1 ) && ( 100 >= num1 ) )
      && ( ( 0 <= num2 ) && ( 100 >= num2 ) ) )
    {
        answer = num1 * num2;
    }

    return answer;
}


// 다른 사람의 풀이3
int kake(int a, int b) { 
    int res = 0; 
    while (b > 0) { 
        if (b & 1) res = res + a; 
        a = a << 1; 
        b = b >> 1; 
    } 
    return res; 
} 

int solution(int num1, int num2) {
    return kake(num1, num2);
}


// 다른 사람의 풀이4
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    answer = num1*num2;
    return answer;
}
