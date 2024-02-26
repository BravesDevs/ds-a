function lengthOfLastWord(s:string):number{
    return s.trim().split('').pop().length
}

console.log(lengthOfLastWord("   fly me   to   the moon  "));