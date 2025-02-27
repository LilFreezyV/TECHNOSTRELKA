import pandas as pd

# full_df = pd.DataFrame(
#     [],
#     columns=['title', 'description', 'text_lemm', 'genre']
# )

# for film in get_fulls_films():
#      full_df.loc[len(df)] = {
#           'title': film[0],
#           'description': film[1],
#           'text_lemm': film[2],
#           'genre': film[3]
#      }

full_df = pd.read_csv('final_dataset_full.csv')

# short_df = pd.DataFrame(
#     [],
#     columns=['title', 'description', 'text_lemm', 'genre']
# )

# for film in get_fulls_films():
#      short_df.loc[len(df)] = {
#           'title': film[0],
#           'description': film[1],
#           'text_lemm': film[2],
#           'genre': film[3]
#      }

short_df = pd.read_csv('final_dataset_short.csv')

def get_full_df():
    return full_df

def get_short_df():
    return short_df