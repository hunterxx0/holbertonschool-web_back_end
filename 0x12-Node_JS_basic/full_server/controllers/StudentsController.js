const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((data, mess) => {
        response.status(200).send(mess);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (major === 'CS' || major === 'SWE') {
      readDatabase(process.argv[2])
        .then((data, _) => {
          if (data[major]) {
            response.send(`List: ${data[major]}`);
          } else {
            response.send('List: []');
          }
        })
        .catch((error) => {
          response.status(500).send(error.message);
        });
    } else {
      response.status(500).send('Major parameter must be CS or SWE');
    }
  }
}

module.exports = StudentsController;
