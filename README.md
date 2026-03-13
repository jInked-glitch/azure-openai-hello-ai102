@"
# Azure OpenAI Hello (AI-102 practice)

Minimal Python example calling an Azure OpenAI deployment and printing the response.

## Files

- `hello_aoai.py`
  - Chat Completions API example using `AzureOpenAI`
  - Uses `messages=[...]`

- `text1_responses_text.py`
  - Responses API example using Azure OpenAI v1-style `base_url`
  - Uses `input="..."`
  - 
## Setup
1) Install packages
```
python -m pip install -U openai python-dotenv
```
2) Create a .env file (DO NOT commit it)
```env
AZURE_OPENAI_ENDPOINT=https://YOUR_RESOURCE_NAME.openai.azure.com/
AZURE_OPENAI_API_KEY=YOUR_KEY_HERE
AZURE_OPENAI_DEPLOYMENT=YOUR_DEPLOYMENT_NAME
AZURE_OPENAI_API_VERSION=2025-01-01-preview
```

## Run

### Chat Completions example

```bash
python hello_aoai.py
```

### Responses API example

```bash
python text1_responses_text.py
```

## Notes
- Use the `*.openai.azure.com` endpoint shown in Azure AI Foundry / Get Started.
- `hello_aoai.py` uses the Chat Completions API.
- `text1_responses_text.py` uses the Responses API with:
  - `base_url = https://YOUR_RESOURCE_NAME.openai.azure.com/openai/v1/`
- In the Responses API example, the script builds the `base_url` from `AZURE_OPENAI_ENDPOINT`.
- Never commit `.env` to GitHub.