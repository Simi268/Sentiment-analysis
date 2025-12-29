import joblib
from src.components.data_cleaning import TextCleaner
from src.logger import logging
from src.exception import CustomException
import sys

class SentimentPredictor:
    def __init__(self):
        try:
            logging.info("Loading model and vectorizer")
            self.model = joblib.load("artifacts/sentiment_model.pkl")
            self.vectorizer = joblib.load("artifacts/tfidf_vectorizer.pkl")
        except Exception as e:
            logging.error("Error loading model artifacts")
            raise CustomException(e, sys)

    def predict(self, text: str) -> int:
        try:
            logging.info("Starting prediction")
            cleaned = TextCleaner.clean_text(text)
            vector = self.vectorizer.transform([cleaned])
            prediction = self.model.predict(vector)[0]
            logging.info("Prediction completed")
            return int(prediction)
        except Exception as e:
            logging.error("Error during prediction")
            raise CustomException(e, sys)

class Predictor:
    def __init__(self):
        self.model = joblib.load("artifacts/sentiment_model.pkl")
        self.vectorizer = joblib.load("artifacts/tfidf_vectorizer.pkl")

    def predict(self, text):
        vec = self.vectorizer.transform([text])
        return self.model.predict(vec)[0]
