""" 
Helper function for File, List and String

"""
def get_words_from_file(file_path):
    words = []
    with open(file_path) as fo:
        for word in fo:
            words.append(word)
    return set(words)


def has_word_in_text(sentence, match_words):
    return any(word.lower() in sentence.lower().split() for word in match_words)