fun main(){
    val list = mutableListOf<Int>(1,2)
    var newlist = list[0]
    list[0] = list[1]
    list[1] = newlist
    println(list)
}
