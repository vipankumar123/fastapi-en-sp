import nltk
from nltk.tokenize import sent_tokenize
from transformers import MarianMTModel, MarianTokenizer


# MarianMTModel

# Download the tokenizer and model
tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ROMANCE")
model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-ROMANCE")

def translate_english_to_spanish(input_text):
    # Data Cleaning
    cleaned_text = input_text.replace('\\n', ' ')
    cleaned_text = cleaned_text.replace('\n', '')
    cleaned_text = cleaned_text.replace(':', '')
    cleaned_text = cleaned_text.replace("'", '')

    # Tokenize sentences using NLTK
    nltk.download('punkt')  # Make sure the punkt tokenizer is downloaded
    sentences = sent_tokenize(cleaned_text)

    # Translate sentences from English to Spanish using mbart50
    translated_sentences = []
    for sentence in sentences:
        inputs = tokenizer.encode(sentence, return_tensors="pt", max_length=1024, truncation=True)
        translated = model.generate(inputs, max_length=1024, num_beams=4, no_repeat_ngram_size=3, early_stopping=True)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        translated_sentences.append(translated_text)

    # Join translated sentences and remove '\r' characters
    translated_text = " ".join(translated_sentences).replace('\r', '')

    return translated_text
