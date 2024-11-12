def single_root_words(root_word, *other_words):
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        if root_word in word.lower() or word in root_word.lower():
            same_words.append(word)

    return same_words
result = single_root_words('зА', 'АзАзелло', 'ЗАбор ','Замер', 'запас', 'узник', 'пузатый')
print(result)




# single_root_words('зА', 'АзАзелло','ЗАбор ' , 'запас', 'узаконенный', 'узник', 'пузатый')




