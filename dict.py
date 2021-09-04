from PyDictionary import PyDictionary

dictionary = PyDictionary()  # A Dictionary object to get meanings


def get_meaning(word):
    """Input: Word (Word to find the meaning)
    Output : Meaning of the word (If the word is valid, else returns False)"""
    meaning = dictionary.meaning(word, disable_errors=True)  # Meaning of the word
    # It returns False of not valid word
    if meaning:  # If meaning is a Truthy value
        word_meaning = """"""
        for type_of_word in meaning.keys():  # Type_of_word is the figure of speech
            # Iterates over the different word types of that word
            word_meaning += type_of_word + ":\n"
            for idx, meaning_of_word in enumerate(meaning[type_of_word]):
                # Iterates over the meaning of the word, as well as the index
                word_meaning += str(idx + 1) + ". " + meaning_of_word + "\n"
                # the idx+1 is to number the meanings. i.e a word can have many
                # meanings, it is to number those (+1 because index starts with 0)
            word_meaning += "\n\n"
        return word_meaning  # Returns the meaning
    else:
        return False
