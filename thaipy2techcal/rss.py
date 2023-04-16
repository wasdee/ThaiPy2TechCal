import feedparser

def read_rss_feed(url):
    feed = feedparser.parse(url)
    return feed

if __name__ == "__main__":
    url = "https://www.meetup.com/ThaiPy-Bangkok-Python-Meetup/events/rss/"
    feed = read_rss_feed(url)

    print("Feed Title:", feed.feed.title)
    print("Feed Link:", feed.feed.link)
    print("Feed Description:", feed.feed.description)
    print("")

    for entry in feed.entries:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published:", entry.published)
        print("Entry Summary:", entry.summary)
        print("------------")