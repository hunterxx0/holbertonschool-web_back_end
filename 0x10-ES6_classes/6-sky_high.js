import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    /* eslint-disable no-underscore-dangle */
    super(sqft);
    this._floors = floors;
    /* eslint-disable no-underscore-dangle */
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
