import Car from './10-car';

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    /* eslint-disable no-underscore-dangle */
    super(brand, motor, color);
    this._range = range;
    /* eslint-disable no-underscore-dangle */
  }

  cloneCar() {
    return new (Object.getPrototypeOf(this.constructor))(undefined, undefined, undefined);
  }
}
