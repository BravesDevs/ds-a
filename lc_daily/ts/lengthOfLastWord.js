function lengthOfLastWord(s) {
    var word = s.trim().split(' ').pop();
    console.log(word);
    return word.length;
}
console.log(lengthOfLastWord("   fly me   to   the moon  "));
