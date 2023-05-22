import nltk
from nltk import FreqDist
from nltk import ngrams
from nltk.corpus import stopwords
from bidi.algorithm import get_display

stop_words = stopwords.words('english')

with open ("requiers.txt") as file:
    text = file.readlines()
    text = "".join(text).lower()
    tokens = nltk.word_tokenize(text)
    new_text = nltk.Text(tokens)
    clean_text = [word for word in tokens if word.isalnum() and word not in stop_words]
    clean_text2 = [word[::-1] for word in clean_text if word.isalpha()]
    print(clean_text)
    frequency = FreqDist(clean_text)
    print(frequency)
    # print(frequency.most_common(50), '\n')
    # output = str(new_text.collocations())
    # print(output)
    # print(tokens)