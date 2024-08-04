import pandas as pd
import spacy
from extract_nltk import extract_entities_nltk
from extract_spacy import extract_entities_spacy
from compare_results import compare_entities

# Load the dataset
dataset_path = 'bbc_news_dataset.csv'
df = pd.read_csv(dataset_path)

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Process multiple articles
for index, row in df.iterrows():
    article_text = row['Description']
    
    print(f"\nArticle {index + 1}:")
    print("Title:", row['Title'])
    print("Date:", f"{row['Year']}-{row['Month']:02d}-{row['Day']:02d}")
    print("Description:", article_text)

    # Extract entities using both approaches
    nltk_entities = extract_entities_nltk(article_text)
    spacy_entities = extract_entities_spacy(article_text)

    print("\nNLTK Named Entities:")
    for entity in nltk_entities:
        print(entity)

    print("\nSpaCy Named Entities:")
    for entity in spacy_entities:
        print(entity)

    # Comparison
    common_entities, nltk_only, spacy_only = compare_entities(nltk_entities, spacy_entities)

    print("\nCommon Entities:", common_entities)
    print("Entities only in NLTK:", nltk_only)
    print("Entities only in SpaCy:", spacy_only)

    print("\n" + "="*50)

# Discussion
discussion = """
Discussion:
1. **Differences in Results**: 
   - NLTK often captures a broader range of entity types, including more fine-grained categories.
   - SpaCy, being machine learning-based, is generally more accurate and can recognize a wider range of named entities.

2. **Limitations**:
   - NLTK's rule-based approach may miss some entities or incorrectly classify them due to reliance on manually crafted rules.
   - SpaCy might also have inaccuracies but typically performs better with contextual understanding.

3. **Observations**:
   - SpaCy's model can recognize entities like dates, events, and more specific organization names, while NLTK might categorize them under broader tags.
   - The short and sometimes fragmented nature of the descriptions in this dataset might affect the accuracy of both NER systems.
"""

print(discussion)