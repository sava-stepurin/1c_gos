import argparse
from nltk.tokenize import WordPunctTokenizer
import pickle


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg('--file_path', type=str)
    args = parser.parse_args()

    with open("data/model.pickle", 'rb') as f:
        model = pickle.load(f)

    with open("data/tfidf.pickle", 'rb') as f:
        vectorizer = pickle.load(f)

    tokenizer = WordPunctTokenizer()

    with open(args.file_path) as f:
        text = f.read()

    parsed_text = ' '.join(tokenizer.tokenize(text.lower()))
    parsed_text = vectorizer.transform([parsed_text])
    res = model.predict(parsed_text)[0]
    print(text, " - ", end="")
    if res == 0:
        print("разговорный")
    elif res == 1:
        print("техническая литература")
    else:
        print("художественная литература")
