fun main() {
    println(average(listOf(100, 80, 90)))
}

fun average(input: List<Int>): Int {
    var avg = 0
    var n = input.size
    for (i in input) {
        avg += i
    }
    return avg / n  
}
