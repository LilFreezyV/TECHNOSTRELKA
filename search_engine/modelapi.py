import numpy as np
import string
import nltk
import re
from nltk.stem import *
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
from joblib import load

GENRES = [
    'drama',
    'thriller',
    'adult',
    'documentary',
    'comedy',
    'crime',
    'horror',
    'sport',
    'animation',
    'action',
    'fantasy',
    'short',
    'sci-fi',
    'adventure',
    'talk-show',
    'western',
    'family',
    'mystery',
    'history',
    'biography',
    'romance',
    'musical',
    'war'
]

nltk.download('stopwords')
nltk.download('punkt_tab')

english_stopwords = stopwords.words("english")
english_stopwords.extend(['…', '«', '»', '...'])

mystem = Mystem()

stemmer = SnowballStemmer("english")

logreg = load('logistic_regression_model.joblib')

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

def process_query(query: str) -> list[str]:
    # Предобработка текста
    query = remove_multiple_spaces(remove_numbers(remove_punctuation(query.lower())))
    query = remove_stop_words(query)
    query = lemmatize_text(query)

    # Получаем вероятности для каждого жанра
    probabilities = logreg.predict_proba([query])[0]

    # Сортируем вероятности и получаем индексы жанров с наибольшими вероятностями
    top3_indices = np.argsort(probabilities)[-3:][::-1]

    result = []

    for idx in top3_indices:
        result.append(GENRES[int(idx)])

    return result

    # print("Топ-3 жанра с наибольшими вероятностями:")
    # for idx in top3_indices:
    #     print(f"Жанр: {GENRES[int(idx)]}, Вероятность: {probabilities[idx]:.4f}")