// 내 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    vector<int> answer(2);
    answer[0] = money/5500;
    answer[1] = money%5500;
    return answer;
}


// 내 풀이2
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    vector<int> answer;
    answer.push_back(money/5500);
    answer.push_back(money%5500);
    return answer;


// 다른 사람의 풀이1
#include <vector>

using namespace std;

vector<int> solution(int money) {
    return vector<int> {money / 5500, money % 5500};
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    return {money / 5500, money % 5500};
}


// 다른 사람의 풀이3
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int money) {
    vector<int> answer;
    int cnt = 0;
    while(money>=5500) {
        cnt++;
        money -= 5500;   
    }
    answer.push_back(cnt);
    answer.push_back(money);
    return answer;
}


// 다른 사람의 풀이4
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int hiki(int x, int y) {
    if (!y) return x;
    return hiki(x ^ y, (~x & y) << 1);
}

int kake(unsigned int a, unsigned int b) { 
    int res = 0;
    while (b) { 
        if (b & 1) res = res + a; 
        a = a << 1; 
        b = b >> 1; 
    } 
    return res; 
} 

int wari(int w1, int w2) {
    if (w2 == 1) return w1;
    int ans = exp(log(w1) - log(w2)) + 0.0000000001;
    return ans;
}

vector<int> solution(int money) {
    return vector<int>{wari(money, 5500), hiki(money, kake(5500, wari(money, 5500)))};
}
