from pathlib import Path
from plagiarism_engine.preprocessing import preprocess_document
import pandas as pd

def get_text_files(data_dir):
    data_dir = Path(data_dir)
    return sorted(data_dir.rglob("*.txt"))

def load_document(file_path,size=3):
    tokens,shingles = preprocess_document(file_path,size)
    return {
        "path": str(file_path),
        "tokens": tokens,
        "shingles": shingles
    }
    
def load_corpus(data_dir,size=3):
    files = get_text_files(data_dir)
    corpus = []
    for file_path in files:
        document = load_document(file_path,size)
        corpus.append(document)
    return corpus

def load_pairs_dataset(csv_path,text_col_a,text_col_b,label_col,limit=None):
    df = pd.read_csv(csv_path)
    if limit is not None:
        df = df.head(limit)
    pairs = []
    for _, row in df.iterrows():
        pairs.append({"text_a": row[text_col_a],"text_b": row[text_col_b],"label": row[label_col]})
    return pairs