export default function updateUniqueItems(pmap) {
  /* eslint-disable curly*/
  /* eslint-disable no-magic-numbers*/
  /* eslint-disable function-call-argument-newline*/

  if (!(pmap instanceof Map)) throw Error('Cannot process');
  pmap.forEach((value, key) => {
    if (value === 1) pmap.set(key, 100);
  });
}
