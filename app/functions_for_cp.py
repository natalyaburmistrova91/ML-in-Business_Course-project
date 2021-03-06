import re
from razdel import tokenize
import pymorphy2


morph = pymorphy2.MorphAnalyzer()

stopword_eng = []

with open('final_stop_words.txt') as f:
    stopword_eng += [w.strip() for w in f.readlines() if w]


def clean_text(text):
    '''
    очистка текста

    на выходе очищеный текст

    '''
    if not isinstance(text, str):
        text = str(text)

    text = text.lower()
    text = text.strip('\n').strip('\r').strip('\t')
    text = re.sub("-\s\r\n\|-\s\r\n|\r\n", '', str(text))
    text = re.sub("\|", ' ', str(text))
    text = re.sub("https?:\/\/\S+", '', str(text))
    text = re.sub("[0-9]|[-—.,:;_%©«»?*!@#№$^•·&()]|[+=]|[[]|[]]|[/]|", '', text)
    text = re.sub(r"\r\n\t|\n|\\s|\r\t|\\n", ' ', text)
    text = re.sub(r'[\xad]|[\s+]', ' ', text.strip())

    # tokens = list(tokenize(text))
    # words = [_.text for _ in tokens]
    # words = [w for w in words if w not in stopword_ru]

    # return " ".join(words)
    return text


cache = {}


def lemmatization(text):
    '''
    лемматизация
        [0] если зашел тип не `str` делаем его `str`
        [1] токенизация предложения через razdel
        [2] проверка есть ли в начале слова '-'
        [3] проверка токена с одного символа
        [4] проверка есть ли данное слово в кэше
        [5] лемматизация слова
        [6] проверка на стоп-слова

    на выходе лист отлемматизированых токенов
    '''

    # [0]
    if not isinstance(text, str):
        text = str(text)

    # [1]
    tokens = list(tokenize(text))
    words = [_.text for _ in tokens]

    words_lem = []
    for w in words:
        if w[0] == '-':  # [2]
            w = w[1:]
        if len(w) > 1:  # [3]
            if w in cache:  # [4]
                words_lem.append(cache[w])
            else:  # [5]
                temp_cach = cache[w] = morph.parse(w)[0].normal_form
                words_lem.append(temp_cach)

    words_lem_without_stopwords = [i for i in words_lem if not i in stopword_eng]  # [6]

    return words_lem_without_stopwords

