//checkPS("()") == true
//checkPS("()()") == true
//checkPS("(())()") == true


//input이라는 문자열을 받는 checkPS를 Boolean형식으로 출력하는 함수를 만든다
//변형가능한 리스트를 stack이라는 변수에 할당한다
//c라는 변수가 input만큼 반복하는 동안
//c일 때, '('를 stack에 저장한다
//')'는 만약 stack이 비었거나, stack 리스트/배열의 마지막 요소가 '('가 아닌 경우
//false를 반환한다
//그렇지 않으면, stack의 리스트 개수 -1번째 요소를 제거한다
//비어있는 stack을 반환한다

fun main() {
    println(checkPS("()"))
}

fun checkPS(input: String): Boolean {
    var stack = mutableListOf<Char>()
    for (c in input) {
        when (c) {
            '(' -> stack.add(c)
            ')' -> {
                if (stack.isEmpty() || stack.last() != '(') {
                    return false
                } else {
                    stack.removeAt(stack.size - 1)
                }
            }
        }
    }

    return stack.isEmpty()
}
