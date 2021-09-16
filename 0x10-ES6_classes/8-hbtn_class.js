export default class Currency {
  constructor(size, location) {
    /* eslint-disable no-underscore-dangle */
    this._size = size;
    this._location = location;
    /* eslint-disable no-underscore-dangle */
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this._location;
    if (hint === 'number') return this._size;
    return;
  }
}
