function read_layer(index){
    var fs = require('fs');
    layerStrokes.splice(0, layerStrokes.length);
    layer_data = fs.readFileSync('Json/Layer'+index+'.json','utf-8')
    layer_data = JSON.parse(layer_data);
    for (let i = 0, len = layer_data.length; i < len; i++){
        layerStrokes.push(layer_data[i]);
    }
    appConsole.log(layerStrokes)
}



function save_layer(index){
    var fs = require('fs');
    fs.writeFile('Json/Layer'+index+'.json', JSON.stringify(strokes), function (err) {
        if (err) throw err;
        appConsole.log('Saved layer!');
    });
}

function redrawlayer(){
    for (let i = 0, len = layerStrokes.length; i < len; i++) {
        var a_stroke = layerStrokes[i]
        appConsole.log(a_stroke);
        if (a_stroke.length == 0){
            continue;
        }
        context.moveTo(a_stroke[0][0] * 2,a_stroke[0][1] * 2)
        for (let j = 1, len = a_stroke.length; j < len; j++){
            context.lineTo(a_stroke[j][0] * 2, a_stroke[j][1] * 2);
            context.stroke();
        }
    }
}

function activate_python_once(filename){
    //调用python
    appConsole.log("active python");
    var path = require('path');
    var pypath = path.join(__dirname,'python/single_image.py');
    const spawn = require('child_process').spawn;
    const py = spawn('python', [pypath,filename]);
    let output = "";
    py.stdout.on("data", (data) => {
        output += data.toString();
    });
    py.stderr.on("data", (data) => {
        output += data.toString();
    });
    py.stdout.on("close", () => {
        appConsole.log(output);
    });
}