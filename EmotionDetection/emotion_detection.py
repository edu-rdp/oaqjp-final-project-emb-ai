import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes emotion, handling potential errors from the API.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    # For a blank entry, the API returns a 400 status code.
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    response_dict = json.loads(response.text)
    emotion_predictions = response_dict.get('emotionPredictions', [])
    if not emotion_predictions:
        return None 

    emotions = emotion_predictions[0].get('emotion', {})
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion

    return emotions