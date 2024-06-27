from multiprocessing import Process
from slack_bot.py import start_slack_bot
from twitter_bot.py import start_twitter_bot
from discord_bot.py import start_discord_bot

if __name__ == "__main__":
    slack_process = Process(target=start_slack_bot)
    twitter_process = Process(target=start_twitter_bot)
    discord_process = Process(target=start_discord_bot)
    
    slack_process.start()
    twitter_process.start()
    discord_process.start()
    
    slack_process.join()
    twitter_process.join()
    discord_process.join()
