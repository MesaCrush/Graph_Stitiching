function read_return_strokes(){
    var fs = require('fs');
    strokes.splice(0, strokes.length);
    var return_data;
    return_data = fs.readFileSync('Json/Recieve.json',"utf8");   
    return_data = JSON.parse(return_data)
    return_data = return_data["text"]
    appConsole.log(return_data)  
    for (let i = 0, len = return_data.length; i < len; i++){
        strokes.push(return_data[i]);
    }
    appConsole.log(strokes)
}

function drawimg(index){
    appConsole.log("imgdraw_clicked")
    read_return_strokes()
    appConsole.log(strokes)
    redraw()
}


function activate_imgdraw(){
    var img1 = document.getElementById("img1");
    appConsole.log('imgdraw activate!');
    img1.onclick = function(e){drawimg(0);}
}