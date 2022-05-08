var x_start,y_start,x_end,y_end;
function activate_select(){
    if (!isAllowDraw){
        appConsole.log("select ready to used");
        theCanvas.onmousedown = function(e) {
            appConsole.log("select start");
            let ele = windowToCanvas(theCanvas, e.clientX, e.clientY);
            x_start = ele.x;
            y_start = ele.y;
        }
        theCanvas.onmouseup = function(e) {
            let ele = windowToCanvas(theCanvas, e.clientX, e.clientY)
            x_end = ele.x;
            y_end = ele.y;
            appConsole.log(" x_start,x_end,y_start,y_end", x_start,x_end,y_start,y_end);
            context.rect(x_start,y_start,x_end-x_start,y_end-y_start);
            context.stroke();
        }
    }

}
