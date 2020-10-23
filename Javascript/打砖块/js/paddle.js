class Paddle {
    constructor() {
        this.image = imageFromPath('img/paddle.png'),
            this.w = 64,
            this.h = 16,
            this.x = 150,
            this.y = 250,
            this.speed = 5
    }

    //创建paddl的移动功能
    move(x) {
        if (x < 0) {
            this.x = 0
        } else if (x + this.w > 400) {
            this.x = 400 - this.w
        } else {
            this.x = x
        }
    }

    moveLeft(x) {
        this.move(this.x - this.speed)
    }

    moveRight(x) {
        this.move(this.x + this.speed)
    }

    collide(ball) {
        if (this.x + this.w >= ball.x && this.x <= ball.x + ball.w) {
            if (this.y + this.h >= ball.y && this.y <= ball.y + ball.h) {
                return true
            }
        }
        return false
    }
}
