
const { ipcRenderer } = require('electron');

function activate_python(){
    //调用python
    var path = require('path');
    var pypath = path.join(__dirname,'python/test-client.py')
    const spawn = require('child_process').spawn;
    const py = spawn('python3', [pypath]);
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

function save_strokes(){
    var fs = require('fs');
    fs.writeFile('Json/Curr_Stroke.json', JSON.stringify(strokes), function (err) {
        if (err) throw err;
        appConsole.log('Saved Stroke!');
    });
}

function activate_button(){
    var b1 = document.getElementById("b1");
    appConsole.log("init");
    b1.onclick = function(){
        appConsole.log("click");
        save_strokes()
        ipcRenderer.on('main-msg', (event, arg) => {
            appConsole.log("返回数据",arg) // prints 数据
            if (arg[9]=="N"){
                document.getElementById("notification").innerHTML="NO related item found. Command+R to reload and redraw"
            }
            else if (arg[9] == "c"){
                document.getElementById("notification").innerHTML="Connection Refused contact server manager to check server status."
            }
            else{
                document.getElementById("notification").innerHTML="Successfully generated, Wait for 1 sec and Command + R to show"
                activate_python()
            }
            
        })
        ipcRenderer.send('renderer-msg', strokes)
    }
}
