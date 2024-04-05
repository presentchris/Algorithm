// 내 풀이1
#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    reverse(num_list.begin(), num_list.end());
    return num_list;
}


// 내 풀이2
#include <algorithm>
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> tem;
    for(int i = num_list.size()-1; i>=0; i--) {
    tem.push_back(num_list[i]);
}
    return tem;
}


// 다른 사람의 풀이1
#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    return vector<int> (num_list.rbegin(), num_list.rend());;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;

    swap(num_list,answer);
    reverse(answer.begin(),answer.end());

    return answer;
}


