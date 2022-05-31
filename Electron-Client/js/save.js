function activate_python_save(){
    //调用python
    var path = require('path');
    var pypath = path.join(__dirname,'python/convert.py')
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
