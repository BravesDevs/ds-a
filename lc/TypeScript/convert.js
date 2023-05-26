function convert(s, numRows) {
    var placingIndex = getPlacingIndex(s.length, numRows);
    var stringMap = {};
    // Initializing default values
    for (var i = 1; i <= numRows; i++) {
        stringMap[i] = "";
    }
    for (var i = 0; i < s.length; i++) {
        stringMap[placingIndex[i]] += s[i];
    }
    return Object.keys(stringMap).map(function (key) { return stringMap[key]; }).join("");
    ;
}
function getPlacingIndex(strLength, numRows) {
    var placeKey = [];
    var reverse = false;
    var index = 1;
    placeKey.push(index);
    for (var i = 1; i < strLength; i++) {
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
