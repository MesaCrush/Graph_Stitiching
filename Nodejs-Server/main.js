const express = require("express");
const server = express();
const routes = require("./routes");
server.use(express.json());

routes(server);

server.post('/',(req,res) =>{
    console.log("收到",req.body);
    res.status(201).send();
});

server.get('/',(req,res) =>{
    res.send("hello world");
});

server.put('/',(req,res) =>{
    console.log("收到请求内容",req.body)
    res.send();
});

server.listen(6199,()=>{
    console.log("获取数据成功");
});


