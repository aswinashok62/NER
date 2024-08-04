# extract_nltk.py
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_entities_nltk(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    ne_tree = ne_chunk(pos_tags)
    iob_tags = tree2conlltags(ne_tree)
    
    entities = []
    for word, pos, tag in iob_tags:
        if tag != 'O':
            entities.append((word, tag))
    
    return entities