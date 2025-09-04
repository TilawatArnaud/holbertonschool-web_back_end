const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    let output = '';
    const originalConsoleLog = console.log;
    console.log = (msg) => { output += `${msg}\n`; };

    countStudents(database)
      .then(() => {
        console.log = originalConsoleLog;
        res.end(`This is the list of our students\n${output}`);
      })
      .catch(() => {
        console.log = originalConsoleLog;
        res.end('This is the list of our students\nCannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
