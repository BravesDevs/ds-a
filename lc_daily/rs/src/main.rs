fn main() {
    let sentence = "i love eating burger".to_string();
    let search_word = "burg".to_string();
    let result = is_prefix_of_word(sentence, search_word);
    println!("{}", result);
}



fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
    let mut count = 0;
    let mut word = String::new();
    for c in sentence.chars() {
        if c == ' ' {
            count += 1;
            if word.starts_with(&search_word) {
                return count;
            }
            word.clear();
        } else {
            word.push(c);
        }
    }
    count += 1;
    if word.starts_with(&search_word) {
        return count;
    }
    -1
}