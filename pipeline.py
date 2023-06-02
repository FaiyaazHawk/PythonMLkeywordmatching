
def parse_to_string():
    import fitz

    pdf_path = "/home/faiyaaz/python/transformers/Resume_SoftwareEng-Intern.pdf"

    doc = fitz.open(pdf_path)

    data = []

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        data.append(text)

    result = " ".join(data)
    
    #print(type(result))
    return result

def filter_string(str):
    import nltk
    nltk.download("punkt")
    nltk.download("stopwords")
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    pattern = r'\w+'

    tokenizer = RegexpTokenizer(pattern)

    tokens = nltk.word_tokenize(str)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    #remove punctuation
    filtered_text = " ".join(filtered_tokens)
    
    return filtered_text


### references: https://www.sbert.net/docs/usage/semantic_textual_similarity.html
###             https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

#import sentencetransformer and instantiate model
def matchingEngine(resume_list, job_list):
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from sentence_transformers import util
    
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


    ## normalize the list to same length
    def fill_lists_with_empty_strings(list1, list2):
        max_length = max(len(list1), len(list2))

        # Fill list1 with empty strings
        while len(list1) < max_length:
            list1.append("")

        # Fill list2 with empty strings
        while len(list2) < max_length:
            list2.append("")

        return list1, list2

    fill_lists_with_empty_strings(resume_list,job_list)



    #encoding sentences to compare
    embeddingsResume = model.encode(resume_list, convert_to_tensor=True)
    embeddingsJob = model.encode(job_list, convert_to_tensor=True)



    #compute the similarity using a similarity matrix

    

    cosine_scores = util.cos_sim(embeddingsResume,embeddingsJob) #gives tensor with matchs



    ##find matched items in for each cos-sim with threshold greater than 0.7
    matched_items = []
    for i in range(cosine_scores.shape[0]):
        for j in range(cosine_scores.shape[1]):
            if cosine_scores[i,j] > 0.7: # magic number decided for match threshold
                value = np.round(cosine_scores[i,j].numpy(), decimals=4) #converting tensor value to int (to 4 decimal places)
                matched_items.append((resume_list[i], job_list[j], "Score: " + str(value)))


    ##printing result to terminal
    print(len(matched_items)/len(resume_list)*100)

    ### Notes: embeddings ignores capitalization so no need to normalize for that. 
    ### 0.7 seems to be the best value to match based on testing

#resume
result1 = parse_to_string()
resume_list = filter_string(result1)
#job
import os
job_path = "/home/faiyaaz/python/transformers/job_list.txt"
job_string = open(job_path, "r").read()

job_list = filter_string(job_string)

matchingEngine(resume_list.split(' '), job_list.split(' '))


