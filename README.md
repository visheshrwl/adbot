# Chatbot Project

This project implements a chatbot integrated with Slack, Twitter, and Discord using MindsDB for response generation and various advanced features.

## Setup

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
    -  Create a `.env` file in the project root and add the following:
        ```bash
        SLACK_BOT_TOKEN=your_slack_bot_token
        SLACK_APP_TOKEN=your_slack_app_token
        TWITTER_API_KEY=your_twitter_api_key
        TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
        TWITTER_ACCESS_TOKEN=your_twitter_access_token
        TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
        DISCORD_TOKEN=your_discord_bot_token
        ```

3. Train the MindsDB model using the provided script.

# Running the bots

Run the main script to start all the bots:

```bash
python main.py
```