const express = require("express");
var route = express.Router()


route.post('/',(req,res) =>{
    console.log("收到post",req.body);
    const spawn = require('child_process').spawn;
    const py = spawn('python', ['./python/wordmap.py',req.body["text"]]);
    let output= "";
    let errormes = "";
    py.stdout.on("data", (data) => {
        output += data.toString().trim();
    });
    py.stderr.on("data", (data) => {
        errormes += data.toString();
    });
    py.stdout.on("close", () => {
        console.log(output);
        console.log("error: ",errormes);
        res.status(201).send(JSON.stringify({"text":output,"err":errormes}));
    });
    
});

route.get('/',(req,res) =>{
    res.send("get from post");
});

route.put('/',(req,res) =>{
    //暂时不重要
    res.send();
});


module.exports = route;