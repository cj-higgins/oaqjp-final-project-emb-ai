import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestMyFunction(unittest.TestCase):

    def test_my_function(self):
        results=[]
        texts = ["I am glad this happened", "I am really mad about this", "I feel disgusted just hearing about this","I am so sad about this","I am really afraid that this will happen"]
        for text in texts:
            response = emotion_detector(text)
            dominant_emotion = response["dominant_emotion"]
            results.append(dominant_emotion)
        print(results)
        self.assertEqual(results, ["joy","anger","disgust","sadness","fear"])

if __name__ == "__main__":
    unittest.main()