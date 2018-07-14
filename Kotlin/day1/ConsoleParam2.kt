package xyz.houtian17.kt03

fun main(args: Array<String>) {
    args.flatMap {
        it.split("_")
    }.map {
        print("$it ${it.length}")
    }
}