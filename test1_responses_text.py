"""
Minimal Azure OpenAI Responses API example

What this script does:
- Connects to Azure OpenAI using the v1-style base_url
- Sends a simple text prompt with the Responses API
- Prints the model output

Required environment variables in .env:
- AZURE_OPENAI_ENDPOINT
- AZURE_OPENAI_API_KEY
- AZURE_OPENAI_DEPLOYMENT
"""

import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

# .env ファイルから環境変数を読み込む
# 例:
# AZURE_OPENAI_ENDPOINT=https://xxxxx.openai.azure.com/
# AZURE_OPENAI_API_KEY=your_api_key
# AZURE_OPENAI_DEPLOYMENT=your_deployment_name
load_dotenv()

# 使用中の openai パッケージのバージョン確認
# トラブル時の切り分けに役立つ
print("openai version:", openai.__version__)

# Azure OpenAI に Responses API (v1) 形式で接続するクライアントを作成
client = OpenAI(
    # 環境変数の endpoint 末尾の "/" を取り除き、
    # Responses API 用の "/openai/v1/" を付け足して base_url を作る
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

# Responses API を使ってモデルにプロンプトを送信
resp = client.responses.create(
    # ここには「モデル名」ではなく Azure 上の deployment 名を指定する
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    input="Say hello in French in one sentence."
)

# Responses API の出力テキストを表示
print(resp.output_text)