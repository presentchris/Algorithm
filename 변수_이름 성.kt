//[변수]
//아래 동작 구현에 코드를 추가하여 원하는 결과물을 출력하세요.

//var first = "성"
//var second = "이름"
///* 동작 구현 */
//println("결과물: $first $second") // "결과물: 이름 성"

fun main() {
    var first = "성"
    var second = "이름"
    first = second
    second = "성"
    println("결과물 : $first $second")
}
