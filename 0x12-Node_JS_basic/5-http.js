const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }
  if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((data) => {
        const dt = `This is the list of our students\n${data}`;
        res.end(dt);
      })
      .catch((error) => {
        res.end(error.message);
      });
  }
});

app.listen(1245);

module.exports = app;
