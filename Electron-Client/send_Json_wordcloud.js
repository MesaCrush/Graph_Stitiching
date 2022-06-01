const { net } = require('electron')


function send_Json_to_Server_word(event,arg){
    var postData = JSON.stringify(arg);
    const requestw = net.request({
        method: 'POST',
        protocol: 'http:',
        hostname: '127.0.0.1',
        port: 6199,
        path: '/wordcloud',
        headers: {
            // 这里要将content-type改成这种提交form表单时使用的格式
            'Content-Type': 'application/json'
        }
    });
    
    requestw.on('response',(response)=>{  //监听响应
        console.log("Status Code:" + response.statusCode);  //返回状态码
        response.on('data',(chuck)=>{  //获取返回数据
        })
        //监听结束
    })
    requestw.write(postData);
    requestw.end();
}

module.exports = send_Json_to_Server_word;