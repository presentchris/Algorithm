fun main() {
    println(tomorrow("월"))
}

fun tomorrow(input: String): String {
    var day = listOf<String>("월", "화", "수", "목", "금", "토", "일")
    var i = 0
    if (input in day) {
        i = day.indexOf(input) + 1
    }
    return day[i]
}
