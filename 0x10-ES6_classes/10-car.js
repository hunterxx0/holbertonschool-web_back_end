export default class Car {
  constructor(brand, motor, color) {
    /* eslint-disable no-underscore-dangle */
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    /* eslint-disable no-underscore-dangle */
  }

  cloneCar() {
    const origin = this;
    return Object.assign(Object.create(Object.getPrototypeOf(origin)),
      { _brand: undefined, _motor: undefined, _color: undefined });
  }
}
