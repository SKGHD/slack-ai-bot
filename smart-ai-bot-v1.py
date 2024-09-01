# Import necessary libraries
import os
import json
import boto3
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask import Flask, request, Response

# Initialize Flask app
app = Flask(__name__)

# Load Slack token from .slack_token file and set it as an environment variable
with open('.slack_token', 'r') as token_file:
    os.environ['SLACK_TOKEN'] = token_file.read().strip()

# Initialize Slack client using the token from environment variables
slack_token = os.environ['SLACK_TOKEN']
slack_client = WebClient(token=slack_token)
# Initialize Amazon Bedrock client
bedrock_client = boto3.client('bedrock', region_name='us-east-1')

# Function to handle Slack events
@app.route("/slack/events", methods=["POST"])
def slack_events():
    data = request.json

    if "challenge" in data:
        return Response(data["challenge"], mimetype='text/plain')

    if "event" in data:
        event = data["event"]
        if event["type"] == "message" and "subtype" not in event:
            user_query = event["text"]
            channel_id = event["channel"]

            # Query Amazon Bedrock
            response = query_bedrock(user_query)

            # Send response back to Slack
            send_message(channel_id, response)

    return Response(status=200)

# Function to query Amazon Bedrock
def query_bedrock(query):
    response = bedrock_client.invoke_endpoint(
        EndpointName='your-bedrock-endpoint',
        ContentType='application/json',
        Body=json.dumps({"input": query})
    )
    result = json.loads(response['Body'].read().decode())
    return result['output']

# Function to send message to Slack
def send_message(channel, text):
    try:
        slack_client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

# Run the Flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)