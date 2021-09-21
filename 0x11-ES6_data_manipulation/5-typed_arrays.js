export default function createInt8TypedArray(length, position, value) {
  /* eslint-disable one-var*/
  /* eslint-disable no-magic-numbers*/
  if (position >= length || position < 0) {
    throw Error('Position outside range');
  }

  const buf = new ArrayBuffer(length);

  const dv = new DataView(
    buf,
    0,
    length,
    );

  dv.setInt8(
    position,
    value,
    );

return dv;

}