   fun main() {
        println(checkPS("[()]"))
    }

    fun checkPS(input: String): Boolean {
        var stack = mutableListOf<Char>()
        for (c in input) {
            for (j in input) {
                when (j) {
                    '[' -> stack.add(j)
                    ']' -> {
                        if (stack.isEmpty() || stack.last() != '[') {
                            return false
                        } else {
                            stack.removeAt(stack.size - 1)
                        }
                    }
                }
            }
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
