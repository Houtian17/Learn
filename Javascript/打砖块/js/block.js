class Block {
    constructor(position) {
        this.image = imageFromPath('img/block.png'),
            this.w = 32,
            this.h = 16,
            this.x = position[0],
            this.y = position[1],
            this.alive = true
    }

    kill() {
        this.alive = false
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








