import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
import pandas as pd

# Page Configuration
st.set_page_config(page_title="NLP Tokenizer", page_icon="🚀")

# Ensure NLTK data is available
@st.cache_resource
def download_nltk_data():
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger_eng')

download_nltk_data()

# UI Layout
st.title(" Simple NLP Tokenizer")
st.markdown("Enter text below to see the NLP pipeline in action.")

user_input = st.text_area("Input Text:", placeholder="e.g., My name is Lenny and I love systems programming.")
analyze_button = st.button("Analyze Text")

if analyze_button and user_input:
    # 1. Tokenization
    tokens = word_tokenize(user_input)
    
    # 2. Cleaning (Stop-word removal)
    stop_words = set(stopwords.words('english'))
    cleaned_tokens = [w for w in tokens if not w.lower() in stop_words]
    
    # 3. POS Tagging
    tags = pos_tag(tokens)
    
    # Display Results in Tabs
    tab1, tab2, tab3 = st.tabs(["Raw Tokens", "Cleaned Text", "POS Tags"])
    
    with tab1:
        st.write(tokens)
        
    with tab2:
        st.write(cleaned_tokens)
        
    with tab3:
        # Convert tags to a DataFrame for a better look
        df = pd.DataFrame(tags, columns=['Word', 'POS Tag'])
        st.table(df)

elif analyze_button and not user_input:
    st.warning("Please enter some text first!")
st.markdown("Created by GROUP E, Software Engineering")
