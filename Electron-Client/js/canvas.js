var nodeConsole = require('console');
const { app } = require('electron');
var appConsole = new nodeConsole.Console(process.stdout, process.stderr);
const strokes = [];
const selected_line = [];
isAllowDraw = true;


const windowToCanvas = (canvas, x, y) => {
    //获取canvas元素距离窗口的一些属性，MDN上有解释
    let rect = canvas.getBoundingClientRect()
    //x和y参数分别传入的是鼠标距离窗口的坐标，然后减去canvas距离窗口左边和顶部的距离。
    return {
        x: x - rect.left * (canvas.width/rect.width),
        y: y - rect.top * (canvas.height/rect.height)
    }
}

function redraw(){
    for (let i = 0, len = strokes.length; i < len; i++) {
        a_stroke = strokes[i];
        context.moveTo(a_stroke[0][0] * 2,a_stroke[0][1] * 2)
        for (let j = 1, len = a_stroke.length; j < len; j++){
            context.lineTo(a_stroke[j][0] * 2, a_stroke[j][1] * 2);
            context.stroke();
        }
    }
}

function read_strokes(){
    var fs = require('fs');
    strokes = [];
    fs.readFile('Json/Curr_Stroke.json','utf-8', function (err,data) {
        if (err) throw err;
        appConsole.log('Read Stroke!');
        strokes.push(JSON.parse(data));
    });
}

function activate_canvas(){
    appConsole.log("canvas activate")
    let isAllowDrawLine = false
    let nextstroke = []
    if (isAllowDraw){
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
}


