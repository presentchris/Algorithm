
//[리스트 + 변수]
//아래 동작 구현에 코드를 추가하여 원하는 결과물을 출력하세요.
//val list = mutableListOf(1,2)
///* 동작 구현 */
//println("결과물: $list") // "결과물: [2, 1]"
​
​
fun main(){
    val list = mutableListOf<Int>(1,2)
    list[0] = list[1]
    list[1] = 1
    println(list)
}
