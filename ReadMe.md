### README.md

# Smart AI Slack Bot

This project is a Slack bot that uses Amazon Bedrock to answer user queries. The bot is deployed on an EC2 instance and acts as the backend for interactions between the Slack bot and the Amazon Bedrock foundational model.

## Prerequisites

- Python 3.6 or higher
- AWS account with access to Amazon Bedrock
- Slack account with a created Slack app and bot token
- EC2 instance (if deploying on AWS)

## Setup Instructions

### Step 1: Clone the Repository

```sh
git clone https://github.com/your-repo/smart-ai-bot.git
cd smart-ai-bot
```

### Step 2: Create a Virtual Environment

1. **Create the virtual environment**:
   ```sh
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - **Command Prompt**:
     ```sh
     venv\Scripts\activate
     ```
   - **PowerShell**:
     ```sh
     .\venv\Scripts\Activate
     ```

### Step 3: Install Dependencies

```sh
pip install -r requirements.txt
```

### Step 4: Set Environment Variables

1. **Set the Slack bot token**:
   - **Command Prompt**:
     ```sh
     set SLACK_BOT_TOKEN=xoxb-your-bot-token
     ```
   - **PowerShell**:
     ```sh
     $env:SLACK_BOT_TOKEN="xoxb-your-bot-token"
     ```

2. **Set AWS credentials**:
   Ensure your AWS credentials are configured. You can use the AWS CLI to configure them:
   ```sh
   aws configure
   ```

### Step 5: Update the Script

Ensure the [`smart-ai-bot-v1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FD%3A%2FDownloads%2FBITS%20MTECH%2FM.tech%20final%20sem%20project%2Fcode%2Fslack-ai-bot%2Fsmart-ai-bot-v1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\Downloads\BITS MTECH\M.tech final sem project\code\slack-ai-bot\smart-ai-bot-v1.py") script reads the Slack token from the environment variable:

```python
# Initialize Slack client
slack_token = os.environ["SLACK_BOT_TOKEN"]
slack_client = Web

Client

(token=slack_token)
```

### Step 6: Run the Bot

```sh
python smart-ai-bot-v1.py
```

### Step 7: Deploy to EC2 (Optional)

1. **Launch an EC2 instance** with a suitable AMI (e.g., Amazon Linux 2).
2. **SSH into the EC2 instance** and set up the environment:
   ```sh
   sudo yum update -y
   sudo yum install python3 -y
   sudo pip3 install virtualenv
   ```

3. **Clone the repository** and set up the virtual environment:
   ```sh
   git clone https://github.com/your-repo/smart-ai-bot.git
   cd smart-ai-bot
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Set environment variables** on the EC2 instance:
   ```sh
   export SLACK_BOT_TOKEN='xoxb-your-bot-token'
   ```

5. **Run the bot**:
   ```sh
   python smart-ai-bot-v1.py
   ```

### Security Considerations

- **Never hardcode sensitive information** such as API keys or tokens in your source code.
- **Use environment variables** to manage sensitive information securely.
- **Ensure your EC2 instance** has the necessary IAM roles and permissions to access Amazon Bedrock and other AWS services.

### Troubleshooting

- **Check Slack API permissions**: Ensure your Slack app has the necessary permissions (scopes) to read and send messages.
- **Verify AWS credentials**: Ensure your AWS credentials are correctly configured and have the necessary permissions.
- **Review logs**: Check the logs for any errors or issues during execution.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

By following these instructions, you should be able to set up and run the Smart AI Slack Bot on any system.