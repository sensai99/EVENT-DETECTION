import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk import download

download('punkt') # if necessary...
# download('stopwords')

stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

# def rem_stopwords(text) :

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

A = 'indian cricket has moved on from Dhoni, selectors to convey this to Sourav Ganguly'

B = 'Dhoni to watch first day’s proceedings, confirms manager Diwakar becom'
print(cosine_sim(A, B))

# B = normalize(B)
# print(B)
# print(cosine_sim('a little bird', 'a little bird chirps'))
# print(cosine_sim('a little bird', 'a big dog barks'))