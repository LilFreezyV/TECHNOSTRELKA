import pandas as pd
import films

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

movies = films.get_short_df()

tfv = TfidfVectorizer(min_df=3,  max_features=None,
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

tfv_matrix = tfv.fit_transform(movies['text'])

sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


def give_recomendations(title, sig=sig) -> list[dict]:

    idx = indices[title]

    sig_scores = list(enumerate(sig[idx]))

    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    sig_scores = sig_scores[1:11]

    movie_indices = [i[0] for i in sig_scores]

    # Top 10
    result_df = movies[['title', 'genre', 'text']].iloc[movie_indices]

    res = []
    for _, row in result_df.iterrows():
        res.append({
            'title': row['title'],
            'text': row['text'],
            'genre': row['genre']
        })

    return res

