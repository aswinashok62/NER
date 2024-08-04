## Setup

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Download the SpaCy model:
    ```sh
    python -m spacy download en_core_web_sm
    ```

3. Run the NER comparison script:
    ```sh
    python scripts/nlp_ner_comparison.py
    ```

## Notes

- The `sample_texts.txt` file contains example texts for testing (if used).
- Adjust the text in the script as needed.