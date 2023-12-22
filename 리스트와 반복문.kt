fun main() {
    println(summ(listOf(100, 80, 90)))
}
//summ함수에 값 넣어서 출력

fun summ(input: List<Int>): Int {
    var sum = 0
    for (i in input) {
        sum += i
    }
    return sum
}

//i가 input만큼 반복될 때,
//sum에다가 i 더함
//sum 반환
