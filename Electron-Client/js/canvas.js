var nodeConsole = require('console');
const { app } = require('electron');
var appConsole = new nodeConsole.Console(process.stdout, process.stderr);
const strokes = [];
const selected_line = [];

const windowToCanvas = (canvas, x, y) => {
    //获取canvas元素距离窗口的一些属性，MDN上有解释
    let rect = canvas.getBoundingClientRect()
    //x和y参数分别传入的是鼠标距离窗口的坐标，然后减去canvas距离窗口左边和顶部的距离。
    return {
        x: x - rect.left * (canvas.width/rect.width),
        y: y - rect.top * (canvas.height/rect.height)
    }
}

function read_strokes(){
    var fs = require('fs');
    fs.readFile('Json/Curr_Stroke.json','utf-8', function (err,data) {
        if (err) throw err;
        appConsole.log('Read Stroke!');
        strokes.push(JSON.parse(data));
    });
}

function activate_canvas(){
    appConsole.log("canvas activate")
    let theCanvas = document.getElementById('theCanvas')
    let context = theCanvas.getContext('2d')
    let isAllowDrawLine = false
    let nextstroke = []

    theCanvas.onmousedown = function(e) {
        isAllowDrawLine = true
        let ele = windowToCanvas(theCanvas, e.clientX, e.clientY)
        let { x, y } = ele
        context.moveTo(x, y)
        nextstroke.push([x/2,y/2]) 
        theCanvas.onmousemove = (e) => {
            if (isAllowDrawLine) {
                let ele = windowToCanvas(theCanvas, e.clientX, e.clientY)
                let { x, y } = ele
                context.lineTo(x, y)
                nextstroke.push([x/2,y/2]) 
                context.stroke()
            }
        }
    }
    theCanvas.onmouseup = function() {
        strokes.push(nextstroke);
        nextstroke = []
        isAllowDrawLine = false
    }
}


