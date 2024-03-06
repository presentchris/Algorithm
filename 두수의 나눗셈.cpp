// 내 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = (int)((double)num1/num2*1000) ;
    return answer;
}


// 내 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = (int)((float)num1/num2*1000) ;
    return answer;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    return (num1* 1000)/num2 ;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = ((num1*1.0) / num2) * 1000;
    return answer;
}


// 다른 사람의 풀이3
int solution(int num1, int num2) {
    num1 *= 1000;
    return (int)(num1/num2);
}


// 다른 사람의 풀이4
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    return double(num1) / double(num2) * 1000;
}
