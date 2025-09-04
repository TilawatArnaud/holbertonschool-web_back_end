import readDatabase from '../utils';

export default class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const database = process.argv[2];
      const fields = await readDatabase(database);
      let output = 'This is the list of our students\n';
      const sortedFields = Object.keys(fields).sort(
        (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
      );

      sortedFields.forEach((field) => {
        output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });
      res.status(200).send(output.trim());
    } catch (err) {
      res.status(500).send(err.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    try {
      const { major } = req.params;
      if (!['CS', 'SWE'].includes(major)) {
        res.status(500).send('Major parameter must be CS or SWE');
        return;
      }
      const database = process.argv[2];
      const fields = await readDatabase(database);
      const students = fields[major] || [];

      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (err) {
      res.status(500).send(err.message);
    }
  }
}
