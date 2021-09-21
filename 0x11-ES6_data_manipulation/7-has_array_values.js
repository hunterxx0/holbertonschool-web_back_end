export default function hasValuesFromArray(nset, array) {
  return array.every((val) => nset.has(val));
}
