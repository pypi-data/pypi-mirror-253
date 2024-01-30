
def import_words(words: list):
    books = {
        '英语单词': {
            '所有单词': (所有单词 := []),
            '四级精选': (四级精选 := []),
            '六级精选': (六级精选 := []),
            '考研精选': (考研精选 := []),
            '雅思精选': (雅思精选 := []),
            '托福精选': (托福精选 := []),
            'GRE精选': (GRE精选 := []),
        }
    }
    for word in words:
        tag = word['tag']
        所有单词.append(word)
        if '四级' in tag: 四级精选.append(word)
        if '六级' in tag: 六级精选.append(word)
        if '考研' in tag: 考研精选.append(word)
        if '雅思' in tag: 雅思精选.append(word)
        if '托福' in tag: 托福精选.append(word)
        if 'rgb' in tag: GRE精选.append(word)
    return books