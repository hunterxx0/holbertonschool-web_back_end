export default function appendToEachArrayValue(array, appendString) {
  for (let value of array) {
    const idx = array.indexOf(value);
    array[idx] = appendString + value;
  }

  return array;
}