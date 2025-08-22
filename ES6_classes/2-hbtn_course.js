export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof (length) !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be a arrays of string');
    }
    if (!students.every(students => (typeof (students) === 'string'))) {
      throw new TypeError('Students must be a arrays of string');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof (name) !== 'string') {
      throw new TypeError('Name must be a string');
    }
    return this._name = name;
  }

  get length() {
    return this._length;
  }

  set length(length) {
    return this._length = length;
  }

  get students() {
    return this._students;
  }

  set students(students) {
    return this._students = students;
  }
}
