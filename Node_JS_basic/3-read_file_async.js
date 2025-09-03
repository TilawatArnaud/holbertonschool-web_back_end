const fs = require('fs');

function countStudents(path) {
  let students = 0;
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      }

      const lines = data.split('\n');

      for (let counter = 0; counter < lines.length; counter += 1) {
        if (lines[counter].length > 0) students += 1;
      }

      students -= 1;

      console.log(`Number of students: ${students}`);

      const classrooms = [];

      lines.slice(1).forEach((line) => {
        if (line.length === 0) return;
        const parts = line.split(',');
        const field = parts[3];

        if (field && !classrooms.includes(field)) {
          classrooms.push(field);
        }
      });
      const groupedStudents = {};
      classrooms.forEach((field) => {
        groupedStudents[field] = [];
      });
      lines.slice(1).forEach((line) => {
        if (line.length === 0) return;
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[3];
        groupedStudents[field].push(firstname);
      });
      classrooms.forEach((field) => {
        console.log(`Number of students in ${field}: ${groupedStudents[field].length}. List: ${groupedStudents[field].join(', ')}`);
      });
      return resolve();
    });
  });
}

module.exports = countStudents;
