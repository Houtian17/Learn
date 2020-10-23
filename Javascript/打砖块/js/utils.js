var log = console.log.bind(console)

//加载图片
var imageFromPath = function (path) {
    var image = new Image()
    image.src = path
    return image
}
