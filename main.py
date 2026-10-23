# Simple Sentiment Analysis (No Libraries)

positive_words = [
    "good", "great", "happy", "excellent", "awesome",
    "love", "nice", "best", "amazing", "wonderful"
]

negative_words = [
    "bad", "sad", "hate", "worst", "terrible",
    "poor", "awful", "boring", "angry", "disappointing"
]

text = input("Enter a sentence: ").lower()

positive = 0
negative = 0

for word in positive_words:
    if word in text:
        positive += 1

for word in negative_words:
    if word in text:
        negative += 1

print("\nResult:")

if positive > negative:
    print("😊 Positive Sentiment")
elif negative > positive:
    print("😞 Negative Sentiment")
else:
    print("😐 Neutral Sentiment")