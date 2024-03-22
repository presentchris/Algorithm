// 내 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    for(int i = 1; i <= n; i += 2){
        answer.push_back(i);
    }
    return answer;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    for(int i=1;i<=n;i+=2) answer.push_back(i);
    return answer;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    int i = 1;
    while(i <= n)
    {
        answer.emplace_back(i);
        i+=2;
    }
    return answer;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>
using namespace std;
vector<int> solution(int n) {
    vector<int> answer;
    for (int i = 1; i <= n; i++)
        if (i % 2 == 1)
            answer.push_back(i);
    return answer;
}


// 다른 사람의 풀이4
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer;
    for(int i=1;i<=n;i++){
        if(i&1)
            answer.push_back(i);
    }
    return answer;
}
