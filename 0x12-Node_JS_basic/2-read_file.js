const fs = require('fs');

function countStudents(path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      throw Error('Cannot load the database');
    }
    const lines = data.split('\n');
    console.log(`Number of students: ${lines.length - 1}`);
    const dct = {};
    for (let line = 1; line < lines.length; line += 1) {
      const std = lines[line].split(',');
      if (std[3]) {
        const key = dct[std[3]];
        if (key) {
          key.push(std[0]);
        }
      } else {
        dct[std[3]] = [std[0]];
      }
    }
    for (const [key, value] of Object.entries(dct)) {
      console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
    }
  });
}

module.exports = countStudents;
