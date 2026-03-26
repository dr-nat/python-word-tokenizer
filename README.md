# 🔍 Simple NLP Tokenizer (Web Edition)

An interactive Natural Language Processing (NLP) application built with **Python**, **NLTK**, and **Streamlit**. This project demonstrates a complete text-processing pipeline—from raw user input to structured grammatical analysis—accessible via a modern web interface.

---

## 🚀 Features
* **Web Interface:** A clean, reactive UI for real-time text analysis.
* **Tokenization:** Breaks down complex sentences into individual linguistic units.
* **Stop-Word Filtering:** Removes high-frequency "noise" words to isolate core meaning.
* **POS Tagging:** Automatically categorizes words into Parts of Speech (Nouns, Verbs, etc.).
* **Interactive Tabs:** Organized view of Raw Tokens, Cleaned Text, and POS Tags.

---

## 📚 Library & Dependency Breakdown

### **1. NLTK (Natural Language Toolkit)**
The "engine" of the project. It is the leading platform for building Python programs to work with human language data.
* **`word_tokenize`**: Uses the Punkt algorithm to split text based on punctuation and language rules.
* **`stopwords`**: A pre-compiled list of 179 English words (like "the", "is", "at") used to filter out non-essential data.
* **`pos_tag`**: A pre-trained Perceptron Tagger that assigns grammatical labels based on word context.

### **2. Streamlit**
The "bridge" between Python and the Web.
* It turns Python scripts into shareable web apps in minutes.
* Handles the **Frontend** (UI components like buttons and text areas) and the **Backend** (executing the Python logic) in a single reactive loop.

### **3. Pandas**
Used to structure the POS Tag results into a clean, readable table format within the web app.

---

## 🛠️ Installation & Execution

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/python_tokenizer.git](https://github.com/your-username/python_tokenizer.git)
    cd python_tokenizer
    ```

2.  **Activate Virtual Environment:**
    ```bash
    source myvenv/bin/activate
    ```

3.  **Install Required Packages:**
    ```bash
    pip install nltk streamlit pandas
    ```

4.  **Launch the Web App:**
    ```bash
    streamlit run app.py
    ```

---

## 🏷️ POS Tag Reference (Penn Treebank)

| Tag | Description |
| :--- | :--- |
| **NN** | Noun, singular |
| **VB / VBP** | Verb (Base form / Present) |
| **JJ** | Adjective |
| **PRP** | Personal Pronoun |
| **IN** | Preposition or Conjunction |
| **DT** | Determiner |

---

## 📖 Project Defense: Why this Architecture?

* **Modular Design:** Separating the NLP logic from the UI allows for easier testing and scaling.
* **Python-Native Frontend:** Using Streamlit ensures the project remains lightweight and focused on data processing rather than heavy JavaScript development.
* **Educational Transparency:** NLTK was chosen over "black-box" alternatives (like spaCy) specifically to demonstrate the granular steps of the NLP pipeline.
