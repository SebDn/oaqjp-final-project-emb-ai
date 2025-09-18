import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=headers)

    formatted_response = response.json()
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    formatted_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score        
    }

    dominant_emotion = None
    # Find the dominant emotion only if there are actual positive scores to compare
    # If all scores are 0, we consider no dominant emotion.
    if any(score > 0 for score in formatted_output.values()):
        dominant_emotion = max(formatted_output, key=formatted_output.get)
   
    formatted_output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score, 
        'dominant_emotion':dominant_emotion    
    }
    
    return formatted_output