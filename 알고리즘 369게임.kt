fun main() {
    game()
}

fun game() {
    var n = 1
    while (n <= 100) {
        if (n.toString().contains("3") || n.toString().contains("6") || n.toString().contains("9"))
            println("clap")
        else
            println(n)
        n++
    }
}
