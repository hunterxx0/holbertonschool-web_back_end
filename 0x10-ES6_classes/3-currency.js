export default class Currency {
  constructor(code, name) {
    /* eslint-disable no-underscore-dangle */
    this._code = code;
    this._name = name;
    /* eslint-disable no-underscore-dangle */
  }

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(code) {
    this._code = code;
  }

  set name(name) {
    this._name = name;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
