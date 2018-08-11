package xyz.houtian17.kt03

fun main(args: Array<String>) {
    val user = User(0, "233")
    println(user)

    HelloKotlin::class.constructors.map(::println)
}

class HelloKotlin {
    fun hello(){

    }
}