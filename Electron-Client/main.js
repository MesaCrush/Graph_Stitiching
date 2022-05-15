const { app, BrowserWindow,ipcMain } = require('electron')
const send_Json_to_Server_ver1 = require('./send_Json_ver1')
const send_Json_to_Server_ver2 = require('./send_Json_ver2')

//生成主屏幕
let win  = null;
const createWindow = () => {
    const win = new BrowserWindow({
      width: 1000,
      height: 800,
      webPreferences: { // 允许使用node
        nodeIntegration: true, 
        contextIsolation: false  
      }
    })
  
    win.loadFile('index.html')
}
app.whenReady().then(() => {
    createWindow()
})
app.on('window-all-closed', () => {
    win = null
    app.quit()
})


// 监听渲染进行发送的消息
ipcMain.on('renderer-msg', (event, arg) => {
    arg = JSON.parse(arg)
    if (arg["ver"] == "#Reflash_Request"){
        console.log("reload request get")
        win.loadFile('index.html')
    }
    else if (arg["ver"] == 1){
        console.log("ver1 active");
        console.log(arg["text"]);
        send_Json_to_Server_ver1(event,arg["text"]);
    }
    else{
        console.log("ver2 active");
        console.log(arg);
        send_Json_to_Server_ver2(event,arg);
    }
})



