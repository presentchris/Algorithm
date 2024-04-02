// 내 풀이1
using System;

public class Solution {
    public int solution(int slice, int n) {
        int answer = 0;
        if (n%slice==0){
            answer = n/slice;
        }
        else {
            answer = n/slice+1;
        }
        return answer;
    }
}


// 내 풀이2
using System;

public class Solution {
    public int solution(int slice, int n) {
        int answer= n%slice==0?n/slice:n/slice+1;
        return answer;
    }
}


// 다른 사람의 풀이1
using System;

public class Solution
{
    public int solution(int slice, int n)
    {
        return n % slice > 0 ? n / slice + 1 : n / slice;
    }
}


// 다른 사람의 풀이2
using System;

public class Solution {
    public int solution(int slice, int n) {
        return (int)Math.Ceiling(n / (double)slice);
    }
}

