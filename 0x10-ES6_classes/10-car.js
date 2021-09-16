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
    return new (Object.getPrototypeOf(this.constructor))(undefined, undefined, undefined);
  }
}
