import speech_recognition as sr
from textblob import TextBlob

# Initialize the recognizer
recognizer = sr.Recognizer()

def recognize_speech_from_mic():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"Transcribed Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def analyze_sentiment(text):
    if text:
        analysis = TextBlob(text)
        sentiment_score = analysis.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        return sentiment, sentiment_score
    return None, None

# Example usage
transcribed_text = recognize_speech_from_mic()
sentiment, score = analyze_sentiment(transcribed_text)

if sentiment:
    print(f"Sentiment: {sentiment}, Score: {score:.2f}")
