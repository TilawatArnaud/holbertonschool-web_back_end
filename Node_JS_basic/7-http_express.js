const express = require('express');
const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2];

const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  const header = 'This is the list of our students\n';
  let output = '';

  const originalLog = console.log;
  console.log = (msg) => { output += `${msg}\n`; };

  countStudents(databasePath)
    .then(() => {
      console.log = originalLog;
      res.send(header + output.trim());
    })
    .catch(() => {
      console.log = originalLog;
      // Affiche toujours le header en première ligne
      res.send(`${header}Cannot load the database`);
    });
});

app.listen(1245);

module.exports = app;
