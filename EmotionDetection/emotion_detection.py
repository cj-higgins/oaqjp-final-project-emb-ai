import requests
import json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=data, headers=Headers)
    response_dict = response.json()
    anger_score = response_dict['emotionPredictions'][0]['emotion']['anger']
    disgust_score = response_dict['emotionPredictions'][0]['emotion']['disgust']
    fear_score = response_dict['emotionPredictions'][0]['emotion']['fear']
    joy_score = response_dict['emotionPredictions'][0]['emotion']['joy']
    sadness_score = response_dict['emotionPredictions'][0]['emotion']['sadness']
    
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotions, key=emotions.get)

    return {
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': dominant_emotion
}
    