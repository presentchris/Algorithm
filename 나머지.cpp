// 내 풀이
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    return num1%num2;
}


// 다른 사람의 풀이1
#include <cmath>
int hiki(int x, int y) {
    if (y == 0) return x;
    return hiki(x ^ y, (~x & y) << 1);
}

int kake(unsigned int a, unsigned int b) { 
    int res = 0;
    while (b > 0) 
    { 
        if (b & 1) res = res + a; 
        a = a << 1; 
        b = b >> 1; 
    } 
    return res; 
} 

int wari(int w1, int w2) {
    if (w1 == 0) return 0;
    if (w2 == 0) return 0;
    int sign = (w1 < 0) ^ (w2 < 0);
    w1 = abs(w1);
    w2 = abs(w2);
    if (w2 == 1) return ((sign == 0) ? w1 : -w1);
    int ans = exp(log(w1) - log(w2)) + 0.0000000001;
    return ((sign == 0) ? ans : -ans);
}

int solution(int num1, int num2) {
    return hiki(num1, kake(num2, wari(num1, num2)));
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = -1;
    return num1 % num2;
}
