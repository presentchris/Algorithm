// 내 풀이
using System;

public class Solution {
    public int solution(int num1, int num2) {
        int answer = 0;
        if (num1 == num2){
            answer = 1;
        }
        else {
            answer = -1;
        }
        return answer;
    }
}


// 다른 사람의 풀이1
using System;

public class Solution {
    public int solution(int num1, int num2) {

        return num1 == num2 ? 1 : -1;
    }
}


// 다른 사람의 풀이2
using System;

public class Solution {
    public int solution(int num1, int num2) {
        int answer = 1;
        if(num1 != num2) answer *= -1;
        return answer;
    }
}
