import numpy as np
import pandas as pd
import string
import nltk
import re
from nltk.stem import *
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import films

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = films.get_full_df()

nltk.download('stopwords')
nltk.download('punkt_tab')

english_stopwords = stopwords.words("english")
english_stopwords.extend(['…', '«', '»', '...'])

mystem = Mystem()

stemmer = SnowballStemmer("english")


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['text_lemm'])

def remove_punctuation(text):
    return "".join([ch if ch not in string.punctuation else ' ' for ch in text])

def remove_numbers(text):
    return ''.join([i if not i.isdigit() else ' ' for i in text])

def remove_multiple_spaces(text):
	return re.sub(r'\s+', ' ', text, flags=re.I)

def lemmatize_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in english_stopwords and token != " "]
    text = " ".join(tokens)
    return text

def remove_stop_words(text):
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in english_stopwords and token != ' ']
    return " ".join(tokens)

def lemmatize_text(text):
    text_lem = mystem.lemmatize(text)
    tokens = [token for token in text_lem if token != ' ']
    return " ".join(tokens)

def process_query(query: str) -> list[dict]:
    # Предобработка текста
    query = remove_multiple_spaces(remove_numbers(remove_punctuation(query.lower())))
    query = remove_stop_words(query)
    query = lemmatize_text(query)

    user_input_vector = vectorizer.transform([query])

    similarities = cosine_similarity(user_input_vector, tfidf_matrix)
    top_10_indices = similarities.argsort()[0][-10:][::-1]  # Индексы 10 самых близких фильмов
    try:
        result_df = df.iloc[top_10_indices][['title', 'text', 'genre']]
    except Exception as e:
        pass

    res = []
    for _, row in result_df.iterrows():
        res.append({
            'title': row['title'],
            'text': row['text'],
            'genre': row['genre']
        })
    
    return res