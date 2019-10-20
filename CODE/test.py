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

vectorizer = TfidfVectorizer(tokenizer=normalize)#	, stop_words='english')

# def rem_stopwords(text) :

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    # print(tfidf.)
    return ((tfidf * tfidf.T).A)[0,1]



A = "# PulwamaAttack # PulwamaTerrorAttack United all Indians to rise in one voice # Pulwamaneveragain"

B = "In these 21 days, one thing that has come out evidently which the world has also seen— while Pakistan is united against India, India is divided against both Terror and Pakistan. They are united, we are divided. # PulwamaAttack # JammuTerrorAttack # WarOnTerror"

C = "Where was # PMModi when # PulwamaAttack happened? Why didn't he address the nation when 15 miners were trapped in Meghalaya? Modiji is the first to take credit for other people's achievements & the last to take responsibility for his govt's failures. # ASAT # MissionShakti # DRDO"

D = "PM didn’t address the nation after # PulwamaAttack PM didn’t address the nation after # BalakotStrike PM addresses the nation today to seek credit for # MissionShakti ... It’s clear- he’s on a reactive mode after @ RahulGandhi changed the election narrative to Economic with # NYAY"

print(cosine_sim(A, B))

print(cosine_sim(C, D))

print(cosine_sim(A, C))

print(cosine_sim(D, B))


# B = normalize(B)
# print(B)
# print(cosine_sim('a little bird', 'a little bird chirps'))
# print(cosine_sim('a little bird', 'a big dog barks'))