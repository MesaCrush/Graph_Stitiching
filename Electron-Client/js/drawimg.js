function read_return_strokes(index){
    var fs = require('fs');
    strokes.splice(0, strokes.length);
    var return_data;
    return_data = fs.readFileSync('Json/Recieve.json',"utf8");   
    return_data = JSON.parse(return_data)
    var data_key = "img".concat(index.toString())
    appConsole.log(data_key)
    return_data = return_data[data_key]
    appConsole.log(return_data)  
    for (let i = 0, len = return_data.length; i < len; i++){
        strokes.push(return_data[i]);
    }
    appConsole.log(strokes)
}

function drawimg(index){
    appConsole.log("imgdraw_clicked")
    read_return_strokes(index)
    appConsole.log(strokes)
    redraw()
}


function activate_imgdraw(){
    var img1 = document.getElementById("img1");
    img1.onclick = function(e){drawimg(1);}
    var img2 = document.getElementById("img2");
    img2.onclick = function(e){drawimg(2);}
    var img3 = document.getElementById("img3");
    img3.onclick = function(e){drawimg(3);}
    var img4 = document.getElementById("img4");
    img4.onclick = function(e){drawimg(4);}
    var img5 = document.getElementById("img5");
    img5.onclick = function(e){drawimg(5);}
    var img6 = document.getElementById("img6");
    img6.onclick = function(e){drawimg(6);}
}