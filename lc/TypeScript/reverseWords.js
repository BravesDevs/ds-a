function reverseWords(s) {
    var res = "";
    var strArr = s.trim().split(" ").filter(Boolean).reverse().join(" ");
    console.log(strArr);
    return res;
}
;
console.log(reverseWords("  hello world  "));
