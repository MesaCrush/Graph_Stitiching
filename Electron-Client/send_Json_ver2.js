const { net } = require('electron')


function send_Json_to_Server_ver2(event,arg){
    //console.log( JSON.stringify({"text":arg})) // print 图像json,  
    var postData = JSON.stringify(arg);
    const request1 = net.request({
        method: 'POST',
        protocol: 'http:',
        hostname: '127.0.0.1',
        port: 6199,
        path: '/version2',
        headers: {
            // 这里要将content-type改成这种提交form表单时使用的格式
            'Content-Type': 'application/json'
        }
    });
    
    request1.on('response',(response)=>{  //监听响应
        console.log("Status Code:" + response.statusCode);  //返回状态码
        response.on('data',(chuck)=>{  //获取返回数据
            //写Recieve.json
            var received_data = JSON.parse(chuck);
            console.log(received_data["text"][0]);
            var path = require('path');
            var fs = require('fs');
            var str = path.join(__dirname,'Json/Recieve.json')
            console.log(str)
            fs.writeFile(str, JSON.stringify(received_data), 'utf8', function (err) {
                if (err) throw err;
                console.log('Saved!');
            });
            let message = chuck.toString()
            event.reply('main-msg', message);  // 给渲染进程回复消息
            //console.log(chunk.toString());
        })
        //监听结束
    })
    request1.write(postData);
    request1.end();
}

module.exports = send_Json_to_Server_ver2;