import java.util.LinkedList
import java.util.Queue

fun main() {
    println(mixAlphabet(1))
}

fun mixAlphabet(input:Int):String{
    val queue: Queue<String> = LinkedList()
    var i = input
    queue.add("a")
    queue.add("b")
    queue.add("c")
    queue.add("d")
    queue.add("e")
    queue.add("f")
    queue.add("g")
    queue.add("h")
    queue.add("i")
    queue.add("j")
    queue.add("k")
    queue.add("l")
    queue.add("m")
    queue.add("n")
    queue.add("o")
    queue.add("p")
    queue.add("q")
    queue.add("r")
    queue.add("s")
    queue.add("t")
    queue.add("u")
    queue.add("v")
    queue.add("w")
    queue.add("x")
    queue.add("y")
    queue.add("z")



    var n = queue.size

    for (j in i..n){
        queue.poll()
        queue.add(queue.poll())
        println(queue.peek())

    }
    return queue.element()
}


//리스트   val queue: Queue<Int> = LinkedList() 생성
//input의 변수 지정
//n = list.size
//큐에 요소 추가
//input에 정수값이 들어오면,
//n까지 반복하는 동안,
//큐에서 첫번째 요소 제거 = remove / poll
//요소 맨뒤로 보내기 = += / add
//요소 출력 = peek / element
