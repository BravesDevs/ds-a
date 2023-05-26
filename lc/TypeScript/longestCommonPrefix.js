function longestCommonPrefix(strs) {
    var res = "";
    if (strs.length === 0)
        return res;
    var minLengthStr = getMinimumLengthStrings(strs);
    var _loop_1 = function (i) {
        var char = minLengthStr[i];
        if (strs.every(function (str) { return str[i] === char; })) {
            res += char;
        }
        else {
            return "break";
        }
    };
    for (var i = 0; i < minLengthStr.length; i++) {
        var state_1 = _loop_1(i);
        if (state_1 === "break")
            break;
    }
    return res;
}
function getMinimumLengthStrings(strings) {
    if (strings.length === 0) {
        return "";
    }
    var minLength = strings.reduce(function (min, str) {
        return str.length < min ? str.length : min;
    }, strings[0].length);
    var minLengthStrings = strings.filter(function (str) { return str.length === minLength; });
    return minLengthStrings.length > 0 ? minLengthStrings[0] : "";
}
console.log(longestCommonPrefix(["flower", "flow", "flight"]));
