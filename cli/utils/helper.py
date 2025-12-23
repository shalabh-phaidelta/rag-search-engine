from nltk.stem import PorterStemmer 
from pathlib import Path

def read_stop_words(path: str) -> list:
    try:
        with open(Path(path), 'r') as file:
            content = file.read()
            lines = content.splitlines()
            return lines
    except FileNotFoundError:
        print(f"File {path} not found")

def remove_stop_words_from(target: list[str]) -> list[str]:
    """Remove stop words"""
    stop_words = read_stop_words("data/stopwords.txt")
    # target = target.split()
    cleaned_target = [w for w in target if w not in stop_words]
    return cleaned_target 

def stem_words(non_root_words: list[str]) -> list[str]:
    """Convert non root words to root words"""
    stemmer = PorterStemmer()
    root_words = [stemmer.stem(w) for w in non_root_words]
    return root_words




if "__main__" == __name__:
    # print(read_stop_words("data/stopwords.txt"))
    # print(remove_stop_words_from("i want to sleep"))
    pass
