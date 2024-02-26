function isPalindrome(s: string): boolean {
  let str = s
    .trim()
    .replace(/[^a-zA-Z0-9]/g, "")
    .replace(/ /g, "")
    .toLowerCase();

  console.log("Str ->", str);
  let splitString = str.split("");
  let reverseStringArray = splitString.reverse();
  let joinArray = reverseStringArray.join("");
  return joinArray == str;
}

console.log(isPalindrome("0P"));
