def create_word_cloud(sentence):

    word_cloud = dict()
    sentence_end = set([".", "!", "?"])
    punctuation = set([",", ":", "(", ")"])

    clean_sentence_chars = []
    end_of_sentence = False
    for char in sentence:
        if char in sentence_end:
            end_of_sentence = True
            clean_sentence_chars.append(" ")
        elif char in punctuation:
            next
        elif end_of_sentence == True:
            clean_sentence_chars.append(char.lower())
            end_of_sentence = False
        else:
            clean_sentence_chars.append(char)

    clean_words = "".join(clean_sentence_chars).split()

    for word in clean_words:
        word_ct = word_cloud.get(word, 0)
        word_cloud[word] = word_ct + 1

    return word_cloud


def word_cloud2(sentence):

    word_cloud = dict()
    sentence_end = set([".", "!", "?"])
    punctuation = set([",", ":", "(", ")"])

    current_word = ""
    new_sentence = False
    for i, char in enumerate(sentence):
        if (i == 0) or (new_sentence == True):
            current_word += char.lower()
            new_sentence = False
        elif char in punctuation:
            word_ct = word_cloud.get(current_word, 0)
            word_cloud[current_word] = word_ct + 1
            current_word = ""
            next
        elif (char in sentence_end) and (current_word != ""):
            word_ct = word_cloud.get(current_word, 0)
            word_cloud[current_word] = word_ct + 1
            current_word = ""
            new_sentence = True
            next
        elif (char == " ") and (current_word != ""):
            word_ct = word_cloud.get(current_word, 0)
            word_cloud[current_word] = word_ct + 1
            current_word = ""
        else:
            current_word += char

    return word_cloud


s = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
print(word_cloud2(s))
s.split()
