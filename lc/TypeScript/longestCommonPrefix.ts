function longestCommonPrefix(strs: string[]): string {
  let res = "";
  if (strs.length === 0) return res;

  const minLengthStr = getMinimumLengthStrings(strs);
  for (let i = 0; i < minLengthStr.length; i++) {
    const char = minLengthStr[i];
    if (strs.every((str) => str[i] === char)) {
      res += char;
    } else {
      break;
    }
  }

  return res;
}

function getMinimumLengthStrings(strings: string[]): string {
  if (strings.length === 0) {
    return "";
  }

  const minLength = strings.reduce((min, str) => {
    return str.length < min ? str.length : min;
  }, strings[0].length);

  const minLengthStrings = strings.filter((str) => str.length === minLength);

  return minLengthStrings.length > 0 ? minLengthStrings[0] : "";
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]))