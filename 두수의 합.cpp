#내 풀이
#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    int answer = num1+num2;
    return answer;
}


#다른 사람의 풀이1
#include <iostream>

int solution(int num1, int num2) {
    int answer;
    answer = num1 + num2;
    return answer;
}

int main(void) {
    std::ios_base::sync_with_stdio(false);
    int num1, num2;
    std::cin >> num1 >> num2;
    std::cout << solution(num1, num2);
}


#다른 사람의 풀이2
int Add(int x, int y) { 
    while (y != 0) { 
        unsigned carry = x & y;
        x = x ^ y;
        y = carry << 1; 
    } 
    return x; 
}

int solution(int num1, int num2) { 
    return Add(num1, num2);
}
