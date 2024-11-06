import yaml
import pickle
import spacy
from gensim import models, corpora
from pathlib import Path
from functools import lru_cache

nlp = spacy.load('en_core_web_md', disable=['parser', 'ner'])

path_to_params = Path(__file__).parent / 'params.yaml'
dataset_root = Path(__file__).parent / 'model'

with open(path_to_params, 'r') as params_yaml:
    params = yaml.safe_load(params_yaml)

N_TOPICS = int(params['N_TOPICS'])
ALPHA = params['ALPHA']
BETA = params['BETA']

def load_resources():
    with open(dataset_root.joinpath("articles.txt"), "r", encoding="utf-8") as f:
        dataset = f.read().split("@delimiter")

    with open(dataset_root.joinpath(f"model_{N_TOPICS}_{ALPHA}_{BETA}.pkl"), "rb") as f_rb:
        model = pickle.load(f_rb)

    with open(dataset_root.joinpath("dictionary.pkl"), "rb") as f_rb:
        dictionary = pickle.load(f_rb)

    with open(dataset_root.joinpath(f"lda_index_{N_TOPICS}_{ALPHA}_{BETA}.pkl"), "rb") as f_rb:
        lda_index = pickle.load(f_rb)

    return dataset, dictionary, model, lda_index

dataset, dictionary, model, lda_index = load_resources()

def text_filter(tokenized_article):
    return [t.lemma_ for t in tokenized_article if t.is_alpha and not t.is_stop]

# Cache the final article retrieval results for efficiency
@lru_cache(maxsize=128)
def find_similar_articles(text):
    """Process the article text and find the top N similar articles."""
    # Tokenize and filter the text
    tokens = text_filter(nlp(text))
    article_bow = dictionary.doc2bow(tokens)
    
    # Retrieve similar articles
    similar_docs = lda_index[model[article_bow]]
    top_n_docs = sorted(enumerate(similar_docs), key=lambda item: -item[1])[1:6]
    
    # Get top articles with similarity scores and a snippet
    similar_articles = [(entry[0], entry[1], dataset[entry[0]][:300]) for entry in top_n_docs]
    
    return similar_articles
