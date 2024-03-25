// 내 풀이1
#include <vector>
#include <map>
using namespace std;

int solution(vector<int> array) {
    map<int, int> frequencyMap;
    
    // 각 숫자의 빈도수를 계산합니다.
    for(int num : array) {
        frequencyMap[num]++;
    }
    
    int maxFrequency = 0; // 가장 높은 빈도수
    int mode = -1; // 최빈값, 초기값은 -1 (최빈값이 여러 개인 경우를 대비)
    
    // 최빈값과 그 빈도수를 찾습니다.
    for(auto const& [num, freq] : frequencyMap) {
        if(freq > maxFrequency) {
            maxFrequency = freq;
            mode = num;
        } else if(freq == maxFrequency) {
            // 이미 maxFrequency와 같은 빈도수의 숫자가 있다면, 최빈값은 여러 개임을 의미
            mode = -1;
        }
    }
    
    // 최빈값이 유일하게 존재하는 경우에만 그 값을 반환합니다.
    // 최빈값이 여러 개인 경우, -1이 반환됩니다.
    return mode;
}


// 내 풀이2
#include <vector>
#include <algorithm> // std::sort 사용을 위해 필요
using namespace std;

int solution(vector<int> numbers) {
    if (numbers.empty()) return -1;

    // 배열 정렬
    sort(numbers.begin(), numbers.end());

    int currentCount = 1; // 현재 값의 등장 횟수
    int maxCount = 0; // 최대 등장 횟수
    int mode = numbers[0]; // 최빈값
    bool multipleModes = false; // 최빈값이 여러 개 있는지 여부

    // 정렬된 배열을 탐색하며 최빈값 찾기
    for (size_t i = 1; i < numbers.size(); ++i) {
        if (numbers[i] == numbers[i - 1]) {
            // 현재 값이 이전 값과 같다면, 카운트 증가
            ++currentCount;
        } else {
            // 새로운 값이 등장했을 때
            if (currentCount > maxCount) {
                maxCount = currentCount;
                mode = numbers[i - 1];
                multipleModes = false; // 새로운 최빈값이 등장했으므로 false로 설정
            } else if (currentCount == maxCount) {
                multipleModes = true; // 최빈값이 여러 개 있다는 표시
            }
            currentCount = 1; // 카운트 초기화
        }
    }

    // 마지막 값 처리
    if (currentCount > maxCount) {
        mode = numbers.back();
        multipleModes = false;
    } else if (currentCount == maxCount) {
        multipleModes = true;
    }

    // 최빈값 반환
    return multipleModes ? -1 : mode;
}


// 다른 사람의 풀이1
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    int maxV = 0;

    unordered_map<int,int> um;
    for(const auto v : array)
    {
        um[v]++;
    }

    for(const auto& v : um)
    {
        if(v.second > maxV)
        {
            maxV = v.second;
            answer = v.first;
        }
        else if(v.second == maxV)
        {
            answer = -1;
        }
    }

    return answer;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    bool overlap = false;

    int num[2003] = {0};

    for(int i = 0; i < array.size(); i++)
    {
        num[array[i]+1000]++;
    }

    for(int i = 0; i < 2003; i++)
    {
        if(num[answer] < num[i])
        {
            overlap = false;
            answer = i;
        }
        else if(num[answer] == num[i])
        {
            overlap = true;
        }
    }

    if(overlap == true) return -1;

    return answer - 1000;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
vector<int> arr(2010);
int solution(vector<int> array) {
    int answer = 0;
    for(int i = 0; i < array.size(); i++){
        arr[array[i]+999]++;
    }

    int max = 0;
    for(int i = 0; i < arr.size(); i++){
        if(max < arr[i])
            max = arr[i];
    }

    int cnt = 0;
    for(int i = 0; i < arr.size(); i++){
        if(max == arr[i]){
            answer = i;
            cnt++;
            if(cnt > 1)
                return -1;
        }
    }

    return answer - 999;
}
