# Azure OpenAI Hello (AI-102 practice)

Minimal Python examples for calling an Azure OpenAI deployment and printing the response.

## Files

- `hello_aoai.py`
  - Chat Completions API example using `AzureOpenAI`
  - Uses `messages=[...]`

- `test1_responses_text.py`
  - Minimal Responses API text example
  - Uses `input="..."`

- `test2_responses_text.py`
  - Responses API invoice extraction from plain text
  - Returns JSON-style output

- `test3_invoice_pdf.py`
  - Responses API invoice extraction from PDF
  - Uploads a PDF file and passes `file_id` with `input_file`

- `invoice.pdf`
  - Sample invoice PDF for local testing

## Setup

1) Install packages

```bash
python -m pip install -U openai python-dotenv
```

2) Create a `.env` file (**DO NOT commit it**)

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

### Minimal Responses API text example

```bash
python test1_responses_text.py
```

### Responses API invoice text example

```bash
python test2_responses_text.py
```

### Responses API invoice PDF example

```bash
python test3_invoice_pdf.py
```

## Notes

- Use the `*.openai.azure.com` endpoint shown in Azure AI Foundry / Get Started.
- `hello_aoai.py` uses the Chat Completions API.
- The Responses API examples use Azure OpenAI v1-style `base_url`.
- In the PDF example, the script uploads the file first and then sends `file_id` with `input_file`.
- The sample PDF in this repository is only for practice.
- Never commit `.env` to GitHub.