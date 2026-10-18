sentence = " Python is useful and Python is powerful."

def count_words(sentence):
    punctuation = ",?;.:/!_-'()"
    for char in punctuation:
        sentence = sentence.replace(char, "" )
        
    word = sentence.strip()
    normalize_word = word.lower()
    final_word = normalize_word.split()

    return final_word, len(final_word)

def count_char(sentence):
    word , _ = count_words(sentence)
    chars = []
    
    count = 0
    for char in word:
        for letters in char:
            chars.append(letters)
            count += 1
                  
    return chars,count

def count_vowels(sentence):
    vowels = ["a", "e", "i" , "o", "u"]
    chars, _ = count_char(sentence)
    
    vowel_letters = 0
    consonants_letters = 0
    
    for char in chars:
        if char in vowels:
            vowel_letters += 1
        else:
            consonants_letters += 1
            
               
    return vowel_letters,consonants_letters
        
def longest_word(sentence):
    words , _ = count_words(sentence)
    
    longest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
            
    return longest
        
def repeated_words(sentence):
    words , _ = count_words(sentence)
    repeated = []
    
    for word in words:
        if words.count(word) > 1 and word not in repeated:
            repeated.append(word)
    
    return repeated
    
def display_analyzer(sentence):
    words, word_length = count_words(sentence)
    _, character_count = count_char(sentence) 
    vowel_count, consonant_count = count_vowels(sentence)
    word_longest = longest_word(sentence) 

    word_repeated = repeated_words(sentence)
  
    print(f"""
========== TEXT ANALYZER ==========
Words: {word_length} 
Characters : {character_count} 
Vowels: {vowel_count}
Consonants: {consonant_count}
Longest word: {word_longest}
Repeated words: {word_repeated}
          """)
    
display_analyzer(sentence)