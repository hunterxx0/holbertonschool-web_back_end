const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path);
  } catch (error) {
    throw Error('Cannot load the database');
  }
  const lines = data.toString().split('\n').filter((n) => n);
  console.log(`Number of students: ${lines.length - 1}`);
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
  }
}

module.exports = countStudents;
