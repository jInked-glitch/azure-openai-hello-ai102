import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
api_key = os.environ["AZURE_OPENAI_API_KEY"]
deployment = os.environ["AZURE_OPENAI_DEPLOYMENT"]

client = OpenAI(
    api_key=api_key,
    base_url=endpoint.rstrip("/") + "/openai/v1/",
)

resp = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": "Say hello in French in one sentence."}],
)

print(resp.choices[0].message.content)
