from collections import defaultdict

def track_hashtags(tweets):
    hashtag_counts = defaultdict(int)
    for tweet in tweets:
        for word in tweet.split():
            if word.startswith("#"):
                hashtag_counts[word] += 1
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_hashtags[:3]


tweets = ["I love #Python", "#Python is awesome", "#DSA is fun", "#Python rocks"]
top_hashtags = track_hashtags(tweets)
print("Top 3 Hashtags:", top_hashtags)