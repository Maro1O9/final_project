"""
server.py

This module implements a Flask web application for detecting emotions
from text input using the Watson NLP Emotion Detection service.

It provides an API endpoint '/emotionDetector' that accepts POST
requests with a text payload and returns the detected emotions and 
the dominant emotion as a JSON response.
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route to handle the emotion detection functionality
@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotion from a given text input.

    Returns:
        JSON response containing the emotion scores and the dominant emotion.
    """

    # Get the JSON data from the POST request
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided for emotion detection'}), 400

    # Get the text to analyze from the JSON
    text_to_analyze = data['text']

    # Run the emotion detector function on the text
    emotion_result = emotion_detector(text_to_analyze)

    # Format the response as requested
    response_message = (f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, 'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, 'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}.")

    # Return the response as a JSON
    return jsonify({'message': response_message})

# Home route to render the HTML page
@app.route('/')
def index():
    """
    home route
    """
    return render_template('index.html')

if __name__ == '__main__':
    # Run the app on localhost at port 5000
    app.run(host='0.0.0.0', port=5000)
