// 내 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int angle) {
    return angle < 90 ? 1 :
    angle == 90 ? 2 :
    angle < 180 ? 3 : 4;
}


// 내 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int angle) {
    int answer = 0;
    if (angle < 90){
        answer = 1;
    } else if (angle == 90){
        answer = 2;
    } else if (angle < 180){
        answer = 3;
    } else{
        answer = 4;
    }
    return answer;
}


// 다른 사람의 풀이1
int solution(int angle) {
    return angle % 90 == 0 ? angle / 90 * 2 : (angle / 90) * 2 + 1; 
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int angle) {
    return angle > 90 ? (angle == 180 ? 4 : 3) : (angle == 90 ? 2 : 1);
}


// 다른 사람의 풀이3
int solution(int angle) {
    return !(angle % 90) ? angle/45 : (angle/90 << 1) + 1;
}
