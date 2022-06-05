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

    var wordcloud_v = document.getElementById("wordcloud_v");
    wordcloud_v.onclick = function(){
        appConsole.log('wordcloud_v');
        activate_wordcloud_verify()
    }

    var wordcloud_b = document.getElementById("wordcloud_b");
    wordcloud_b.onclick = function(){
        appConsole.log('wordcloud_b');
        activate_wordcloud_sent()
    }

    var blayer1 = document.getElementById("blayer1");
    blayer1.onclick = function(){
        appConsole.log('blayer1');
        save_layer(1)
        activate_python_once("Layer1.json")
    }

    var slayer1 = document.getElementById("slayer1");
    slayer1.onclick = function(){
        appConsole.log('slayer1');
        read_layer(1);
        redrawlayer();
        
    }

    var blayer2 = document.getElementById("blayer2");
    blayer2.onclick = function(){
        appConsole.log('blayer2');
        save_layer(2)
        activate_python_once("Layer2.json")
    }

    var slayer2 = document.getElementById("slayer2");
    slayer2.onclick = function(){
        appConsole.log('slayer2');
        read_layer(2);
        redrawlayer();
        
    }

    var blayer3 = document.getElementById("blayer3");
    blayer3.onclick = function(){
        appConsole.log('blayer3');
        save_layer(3)
        activate_python_once("Layer3.json")
    }

    var slayer3 = document.getElementById("slayer3");
    slayer3.onclick = function(){
        appConsole.log('slayer3');
        read_layer(3);
        redrawlayer();
        
    }


}



window.onload=function(){
    theCanvas = document.getElementById('theCanvas')
    context = theCanvas.getContext('2d')
    activate_canvas();
    activate_select();
    activate_button();
    activate_send();
    activate_imgdraw();
    
}