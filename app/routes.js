module.exports = function(app) {
    // Pass in express instance as app



    // Handle frontend requests
    app.get('/', function(req, res) {
        //res.send('hello world');
        res.sendfile('./public/views/index.html');
    });

    app.post('/', function(req, res){
        console.log(req);
        res.send('bar');
        /*
        var keyword = req.body;
        var spawn = require("child_process").spawn;
        var process = spawn('python',["youtube.py", keyword]);
        process.stdout.on('data', function (data){
            res.send(data);
        });
        */
    })

    app.get('/cats', function(req,res){
        res.send('I like cats');
    })
}