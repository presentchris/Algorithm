import java.util.Stack

fun main() {
    println(reverseWord("hi"))
    println(reverseWord("easy"))
}

fun reverseWord(input: String): String {
    val stack = Stack<Char>()
    for (char in input) {
        stack.push(char)
    }
    var reverse = ""
    while (!stack.isEmpty()) {
    reverse += stack.pop()
    }

    return reverse
}
