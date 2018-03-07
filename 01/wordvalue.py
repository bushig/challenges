from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words_list = []
    with open(DICTIONARY) as f:
        word = f.readline()
        while word:
            words_list.append(word.strip())
            word = f.readline()
    return words_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        if letter != '-':
            score += LETTER_SCORES[letter.upper()]
    return score

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_score = 0
    best_word = ""
    for word in words:
        if calc_word_value(word) > max_score:
            best_word = word
            max_score = calc_word_value(word)
    return best_word

if __name__ == "__main__":
    pass # run unittests to validate
