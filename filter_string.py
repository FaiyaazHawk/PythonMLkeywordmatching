import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer


def filter_string(str):
    #remove punctuation marks
    tokenizer = RegexpTokenizer(r'\w+')
    non_punc_list = tokenizer.tokenize(str)
    
    non_punc_str = " ".join(non_punc_list) #getting back a string for removing stopwords
    tokens = nltk.word_tokenize(non_punc_str)

    stop_words = set(stopwords.words("english"))

    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    
    filtered_string = " ".join(filtered_tokens)


    return filtered_string
