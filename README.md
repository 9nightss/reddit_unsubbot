# reddit_unsubbot
 // This bot is specifically made for subreddit hoarders :) 

# UnsubBot - Mass Unfollow Reddit Subreddits

UnsubBot is a Python script that allows users to quickly unfollow all the subreddits they are subscribed to on Reddit using the Reddit API (PRAW).

## Prerequisites

- Python 3.x
- [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/en/latest/)
- Reddit account and API credentials

### Install PRAW

To install PRAW, use pip:

```bash
pip install praw
```

## Setup

Before running the script, you need to configure your Reddit API credentials.

1. Go to [Reddit's Developer page](https://www.reddit.com/prefs/apps) and create a new developer application to get your **client ID** and **client secret**.

2. Replace the placeholders in the script with your credentials:
   - `CLIENT_ID`
   - `CLIENT_SECRET`
   - `USERNAME`
   - `PASSWORD`
   - `USER_AGENT` (can be any descriptive string)

```python
CLIENT_ID = "Enter_your_clientid"
CLIENT_SECRET = "Enter_your_secretkey"
USERNAME = "your_username"
PASSWORD = "your_password"
USER_AGENT = "UnsubBot"
```

## Usage

1. Clone or download the script:

   ```bash
   git clone https://github.com/your-username/unsubbot.git
   cd unsubbot
   ```

2. Run the script:

   ```bash
   python unsubbot.py
   ```

   The script will:
   - Authenticate using your Reddit credentials.
   - Retrieve all the subreddits you're subscribed to.
   - Unsubscribe from each subreddit.

3. You will see output like this:
   ```bash
   Found 20 subscribed subreddits. Leaving them now...
   Leaving r/subreddit1
   Leaving r/subreddit2
   ...
   All done!
   ```

## Important Notes

- Ensure your Reddit account has the necessary permissions to unsubscribe from subreddits.
- Use caution when running scripts like this, as it will unfollow all subreddits.
- The script uses Reddit's API with your credentials; keep them secure and do not share your client ID, secret, or password.
- You can modify the script to target specific subreddits by changing the logic for `subscribed_subs` (e.g., filter based on name or category).

## Troubleshooting

- **Authentication errors:** Ensure your `CLIENT_ID`, `CLIENT_SECRET`, `USERNAME`, `PASSWORD`, and `USER_AGENT` are correct.
- **API limits:** Reddit's API has rate limits. If you unfollow too many subreddits too quickly, you might encounter temporary bans or limitations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
