def translate(sentence):
    words = {
        'esta': 'is',
        'la': 'the',
        'en': 'in',
        'gato': 'cat',
        'casa': 'house',
        'el': 'the'
        }
    trsl = (words.get(word, word) for word in sentence.split())
    res = " ".join(trsl)
    return res


print(translate("el gato esta en la casa"))