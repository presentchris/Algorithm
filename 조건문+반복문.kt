fun main() {
    val list = listOf<Int>(5, 1, 7, 3, 8)
    val n = 6
    val newList = mutableListOf<Int>()
    for (i in 0 until list.size){
        if (list[i]>n){
            newList.add(list[i])
        }
    }
    println("결과물: $newList")
}
