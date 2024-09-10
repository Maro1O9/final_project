import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if the input text is blank or only spaces
        # Return the dictionary with None values for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 400:  # Check for bad request status code
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Convert the response JSON into a Python dictionary
    response_data = response.json()

    # Extract the emotion scores from the response
    emotions = response_data.get('emotion_predictions', [])
    
    if not emotions:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse and get the specific emotions and their scores
    emotion_scores = {emotion['emotion']: emotion['score'] for emotion in emotions}

    # Extract the required emotions
    anger = emotion_scores.get('anger', 0)
    disgust = emotion_scores.get('disgust', 0)
    fear = emotion_scores.get('fear', 0)
    joy = emotion_scores.get('joy', 0)
    sadness = emotion_scores.get('sadness', 0)

    # Find the dominant emotion
    emotion_scores = {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness}
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return the formatted output dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
