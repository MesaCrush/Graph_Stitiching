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
}



window.onload=function(){
    theCanvas = document.getElementById('theCanvas')
    context = theCanvas.getContext('2d')
    activate_canvas();
    activate_select();
    activate_button();
    activate_send();
}