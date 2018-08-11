package xyz.houtian17.kt03

enum class Lang(val hello: String) {
    ENGLISH("hello"),
    CHINESE("你好"),
    JAPANESE("おはよう"),
    KORENAN("안녕하세요");

    fun sayHello() {
        println(hello)
    }

    companion object {
        fun parse(name: String): Lang {
            return Lang.valueOf(name.toUpperCase())
        }
    }
}

fun main(args: Array<String>) {
    if (args.isEmpty()) return
    val lang = Lang.parse(args[0])
    println(lang)
    lang.sayHello()
    lang.sayBye()
}

fun Lang.sayBye() {
    val bye = when (this) {
        Lang.ENGLISH -> "bye"
        Lang.CHINESE -> "再见"
        Lang.JAPANESE -> "バイ"
        Lang.KORENAN -> "안녕"
    }
    println(bye)
}