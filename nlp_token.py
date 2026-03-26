print("importing libraries---------------\n")

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

print("\n ---NLTK Tokenizer--- ")
user_input = input("Enter the text you want to tokenize: ")

tokens = word_tokenize(user_input)
print(f"Tokens: {tokens}\n")

stop_words = set(stopwords.words('english'))
filtered_text = [w for w in tokens if not w.lower() in stop_words]

print(f"Cleaned text: {filtered_text}\n")

tagged_tokens = nltk.pos_tag(tokens)

print("\n -- POS TAGS --\n")
print(tagged_tokens)

