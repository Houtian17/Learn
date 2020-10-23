var loadLevel = function (index) {
    window.blocks = []
    index = index - 1
    var level = levels[index]

    for (var i = 0; i < level.length; i++) {
        //位置 p的格式是[x,y]
        var p = level[i]
        var b = new Block(p)

        window.blocks.push(b)
    }
}

var enableDebugMode = function (enabled) {
    if (!enabled) {
        return
    }

    //加载调试关卡
    window.addEventListener('keydown', function (event) {
        var k = event.key
        if ('123456789'.includes(k)) {
            loadLevel(k)
        }
    })
}

var __main = function () {

    var game = new Game()
    var paddle = new Paddle()
    var ball = new Ball()

    enableDebugMode(true)

    loadLevel(1)

    game.registerAction('a', function () {
        paddle.moveLeft()
    })

    game.registerAction('d', function () {
        paddle.moveRight()
    })

    game.update = function () {
        ball.move()
        if (paddle.collide(ball)) {
            ball.反弹()
        }

        if (ball.y > paddle.y) {
            //游戏结束
            game.draw = function () {
                game.ctx.font = "48px serif"
                game.ctx.fillText("游戏结束", 50, 100)
            }
        }

        //draw blocks
        for (var i = 0; i < blocks.length; i++) {
            var b = blocks[i]
            if (b.alive) {
                if (b.collide(ball)) {
                    //杀掉这个block
                    b.kill()
                    ball.反弹()
                }
            }
        }
    }

    game.draw = function () {
        game.ctx.drawImage(ball.image, ball.x, ball.y)

        game.ctx.drawImage(paddle.image, paddle.x, paddle.y)

        //draw blocks
        for (var i = 0; i < blocks.length; i++) {
            var b = blocks[i]
            if (b.alive) {
                game.ctx.drawImage(b.image, b.x, b.y)
            }
        }
    }

    game.run()
}
__main()