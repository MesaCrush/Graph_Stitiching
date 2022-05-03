const { app, BrowserWindow,ipcMain } = require('electron')
const send_Json_to_Server = require('./communication')

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
    if (arg == "#Reflash_Request"){
        console.log("reload request get")
        win.loadFile('index.html')
    }
    else{
        send_Json_to_Server(event,arg)
    }
})



