import os
import praw
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()  # Load .env variables

def reddit_auth():
    """Authenticate with Reddit API using environment variables."""
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="sentiment-topic-tracker by /u/{}".format(os.getenv("REDDIT_USERNAME")),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

def fetch_subreddit_posts(subreddit_name="datascience", limit=100):
    """Fetch posts from a subreddit and return as a list of dictionaries."""
    reddit = reddit_auth()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.hot(limit=limit):
        posts.append({
            "id": post.id,
            "title": post.title,
            "text": post.selftext,
            "score": post.score,
            "url": post.url,
            "created_utc": datetime.utcfromtimestamp(post.created_utc).isoformat(),
            "num_comments": post.num_comments,
            "subreddit": subreddit_name
        })

    return posts

def save_posts_to_csv(posts, filename="data/reddit_posts.csv"):
    """Save list of post dictionaries to a CSV file."""
    df = pd.DataFrame(posts)
    df.to_csv(filename, index=False)
    print(f"✅ Saved {len(posts)} posts to {filename}")

if __name__ == "__main__":
    subreddit = "datascience"
    post_limit = 50
    posts = fetch_subreddit_posts(subreddit_name=subreddit, limit=post_limit)
    save_posts_to_csv(posts, filename=f"data/{subreddit}_posts.csv")