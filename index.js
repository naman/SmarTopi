var express = require('express'),
    app = express();
	fs = require('fs');

app.get('/list', function (req, res) {
	fs.readFile('list.json', 'utf8', function (err,data) {
	  if (err) {
	    return console.log(err);
	  }
	res.send(data);
	});
});

app.listen(8080, function () {
  console.log('listening on port 8080...');
});
