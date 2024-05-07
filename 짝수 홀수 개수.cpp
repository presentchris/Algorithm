// 내 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    int oddcount = 0;
    int evencount = 0;
    for (int i : num_list){
        if (i%2==0){
            evencount += 1;
        } else {
            oddcount += 1;
        }
    }
    vector<int> answer = {evencount, oddcount};
    return answer;
}


// 내 풀이2_count_if 함수를 사용
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> num_list) {
    int counteven = count_if(num_list.begin(), num_list.end(), [](int i){
        return i%2==0;
    });
    int countodd = num_list.size() - counteven;
    vector<int> ans = {counteven, countodd};
    return ans;
}


// 내 풀이3_accumulate과 make_pair를 사용
#include <vector>
#include <numeric>
#include <utility>

using namespace std;

vector<int> solution(vector<int> num_list) {
    pair<int,int> counts = accumulate(num_list.begin(), num_list.end(), make_pair(0,0), [](pair<int,int> list, int num){
        return num%2==0 ? make_pair(list.first+1, list.second) : make_pair(list.first, list.second+1);
    });
    vector<int> ans = {counts.first, counts.second};
    return ans;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer(2, 0);
    for (int num : num_list) {
        answer[num % 2]++;
    }
    return answer;
}


// 다른 사람의 풀이2
#include <vector>
std::vector<int> solution(std::vector<int> num_list) {
    std::vector<int> answer(2,0);
    for(const auto& i : num_list) answer[i&1]++;
    return answer;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    int even = 0;
    for(int i = 0; i < num_list.size(); i++){
        if(num_list[i] % 2 == 0)
            even++;
    }
    answer.push_back(even);
    answer.push_back(num_list.size()-even);
    return answer;
}
