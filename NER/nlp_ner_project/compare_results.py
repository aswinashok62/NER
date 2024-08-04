# compare_results.py
def compare_entities(nltk_entities, spacy_entities):
    nltk_set = set(nltk_entities)
    spacy_set = set(spacy_entities)
    
    common_entities = nltk_set.intersection(spacy_set)
    nltk_only = nltk_set - spacy_set
    spacy_only = spacy_set - nltk_set
    
    return common_entities, nltk_only, spacy_only