from mindsdb import MindsDB
from textblob import TextBlob
import logging
import time
from collections import defaultdict

# Initialize MindsDB
mdb = MindsDB()
project = mdb.get_project('chat_model')

# Initialize logging
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Rate limiting configuration
rate_limit_window = 60  # 1 minute
rate_limit_max_requests = 5
user_request_log = defaultdict(list)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_response(input_text):
    prediction = project.predict(when={'input': input_text})
    return prediction['response']

def get_response_with_sentiment(input_text):
    sentiment = analyze_sentiment(input_text)
    response = get_response(input_text)
    
    if sentiment < 0:
        response = "It seems like you're having a tough time. " + response
    elif sentiment > 0:
        response = "I'm glad to hear that! " + response
    
    return response

def safe_get_response(input_text):
    try:
        response = get_response_with_sentiment(input_text)
    except Exception as e:
        response = "Sorry, I encountered an error while processing your message."
        logging.error(f"Error: {e}")
    return response

def log_interaction(platform, user, message, response):
    logging.info(f"Platform: {platform}, User: {user}, Message: {message}, Response: {response}")

def rate_limited(user):
    current_time = time.time()
    request_times = user_request_log[user]
    
    # Remove requests that are outside the rate limit window
    user_request_log[user] = [t for t in request_times if current_time - t < rate_limit_window]
    
    if len(user_request_log[user]) >= rate_limit_max_requests:
        return True
    else:
        user_request_log[user].append(current_time)
        return False

def handle_command(command, user):
    if command == "/help":
        return "Here are the commands you can use: ..."
    elif command == "/info":
        return "This bot helps you with ..."
    else:
        return "Unknown command. Type /help for the list of commands."

def process_message(message):
    if message.startswith("/"):
        command = message.split()[0]
        return handle_command(command)
    else:
        return safe_get_response(message)
