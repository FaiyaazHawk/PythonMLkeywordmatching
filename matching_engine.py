### references: https://www.sbert.net/docs/usage/semantic_textual_similarity.html
###             https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

#import sentencetransformer and instantiate model
import spacy

def matchingEngine(resume_list, job_list):
    
    nlp = spacy.load("en_core_web_lg")
   
    resume = nlp(resume_list)
    job = nlp(job_list)

    result = resume.similarity(job) *100

    print('The match between the resume and the job is {result}%'.format(result=result))
    
    