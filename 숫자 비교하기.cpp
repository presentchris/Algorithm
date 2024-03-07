// 내 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    if(num1==num2){
        answer = 1;
    } else{
        answer = -1;
    }
    return answer;
}


// 내 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    if(num1==num2){
        answer = true;
    } else{
        answer = false-1;
    }
    return answer;
}


// 내 풀이3_삼항연산자
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    return num1 == num2 ? 1 : -1;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = -1;
    if(num1 == num2){
        return 1;
    }
    return answer;
}


// 다른 사람의 풀이2
int solution(int num1, int num2) {return num1 ^ num2 ? ~0 : 0^1;}


// 다른 사람의 풀이3
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    if(num1 == num2)
        return 1;
    return -1;
}
