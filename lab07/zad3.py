import praw
from dotenv import load_dotenv
from os import getenv
from json import dump

load_dotenv()
USERNAME = getenv("USERNAME")
CLIENT_ID = getenv("CLIENT_ID")
CLIENT_SECRET = getenv("CLIENT_SECRET")


def main() -> None:
    reddit = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=f"basic scraper by {USERNAME}")

    subreddit = reddit.subreddit("MachineLearning")
    top_posts = subreddit.top(limit=100)

    posts_data = []
    for post in top_posts:
        post_info = {}
        post_info["id"] = post.id
        post_info["author"] = post.author.name if post.author else "Unknown User"
        post_info["url"] = post.url
        post_info["score"] = post.score
        posts_data.append(post_info)

    with open("scraped_data.json", "w") as fp:
        dump(posts_data, fp)


if __name__ == "__main__":
    main()