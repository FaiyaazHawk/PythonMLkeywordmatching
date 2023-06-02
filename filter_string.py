def filter_string(str):
    import nltk
    from nltk.corpus import stopwords

    tokens = nltk.word_tokenize(str)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    #remove punctuation
    filtered_text = " ".join(filtered_tokens)

    print(filtered_text)
