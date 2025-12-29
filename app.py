import sys
import logging
from flask import Flask, render_template, request

from src.pipeline.predict_pipeline import Predictor
from src.exception import CustomException

# ------------------------
# Flask app initialization
# ------------------------
app = Flask(__name__)

# ------------------------
# Initialize Predictor
# ------------------------
try:
    predictor = Predictor()
except Exception as e:
    logging.error("Error initializing predictor", exc_info=True)
    raise CustomException(e, sys)

# ------------------------
# Routes
# ------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    error_message = None
    review_text = ""
    sentiment_label = None
    confidence = None

    try:
        if request.method == "POST":
            review_text = request.form.get("review")

            # Empty input validation
            if not review_text or review_text.strip() == "":
                error_message = "Please enter some text to analyze."
            else:
                # Prediction
                prediction = predictor.predict(review_text)

                sentiment_label = (
                    "Positive 😊" if prediction == 1 else "Negative 😞"
                )

                # Confidence score
                proba = predictor.model.predict_proba(
                    predictor.vectorizer.transform([review_text])
                )[0]

                confidence = int(max(proba) * 100)

    except Exception as e:
        logging.error("Error occurred in Flask route", exc_info=True)
        error_message = "Something went wrong. Please try again."

        # ❌ Do NOT raise CustomException in Flask UI
        # raise CustomException(e, sys)

    return render_template(
        "index.html",
        sentiment_label=sentiment_label,
        confidence=confidence,
        review_text=review_text,
        error_message=error_message
    )

# ------------------------
# Main
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)


