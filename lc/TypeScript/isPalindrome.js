function isPalindrome(s) {
    var str = s
        .trim()
        .replace(/[^a-zA-Z0-9]/g, "")
        .replace(/ /g, "")
        .toLowerCase();
    console.log("Str ->", str);
    var splitString = str.split("");
    var reverseStringArray = splitString.reverse();
    var joinArray = reverseStringArray.join("");
    return joinArray == str;
}
console.log(isPalindrome("0P"));
