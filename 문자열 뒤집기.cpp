// 내 풀이1
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string my_string) {
    reverse(my_string.begin(), my_string.end());
    return my_string;


// 내 풀이2
#include <string>

using namespace std;

string solution(string my_string) {
    string ans = "";
    for (int i = my_string.size()-1; i >= 0; i--) {
ans += my_string[i];
}
    return ans;
}


// 다른 사람의 풀이1
#include <bits/stdc++.h>

using namespace std;

string solution(string my_string) {
    return string(my_string.rbegin(), my_string.rend());
}


// 다른 시람의 풀이2
include <string>
#include <vector>
using namespace std;

string solution(string my_string) {
    string answer = "";
    for(int i=my_string.size()-1; i>=0;i--){
        answer.push_back(my_string[i]);
    }
    return answer;
}
