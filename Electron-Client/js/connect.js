
const { ipcRenderer } = require('electron');

function activate_python_main(){
    //调用python
    var path = require('path');
    var pypath = path.join(__dirname,'python/test-client.py')
    const spawn = require('child_process').spawn;
    const py = spawn('python', [pypath]);
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

function sentinfo(ver){
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
                activate_python_main()
            }
            
        })
        var info = {"text":strokes,"ver":ver};
        if (ver == 2){
            //handle none selected needed !!!!!!
            if (x_start > x_end){
                var x_temp = x_start;
                x_start = x_end;
                x_end = x_temp;
            }
            if (y_start > y_end){
                var y_temp = y_start;
                y_start = y_end;
                y_end = y_temp;
            }
            info["select_x"] = x_start/2;
            info["select_y"] = y_start/2;
            info["select_x_dist"] = (x_end-x_start)/2;
            info["select_y_dist"] = (y_end-y_start)/2;
        }
        ipcRenderer.send('renderer-msg', JSON.stringify(info))
}

function activate_send(){
    var b4 = document.getElementById("b4");
    var b3 = document.getElementById("b3");
    appConsole.log("connect ready to used");
    b4.onclick = function(){sentinfo(1)}
    b3.onclick = function(){sentinfo(2)}
}
