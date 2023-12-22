fun main(){
    println(day("화"))
}

fun day(input:String):String{
    var yesterday = listOf<String>("월","화","수","목","금","토","일")
    var i = 0
    if(input in yesterday) {
        i = yesterday.indexOf(input)
        --i
    }
    return yesterday[i]
} 
