import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)

# メソッド名がそのまま chat.completions.create だからAPIの種類は Chat Completions
resp = client.chat.completions.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    # messages=[...] を使って入力形式も Chat Completions 型
    messages=[{"role": "user", "content": "Say hello in French in one sentence."}],
)
# 出力の取り方も Chat Completions 型
print(resp.choices[0].message.content)
