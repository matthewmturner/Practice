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


s = "The bill came to five dollars."
print(create_word_cloud(s))
s.split()
