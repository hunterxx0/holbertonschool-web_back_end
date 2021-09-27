const { express } = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const exp = express();

exp.get('/', AppController.getHome);
exp.get('/students', StudentsController.getAllStudents);
exp.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = exp;
