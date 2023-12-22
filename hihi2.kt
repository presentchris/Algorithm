fun main(){
  val answer = repeatWord("hi", 2)
  println(answer)
}
//repeatWord 함수에 hi와 2를 저장하고 answer라는 변수에 넣는다
//answer를 출력한다
//repeatWord 함수에 문자열 input과 정수 n을 받는다
//n은 1보다 크거나 같고 10보다 작거나 같다

fun repeatWord(input:String, n:Int):String {
//n in 1..10
  //answer라는 변수를 문자열로 초기화한다
  var answer:String=""
  //n번만큼 answer를 반복한다
  repeat(n) {
    //answer라는 변수에 answer와 input을 더한다
    answer = answer + input
  }
  //answer값을 반환한다
  return answer
}
  
