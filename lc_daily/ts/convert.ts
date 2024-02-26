function convert(s: string, numRows: number) {
  if(numRows==1){
    return s
  }
  let placingIndex = getPlacingIndex(s.length, numRows);
  let stringMap = {};

  // Initializing default values
  for (let i = 1; i <= numRows; i++) {
    stringMap[i] = "";
  }

  for (let i = 0; i < s.length; i++) {
    stringMap[placingIndex[i]] += s[i];
  }

  return Object.keys(stringMap).map((key) => stringMap[key]).join("");
}

function getPlacingIndex(strLength: number, numRows: number): number[] {
  let placeKey: number[] = [];
  let reverse = false;
  let index = 1;
  placeKey.push(index);
  for (let i = 1; i < strLength; i++) {
    // Increase index

    if (!reverse) {
      index += 1;
      placeKey.push(index);
      if (index == numRows) {
        reverse = true;
      }
      continue;
    }

    // Decrease index

    if (reverse) {
      index -= 1;
      placeKey.push(index);
      if (index == 1) {
        reverse = false;
      }
    }
    continue;
  }

  return placeKey;
}

console.log(convert("PAYPALISHIRING", 3));
