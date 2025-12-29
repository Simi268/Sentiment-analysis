import re
import nltk
import sys
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.logger import logging
from src.exception import CustomException


def ensure_nltk_resources():
    try:
        stopwords.words("english")
    except LookupError:
        nltk.download("stopwords")

    try:
        nltk.data.find("corpora/wordnet")
    except LookupError:
        nltk.download("wordnet")


class TextCleaner:
    _initialized = False
    _stop_words = None
    _lemmatizer = None

    @classmethod
    def _init_resources(cls):
        if not cls._initialized:
            ensure_nltk_resources()
            cls._stop_words = set(stopwords.words("english"))
            cls._lemmatizer = WordNetLemmatizer()
            cls._initialized = True

    @staticmethod
    def clean_text(text: str) -> str:
        try:
            TextCleaner._init_resources()
            logging.info("Cleaning input text")

            text = text.lower()
            text = re.sub(r"http\S+|www\S+", "", text)
            text = re.sub(r"[^a-z\s]", "", text)

            tokens = [
                TextCleaner._lemmatizer.lemmatize(word)
                for word in text.split()
                if word not in TextCleaner._stop_words
            ]

            return " ".join(tokens)

        except Exception as e:
            logging.error("Error occurred during text cleaning")
            raise CustomException(e, sys)
