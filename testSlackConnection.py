import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Load Slack token from .slack_token file and set it as an environment variable
with open('.slack_token', 'r') as token_file:
    os.environ['SLACK_TOKEN'] = token_file.read().strip()

# Initialize Slack client using the token from environment variables
slack_token = os.environ['SLACK_TOKEN']
slack_client = WebClient(token=slack_token)

def send_test_message(channel, text):
    try:
        response = slack_client.chat_postMessage(channel=channel, text=text)
        print(f"Message sent successfully: {response['ts']}")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

if __name__ == "__main__":
    send_test_message('#ai-slack-bot', 'Hello, this is a test message from the Slack bot!')