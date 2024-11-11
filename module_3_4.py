def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        if root_word in word.lower() or word in root_word:
            same_words.append(word)

        # return same_words
    print(same_words)

single_root_words('ЗА', 'АзАзелло','ЗАбор ' , 'запас', 'узник', 'пузатый')




