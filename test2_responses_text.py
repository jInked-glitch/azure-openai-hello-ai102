
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

# Azure OpenAI に Responses API (v1) 形式で接続するクライアントを作成
client = OpenAI(
    # 環境変数の endpoint 末尾の "/" を取り除き、
    # Responses API 用の "/openai/v1/" を付け足して base_url を作る
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)

prompt = """
Extract the following invoice details and return only valid JSON
with these keys:
invoice_number, invoice_date, vendor_name, total_amount, currency

Invoice text:
Invoice Number: INV-2026-001
Date: 2026-03-13
Vendor: ABC Supplies
Total: EUR 245.90
"""

# Responses API を使ってモデルにプロンプトを送信
resp = client.responses.create(
    # ここには「モデル名」ではなく Azure 上の deployment 名を指定する
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    input=prompt
)

# Responses API の出力テキストを表示
print(resp.output_text)