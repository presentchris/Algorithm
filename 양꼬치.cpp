// python
solution = lambda n, k: n*12000+k*2000-(int(n/10)*2000)

  
// C++
#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    return n*12000+k*2000-(int(n/10)*2000);
}


// 다른 사람의 풀이(C++)
#include <string>
#include <vector>

using namespace std;

int solution(int n, int k) {
    return (n*12000) + ((k-(n/10))*2000);
}
