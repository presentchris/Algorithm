// 내 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> ans;
    for (int n : numbers) {
        ans.push_back(n*2); 
    }
    return ans;
}


// 내 풀이2
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> ans(numbers.size());
    std::transform(numbers.begin(), numbers.end(), ans.begin(), [](int n) {
        return n * 2; 
    });
    return ans;
}


// 다른 사람의 풀이1
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    for(int i=0; i<numbers.size(); i++)
        numbers[i] = numbers[i] << 1;
    return numbers;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    for(auto& v : numbers)
    {
        v *=2;
    }

    return numbers;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for(auto a : numbers) answer.push_back(2 * a);
    return answer;
}


// 다른 사람의 풀이4
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    for(int i = 0; i < numbers.size(); i++){
        answer.push_back(numbers[i]*2);
    }
    return answer;
}


// 다른 사람의 풀이5
#include <bits/stdc++.h>
using namespace std;

vector<int> solution(vector<int> numbers) {
    return accumulate(numbers.begin(), numbers.end(), vector<int>(), [](vector<int>& acc, int cur){
        acc.push_back(cur * 2);
        return acc;
    });
}
