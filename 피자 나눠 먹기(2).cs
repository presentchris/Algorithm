// 내 풀이1
using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=100; i++){
            if((6*i)%n==0){
                answer += i;
                break;
            }
        }
        return answer;
    }
}


// 내 풀이2
using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=100; i++){
            if((6*i)%n==0){
                answer = i;
                break;
            }
        }
        return answer;
    }
}


// 내 풀이3
using System;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 1;
        while(i <= 100) {
            if((6 * i) % n == 0) {
                answer = i;
                break;
            }
            i++;
        }
        return answer;
    }
}


// 내 풀이4_최대공약수(GCD)로 나눈 값으로 계산하여 n의 최소공배수(LCM)를 찾고, 그 최소공배수를 6으로 나눈 값이 필요한 피자 판 수, Gcd는 최대공약수를 찾는 함수, 최소공배수는 solution 함수
using System;

public class Solution {
    // 최대공약수를 계산하는 함수
    private static int Gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    // 필요한 피자 판 수를 계산하는 함수
    public int solution(int n) {
        // 6 조각 피자와 사람 수의 최소공배수를 구한다.
        int lcm = (n * 6) / Gcd(n, 6);
        // 최소공배수를 6으로 나누어 필요한 피자 판 수를 계산한다.
        return lcm / 6;
    }
}


// 내 풀이5_Gcd 메소드는 유클리드 호제법을 재귀적으로 사용하여 최대공약수를 계산. solution 메소드에서는 n과 6의 최대공약수를 n으로 나누어 필요한 피자 판 수를 직접 계산.
using System;

public class Solution {
    // 최대공약수(GCD)를 계산하는 메소드
    private static int Gcd(int a, int b) {
        return b == 0 ? a : Gcd(b, a % b);
    }

    // 필요한 최소 피자 판 수를 반환하는 메소드
    public int solution(int n) {
        return n / Gcd(n, 6);
    }
}


// 다른 사람의 풀이1
using System;

public class Solution {
    public int solution(int n) {
        int temp = n;
        while(n%6!=0)
        {
            n+=temp;
        }
        return n/6;
    }
}


// 다른 사람의 풀이2
using System;

public class Solution {
    public int solution(int n) {
        int answer = n * 6 / GCD(n, 6) / 6;
        return answer;
    }

    public int GCD(int a, int b)
    {
        return a % b == 0 ? b : GCD(b, a % b);
    }
}

