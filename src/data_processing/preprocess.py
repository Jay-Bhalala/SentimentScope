
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def clean_text(text):
    ''' Function to clean the text '''
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabet characters
    text = text.lower().strip()  # Convert to lowercase and strip whitespaces
    return text

def tokenize_text(text):
    ''' Function to tokenize the text '''
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

if __name__ == "__main__":
    sample_text = "This is a sample tweet! Check out https://example.com #datascience"
    cleaned_text = clean_text(sample_text)
    tokens = tokenize_text(cleaned_text)
    print(f"Original: {sample_text}")
    print(f"Cleaned: {cleaned_text}")
    print(f"Tokens: {tokens}")
