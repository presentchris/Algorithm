// python 풀이1
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer

// python 풀이2
solution = lambda my_string, n: ''.join(i*n for i in my_string)


// C++ 풀이1_for문을 사용하여 j만큼 문자 반복
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string ans = "";
    for(char i: my_string){
        for(int j=0; j<n; j++){
            ans += i;
        }
    }
    return ans;
}


// C++ 풀이2
#include <string>
#include <vector>
#include <numeric>

using namespace std;

string solution(string my_string, int n) {
    return accumulate(my_string.begin(), my_string.end(), string(""), [n](string acc, char c){
        return acc + string(n,c);
    });
}


// C++ 풀이3
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string ans = "";
    for(char i: my_string){
        ans += string(n, i);
    }
    return ans;
}


// 다른 사람의 풀이1
  #include <bits/stdc++.h>

using namespace std;

string solution(string my_string, int n) {
    return accumulate(my_string.begin(), my_string.end(), string(), [n](string& acc, char c){
        for (int i = 0 ; i < n ; i++) acc.push_back(c);
        return acc;
    });


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";
    for(auto ch : my_string)
    {
        int t = n;
        while(t--)
            answer.push_back(ch);
    }
    return answer;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {
    string answer = "";

    for (int i = 0; i < my_string.length(); i++)
        for (int k = 0; k < n; k++)
            answer += my_string.substr(i,1);

    return answer;
}


// 다른 사람의 풀이4
#include <string>
#include <vector>

using namespace std;

string solution(string my_string, int n) {

    string answer = "";

    for (int i = 0; i < my_string.length(); i++) {

        for (int j = 0; j < n; j++) {

            answer += my_string.at(i);
        }
    }

    return answer;
}
