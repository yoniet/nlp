from tracemalloc import stop
import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk import ngrams

stop_words = stopwords.words('english')
stop_words.append('в')
# print(type(stop_words))

with open("text_1.txt", encoding="utf-8") as file:
    text = file.readlines()
    text = "".join(text).lower()
    tokens = nltk.word_tokenize(text)
    new_text = nltk.Text(tokens)
    clean_text = [word for word in tokens if word.isalnum() and word not in stop_words]
    # print(clean_text)
    
    frequency = FreqDist(clean_text)
    
    print(frequency.most_common(50), '\n')
    # Two gram
    new_text.collocations()
    n = 3
    new_text = "".join(new_text)
    bigrams = ngrams(new_text.split(), n)
    for each in bigrams:
        print(each)
        
    # clean_text2 = [word for word in clean_text if word not in stop_words]
    # frequency = FreqDist(clean_text2)
    # print(frequency.most_common(50), '\n')

    
    
    
    
    # new_text.concordance("skill")
    # print(new_text)
    # text.concordance("customer")
    
#     count = 0
#     for tok in tokens:
#         if "The" in tok:
#             count= count +1

# print(count)

