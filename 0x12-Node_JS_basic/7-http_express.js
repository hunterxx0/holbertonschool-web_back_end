const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.listen(1245);
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', (req, res) => {
  countStudents(process.argv[2])
    .then((data) => {
      const dt = `This is the list of our students\n${data}`;
      res.end(dt);
    })
    .catch((error) => {
      res.end(`This is the list of our students\n${error.message}`);
    });
});

module.exports = app;
