class Ball {
    constructor() {
        this.image = imageFromPath('img/ball.png'),
            this.w = 8,
            this.h = 8,
            this.x = 150,
            this.y = 230,
            this.speedX = 5,
            this.speedY = 5
    }
    反弹 = function () {
        this.speedY *= -1
    }

    move = function () {
        if (this.x < 0 || this.x + this.w > 400) {
            this.speedX *= -1
        }

        if (this.y < 0 || this.y + this.h > 300) {
            this.speedY *= -1
        }

        this.x += this.speedX
        this.y += this.speedY

    }
}
