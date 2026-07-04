from pathlib import Path
import re
import string
from nltk.corpus import stopwords
ENGLISH_STOPWORDS = set(stopwords.words("english"))

def read_text(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    text = path.read_text(encoding="utf-8",errors="ignore")
    if not text.strip():
        raise ValueError(f"File is empty: {file_path}")
    return text

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def tokenize(text):
    if not text:
        return []
    return text.split()

def remove_stopwords(tokens):
    filtered_tokens = []
    for token in tokens:
        if token not in ENGLISH_STOPWORDS:
            filtered_tokens.append(token)
    return filtered_tokens

#tokens = ["see","you","in","a","another","place"]
#print(remove_stopwords(tokens))

def generate_shingles(tokens,size=3):#size = 3 or 4 or 5
    shingles = set()
    if len(tokens) < size:
        return shingles
    for i in range(len(tokens) - size+1):
        shingle = " ".join(tokens[i: i+size])
        shingles.add(shingle)
    return shingles

def preprocess_all_documents(file_path,size=3):
    text = read_text(file_path)
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    shingles = generate_shingles(tokens,size)
    return tokens,shingles