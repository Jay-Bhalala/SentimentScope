
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(corpus):
    ''' Function to extract features from a corpus of text '''
    vectorizer = TfidfVectorizer(max_features=300)
    features = vectorizer.fit_transform(corpus)
    return features

if __name__ == "__main__":
    sample_corpus = ["This is the first document.", "This document is the second document.", "And this is the third one."]
    features = extract_features(sample_corpus)
    print("Feature matrix:")
    print(features.toarray())
