export default class Airport {
  constructor(name, code) {
    /* eslint-disable no-underscore-dangle */
    this._code = code;
    this._name = name;
    /* eslint-disable no-underscore-dangle */
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
