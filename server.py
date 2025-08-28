"""
This module contains a Flask web application for emotion detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes user-provided text for emotions and returns the result.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle the error case
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    dominant_emotion = response.pop('dominant_emotion')
    response_text = ", ".join([f"'{k}': {v}" for k, v in response.items()])

    # Return the formatted response string, broken into two lines for readability
    return (f"For the given statement, the system response is {response_text}. "
            f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    