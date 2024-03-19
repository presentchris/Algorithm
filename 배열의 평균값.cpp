// 내 풀이1
#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    if(numbers.empty()){
        return 0;
    }
    double sum = 0;
    for(int i: numbers){
        sum+=i;
    }
    double average = sum / numbers.size();
    return average;
}


// 내 풀이2
#include <numeric>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double sum = std::accumulate(numbers.begin(), numbers.end(), 0.0);
    double avg = sum / numbers.size();
    return avg;
}


// 내 풀이3
#include <numeric>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double sum = std::reduce(numbers.begin(), numbers.end(), 0.0);
    double avg = sum / numbers.size();
    return avg;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>
#include <numeric>
using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    int sum = accumulate(begin(numbers), end(numbers), 0, plus<int>());
    answer = (double)sum / numbers.size();
    return answer;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    for(int i = 0; i < numbers.size(); i++)
        answer += numbers[i];
    answer = answer / numbers.size();
    return answer;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>
#include <numeric>
using namespace std;

double solution(vector<int> numbers) {
    double answer = accumulate(numbers.begin(),numbers.end(),0.0) / numbers.size();
    return answer;
}


// 다른 사람의 풀이4
#include <vector>
#include <numeric>
double solution(std::vector<int> n) {
    return reduce(n.cbegin(),n.cend(), 0.0) / n.size();
}


// 다른 사람의 풀이5_이 코드는 일반화될 수는 없는 것 같다
#include <vector>
using namespace std;
double solution(vector<int> numbers) {
    return (double)(*numbers.begin() + numbers.back()) / 2;
}