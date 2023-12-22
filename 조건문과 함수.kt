//[조건문+함수]
//세개의 Int a,b,c가 주어졌을 때 두번째로 큰 수를 Int로 반환하는 함수
//ex) 12, 51, 3 -> 12

fun main() {
    var a = 3
    var b = 7
    var c = 12
    println(secondLargest(a,b,c))
}

//a,b,c의 값을 입력받음
//second함수를 적용
fun secondLargest(a: Int, b: Int, c: Int): Int {
    val second = mutableListOf<Int>(a,b,c)
    var i = second.indexOf(a)
    var j = second.indexOf(b)
    var n = second.indexOf(c)
    second.sortDescending()

    if (i == 1) {
        return second[i]
    }
    else if (j == 1) {
        return second[j]
    }
    else {
        return second[n]
    }
}

//list
//변수 i  = indexOf
//list요소 descending 내림차순 정렬
//if (i == 1),
//println [i]
