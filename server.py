from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get("text")
    result = emotion_detector(text)
    return f"For the given statement, the system response is: 'anger': {result['anger']}, 'disgust'={result['disgust']}, 'fear':{result['fear']}, 'joy':{result['joy']}, 'sadness':{result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

