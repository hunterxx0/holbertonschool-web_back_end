export default function cleanSet(nset, startString) {
  let res = '';

  if (!startString || !startString.length) {
    return res;
  }

  for (const str of nset) {
    if (str && str.startsWith(startString)) {

      if (res.length) {
        res += '-';
      }

      res += str.replace(
        startString,
        '',
        );
    }
  }

  return res;
}
