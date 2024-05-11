// python1
def solution(my_string, letter):
    return ''.join(my_string[i] for i in range(len(my_string)) if my_string[i] != letter)


// python2
solution = lambda my_string, letter: my_string.replace(letter, '')


// C++1
#include <string>#include <vector>

using namespace std;

string solution(string my_string, string letter) {
    char charletter = letter[0];
    string ans = "";
    for(char c : my_string){
        if(c!=charletter) ans+=c;
    }
    return ans;
}


// C++2
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(string my_string, string letter) {
    char charletter = letter[0];
    my_string.erase(remove(my_string.begin(), my_string.end(), charletter), my_string.end());
    return my_string;
}
