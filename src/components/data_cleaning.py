import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.logger import logging
from src.exception import CustomException
import sys


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


class TextCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        try:
            logging.info("Cleaning input text")

            text = text.lower()
            text = re.sub(r"http\S+|www\S+", "", text)
            text = re.sub(r"[^a-z\s]", "", text)

            tokens = text.split()
            tokens = [
                lemmatizer.lemmatize(word)
                for word in tokens
                if word not in stop_words
            ]

            cleaned_text = " ".join(tokens)  
            return cleaned_text

        except Exception as e:
            logging.error("Error occurred during text cleaning")
            raise CustomException(e, sys)


