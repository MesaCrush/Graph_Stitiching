const version1 = require("./version1");
const version2 = require("./version2");

module.exports = (server)=>{
    server.use("/version1",version1);
    server.use("/version2",version2);
}