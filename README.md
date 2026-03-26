# Simple Natural Language Processing (NLP) Tokenizer

An interactive Python-based tool designed to demonstrate the core stages of a Natural Language Processing pipeline. This utility uses the **Natural Language Toolkit (NLTK)** to transform raw text into structured data through tokenization, filtering, and Part-of-Speech (POS) tagging.

---

## 🚀 Features
* **Dynamic User Input:** Process any sentence or paragraph in real-time.
* **Advanced Tokenization:** Uses NLTK's `punkt` models to intelligently handle punctuation and contractions.
* **Stop-Word Filtering:** Automatically removes non-essential "filler" words (e.g., "is", "the", "at") to highlight meaningful content.
* **POS Tagging:** Identifies grammatical categories (Nouns, Verbs, Adjectives) using the `averaged_perceptron_tagger`.

---

## 📚 Core Libraries & Dependencies

This project relies on the following libraries and data packages:

### **Libraries**
* **[NLTK (Natural Language Toolkit)](https://www.nltk.org/):** The primary library for NLP in Python, providing the modules for splitting text and identifying grammatical structures.

### **NLTK Data Packages**
Upon the first execution, the script automatically downloads:
* `punkt_tab`: Required for the word tokenizer to identify word boundaries.
* `stopwords`: A corpus of common words used for the filtering stage.
* `averaged_perceptron_tagger_eng`: The pre-trained model used to assign POS tags.

---

## 🏷️ Understanding POS Tags

The script utilizes the **Penn Treebank Tagset**. Below is a guide to the tags you will see in the output:

| Tag | Description | Example from Project |
| :--- | :--- | :--- |
| **NN / NNP** | Noun (Singular / Proper) | *student, software, David* |
| **VB / VBP** | Verb (Base form / Present) | *play, am, eat* |
| **JJ** | Adjective | *ambitious, green, smart* |
| **RB** | Adverb | *quickly, very, much* |
| **PRP / PRP$** | Pronoun (Personal / Possessive) | *we, I / my, your* |
| **IN** | Preposition or Conjunction | *with, in, for* |
| **DT** | Determiner | *the, a, this* |

---

## 🛠️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/python_tokenizer.git](https://github.com/your-username/python_tokenizer.git)
    cd python_tokenizer
    ```

2.  **Set up a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv myvenv
    source myvenv/bin/activate
    ```

3.  **Install NLTK:**
    ```bash
    pip install nltk
    ```

4.  **Run the Application:**
    ```bash
    python3 nlp_token.py
    ```

---

## 📖 Processing Logic

The script follows a standard NLP pipeline:
1.  **Input:** Captures a string from the user.
2.  **Tokenization:** Splits the string into a list of individual words and punctuation.
3.  **Stop-Word Removal:** Compares tokens against a list of common English words and removes them to leave only "content" words.
4.  **Grammatical Tagging:** Analyzes the remaining words to determine their linguistic role (Noun, Verb, etc.) based on the sentence context.
