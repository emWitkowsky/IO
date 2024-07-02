from nltk.sentiment.vader import SentimentIntensityAnalyzer
import text2emotion as t2e

# Mercure Hotel Warsaw, generated with AI
positive = "The Mercure Warszawa Grand’s prestigious location in the heart of the city, surrounded by ministries and embassies, and just steps away from the fashionable shops and venues of Plac Trzech Krzyży, makes it an ideal spot for both business travelers and leisure visitors. The comfortable rooms and proximity to the beautiful Łazienki Park add to its charm."
negative = "Outdated, dirty, and small rooms mar the experience at Mercure Warszawa Grand. The front desk service was a total disaster, and despite being priced and advertised as a 4-star hotel, it feels more like a 2/3 star facility at best. The need for towel changes and a view over a dirty roof hardly compensate for the convenient location."

# nltk vader
sentiment = SentimentIntensityAnalyzer()

print("Possibly positive review:", sentiment.polarity_scores(positive))     # {'neg': 0.0, 'neu': 0.437, 'pos': 0.563, 'compound': 0.97}
print("Possibly negative review:", sentiment.polarity_scores(negative))    # {'neg': 0.205, 'neu': 0.703, 'pos': 0.092, 'compound': -0.8059}

# text2emotion
print("Possibly positive review:", t2e.get_emotion(positive))     # {'Happy': 0.78, 'Angry': 0.0, 'Surprise': 0.0, 'Sad': 0.0, 'Fear': 0.22}
print("Possibly negative review:", t2e.get_emotion(negative))    # {'Happy': 0.0, 'Angry': 0.30, 'Surprise': 0.20, 'Sad': 0.25, 'Fear': 0.25}