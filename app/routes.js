module.exports = function(app) {
    // Pass in express instance as app



    // Handle frontend requests
    app.get('/', function(req, res) {
        //res.send('hello world');
        res.sendfile('./public/views/index.html');
    });

    app.get('/cats', function(req,res){
        res.send('I like cats');
    })
}