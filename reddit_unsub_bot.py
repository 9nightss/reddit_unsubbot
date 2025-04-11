import praw
   
   # Reddit API credentials
CLIENT_ID = "Enter_your_clientid"
CLIENT_SECRET = "fyout_secretkey"
USERNAME = "username"
PASSWORD = "password"
USER_AGENT = "UnsubBot" 
   
   # Authenticate with Reddit
reddit = praw.Reddit(
       client_id=CLIENT_ID,
       client_secret=CLIENT_SECRET,
       username=USERNAME,
       password=PASSWORD,
       user_agent=USER_AGENT
   )
   
   # Get list of subscribed subreddits
subscribed_subs = list(reddit.user.subreddits(limit=None))
   
print(f"Found {len(subscribed_subs)} subscribed subreddits. Leaving them now...")
   
   # Leave each subreddit
for subreddit in subscribed_subs:
       print(f"Leaving r/{subreddit.display_name}")
       subreddit.unsubscribe()
   
print("All done!")
