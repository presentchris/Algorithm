// 내 풀이1
#include <vector>
#include <algorithm> // sort 함수를 사용하기 위해 필요

using namespace std;

int solution(vector<int> array) {
    // 배열을 오름차순으로 정렬합니다.
    sort(array.begin(), array.end());

    // 배열의 중앙 인덱스를 계산합니다.
    int midIndex = array.size() / 2;

    // 중앙값을 반환합니다.
    return array[midIndex];
}



// 다른 사람의 풀이1
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    sort(array.begin(), array.end());
    answer = array[array.size()/2];
    return answer;
}


// 다른 사람의 풀이2
#include <string>
#include <vector>

using namespace std;

int vector_arrange(vector<int> input_array)
{
    for (int i = 0; i < input_array.size()-1; i++)
    {
        int* first_number = &input_array[i];

        for (int j = 1+i; j < input_array.size(); j ++)
        { 
            int* second_number = &input_array[j];

            if (*first_number > *second_number)
            {
                int temp = *first_number;
                *first_number = *second_number;
                *second_number = temp;
            }
        }
    }

    int result = input_array[input_array.size() / 2];

    return result;
}


// 다른 사람의 풀이3
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> array) {
    sort(array.begin(),array.end());

    return array[array.size()/2];
}


// 다른 사람의 풀이4
#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> array) {
    sort(array.begin(), array.end());
    return array[array.size() / 2];
}


// 다른 사람의 풀이5
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(vector<int> array) {
    sort(array.begin(), array.end());
    int center = array.size() / 2;
    int answer = array[center];
    return answer;
}