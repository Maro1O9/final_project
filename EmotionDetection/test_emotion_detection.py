from emotion_detection import emotion_detector


def test_joy():
    test = emotion_detector("I am glad this happened")
    if test.get('dominant_emotion') == 'joy':
        return "pass"
    return test

print(test_joy())

def test_anger():
    test = emotion_detector("I am really mad about this")
    if test.get('dominant_emotion') == 'anger':
        return "pass"
    return test

print(test_anger())

def test_disgust():
    test = emotion_detector("I feel disgusted just hearing about this")
    if test.get('dominant_emotion') == 'disgust':
        return "pass"
    return test

print(test_disgust())

def test_sadness():
    test = emotion_detector("I am so sad about this")
    if test.get('dominant_emotion') == 'sadness':
        return "pass"
    return test

print(test_sadness())

def test_fear():
    test = emotion_detector("I am really afraid that this will happen")
    if test.get('dominant_emotion') == 'fear':
        return "pass"
    return test

print(test_fear())
