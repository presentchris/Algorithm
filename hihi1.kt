fun main() {
  val answer = repeatWord("hi", 2)
  println(answer)
}
//repeatWord 함수에 hi와 2를 저장하고 answer라는 변수에 넣는다
//answer를 출력한다

fun repeatWord(input:String, n:Int):String{
  //repeatWord 함수에 문자열 input과 정수 n을 받는다
  n in 1..10
  //n은 1보다 크거나 같고 10보다 작거나 같다
  var answer:String = ""
  repeat(n) {
    answer += input
  }
  return answer
}
//answer라는 변수에 텍스트 문자열을 저장한다
//answer라는 변수는 input을 n번만큼 반복하여 더한다
//answer값을 반환한다
