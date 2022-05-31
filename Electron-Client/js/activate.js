function activate_button(){
    var b2 = document.getElementById("b2");
    b2.onclick = function(){
        isAllowDraw = false;
        theCanvas.height = theCanvas.height;
        redraw()
        activate_canvas();
        activate_select();
    }
    var b1 = document.getElementById("b1");
    b1.onclick = function(){
        isAllowDraw = true;
        theCanvas.height = theCanvas.height;
        redraw();
        activate_canvas();
        activate_select();
    }
    var b5 = document.getElementById("b5");
    b5.onclick = function(){
        theCanvas.height = theCanvas.height;
        redraw(-1);
    }

    var b6 = document.getElementById("b6");
    b6.onclick = function(){
        appConsole.log('save & export!');
        activate_python_save();
    }

    var black = document.getElementById("black");
    black.onclick = function(){
        appConsole.log('black');
        color = "black"}

    var red = document.getElementById("red");
    red.onclick = function(){
        appConsole.log('red');
        color = "red"}

    var green = document.getElementById("green");
    green.onclick = function(){
        appConsole.log('green');
        color = "green"}
}



window.onload=function(){
    theCanvas = document.getElementById('theCanvas')
    context = theCanvas.getContext('2d')
    activate_canvas();
    activate_select();
    activate_button();
    activate_send();
    activate_imgdraw()
}