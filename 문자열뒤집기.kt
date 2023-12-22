//문자열 뒤집기 시작
//1. 리스트, ex."logic" -> l=list의[0]번째 -> list의 순서 = 01234 ->list의 문자열을 i로 두고
//String을 숫자로 변형해서? 내림차순 -> 43210 -> toString()해서 문자열로 바꾸면? -> "cigol"
//
//2. 리스트에서 반대로 더하기
//
//
//일상생활적인 의사코드 :
//리스트 함수를 만들어서 문자열로 출력하도록 한다 String "a"를 받는다
//a를 b 변수로 지정한다
//c변수로 지정한다
//c변수를 내림차순한다
//내림차순한 c를 문자열로 출력하도록 b를 반환한다
//
//메인 - 변수 d는 리스트of b
//        println(d)
//
//코드적인 의사코드


//.reversed() 함수를 알아냈다...
// or
//listOf[i]에서 n을 .size로 변수지정 -> n downTo 1
// or
//length-1 해서 반복 (변수 i가 0보다 작을 때 스탑)


//"asdgfhjyew"
//글자 수의 갯수를 n으로 지정한다
//맨 마지막 글자를 첫번째 배열로 가져온다
//그 뒤, 마지막에 있는 글자를 마지막으로 가져온 곳 다음(오른쪽)에 둔다
//이걸 n번 반복한다

//    var a = "abcd"
//    //글자 수의 갯수를 n으로 지정한다
//    var n = a.length
//    var m = n - 1
//    for (i in m downTo 0) {
//        if (i == m) {
//            print(a[m])
//        } else {
//            print(a[--m])
//        }
//    }





fun main() {
    reverse("abcd")
}
fun reverse(input:String){
    //글자 수의 갯수를 n으로 지정한다
    var n = input.length
    //맨 마지막 글자를 첫번째 배열로 가져온다
    var result = ""
    val lastCharacter = input[input.length - 1]
    //마지막으로 가져온 글자 앞에 있는 글자를, 리스트 끝에 둔다.
    result = result + lastCharacter
    //마지막 전 글자를 다음(오른쪽)에 둔다
    for(i )
//    for(i in n-1 downTo 0) {
//        if (i == n-1) {
//            println(gg[i])}
//        else{
////            println(gg[--i])
//        }
//    }

//이걸 n번 반복한다
//    var r = input
//
//    for(i in n downTo 0) {
//        if (i == n) {
//            print(r)
//        }
//    }
//    println()
}
main()
