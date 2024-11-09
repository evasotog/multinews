from flask import Flask, render_template
import feedparser
import random

app = Flask(__name__)

# RSS feeds
spanish_feeds = [
    ("El País", "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"),
    ("ABC", "https://www.abc.es/rss/2.0/espana/"),
    ("La Vanguardia", "https://www.lavanguardia.com/rss/home.xml"),
    ("El Mundo", "https://e00-elmundo.uecdn.es/elmundo/rss/espana.xml"),
    ("20 Minutos", "https://www.20minutos.es/rss"),
]

dutch_feeds = [
    ("Dutch News", "https://www.dutchnews.nl/feed/"),
    ("NL Times", "https://nltimes.nl/rss"),
    ("Holland Times", "https://www.hollandtimes.nl/feed/"),
]

def fetch_feed(url):
    return feedparser.parse(url)

@app.route('/')
def index():
    spanish_news = []
    dutch_news = []

    # Fetch and label each feed item
    for name, feed_url in spanish_feeds:
        feed = fetch_feed(feed_url)
        for entry in feed.entries:
            spanish_news.append({
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary,
                'source': name
            })

    for name, feed_url in dutch_feeds:
        feed = fetch_feed(feed_url)
        for entry in feed.entries:
            dutch_news.append({
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary,
                'source': name
            })

    # Shuffle the news lists
    random.shuffle(spanish_news)
    random.shuffle(dutch_news)

    return render_template('index.html', spanish_news=spanish_news, dutch_news=dutch_news)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
