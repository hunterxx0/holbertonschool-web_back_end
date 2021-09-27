const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }
      const lines = data.toString().split('\n').filter((n) => n);
      let res = (`Number of students: ${lines.length - 1}\n`);
      console.log(res.slice(0, -1));
      const dct = {};
      let key = null;
      let std = null;
      for (let line = 1; line < lines.length; line += 1) {
        std = lines[line].split(',');
        if (std[3]) {
          key = dct[std[3]];
          if (key) {
            key.push(std[0]);
          } else {
            dct[std[3]] = [std[0]];
          }
        }
      }
      for (const [key, value] of Object.entries(dct)) {
        console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
        res += (`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}\n`);
      }
      resolve(res);
    });
  });
}

module.exports = countStudents;
