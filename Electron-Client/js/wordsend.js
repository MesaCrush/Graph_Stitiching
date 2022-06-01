function activate_wordcloud_verify(){
    //调用python
    var path = require('path');
    var pypath = path.join(__dirname,'python/wordmap.py')
    const spawn = require('child_process').spawn;
    var sentense = document.getElementById('wordcloud_s').value;
    var notification = document.getElementById('notification');
    const py = spawn('python', [pypath,sentense]);
    let output = "";
    py.stdout.on("data", (data) => {
        output += data.toString();
    });
    py.stderr.on("data", (data) => {
        output += data.toString();
    });
    py.stdout.on("close", () => {
        appConsole.log(output)  
        if (output[0] == "Y"){
            notification.innerHTML = "update request sent";
        }
        else if (output[0] == "N"){
            notification.innerHTML = "no target word enter. you can try [animal] [verb] [none]";
        }
        else{
            notification.innerHTML = "you have enter one target word: " + output;
        }
    });


}

function activate_wordcloud_sent(){
    var message = document.getElementById('notification').textContent;
    var sentense = document.getElementById('wordcloud_s').value;
    //appConsole.log(message)
    if ( message == "update request sent"){
        appConsole.log("wordcloud sent")
        ipcRenderer.on('main-msg', (event, arg) => {
            appConsole.log("返回数据",arg) 
        })
        var info = {"text":sentense,"ver":"wordcloud"};
        ipcRenderer.send('renderer-msg', JSON.stringify(info))
    }
}