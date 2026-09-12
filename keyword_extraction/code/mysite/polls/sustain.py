from django.core.cache import cache
import pickle

model_cache_key = 'model_cache'
# this key is used to `set` and `get` your trained model from the cache

countVectorizer = cache.get(model_cache_key) # get vectorizer from cache

if countVectorizer is None:
    # your model isn't in the cache
    # so `set` it
    # load the vectorizer
    countVectorizer = pickle.load(open('polls/keywords-count-vectorizer.pkl', 'rb'))
    cache.set(model_cache_key, countVectorizer, None)
