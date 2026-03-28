from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download once
nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.5:
        return "positive", compound
    elif compound <= -0.5:
        return "negative", compound
    else:
        return "neutral", compound