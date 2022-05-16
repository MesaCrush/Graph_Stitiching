const express = require("express");
var route = express.Router()


route.post('/',(req,res) =>{
    console.log("收到post",req.body);
    var fs = require('fs');
    fs.writeFile('temp/temp.json', JSON.stringify(req.body), function (err) {
        if (err) throw err;
        console.log('Saved!');
    });
    
    const spawn = require('child_process').spawn;
    const py = spawn('python3', ['./python/ver1.py']);
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
        res.status(201).send(JSON.stringify({"text":output}));
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