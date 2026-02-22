@"
# Azure OpenAI Hello (AI-102 practice)

Minimal Python example calling an Azure OpenAI deployment and printing the response.

## Setup
1) Install packages
python -m pip install -U openai python-dotenv

2) Create a .env file (DO NOT commit it)
AZURE_OPENAI_ENDPOINT=YOUR_ENDPOINT_HERE
AZURE_OPENAI_API_KEY=YOUR_KEY_HERE
AZURE_OPENAI_DEPLOYMENT=gpt-deploy-01

## Run
python hello_aoai.py

## Notes
- Never commit .env to GitHub.
"@ | Out-File -Encoding utf8 README.md