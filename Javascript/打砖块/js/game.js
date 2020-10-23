class Game {
    constructor() {
        //获取canvas元素
        var canvas = document.getElementById('id-canvas')
        //创建一个画板变量
        var ctx = canvas.getContext('2d')

        this.canvas = canvas
        this.ctx = ctx
        this.keyDowns = {}
        this.actions = {}

        this.setupInputs()

    }

    setupInputs() {
        var self = this
        //添加监听事件 让挡板动起来
        window.addEventListener('keydown', function (event) {
            //创建要监听的键值变量
            var k = event.key
            self.keyDowns[k] = true
        })
        window.addEventListener('keyup', function (event) {
            //创建要监听的键值变量
            var k = event.key
            self.keyDowns[k] = false
        })

    }

    //创建了一个回调函数,可以注册一个行为或者动作，注册一个事件
    registerAction(key, callback) {
        this.actions[key] = callback
    }

    doActions() {
        var keys = Object.keys(this.actions)
        for (var i = 0; i < keys.length; i++) {
            var k = keys[i]
            if (this.keyDowns[k]) {
                this.actions[k]()
            }
        }
    }

    update() {

    }

    run() {
        var canvas = this.canvas
        var self = this
        //状态更新代码
        setInterval(function () {
            self.doActions()
            //状态的更新
            self.update()
            //清除画布
            self.ctx.clearRect(0, 0, canvas.width, canvas.height)
            //绘图的更新
            self.draw()
        }, 1000 / 60)
    }
}
