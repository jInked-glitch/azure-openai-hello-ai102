
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

# PDFファイルをアップロード
with open("sample_invoice_ai102.pdf", "rb") as f:
    uploaded_file = client.files.create(
        file=f,
        purpose="assistants"
    )

# Responses API を使ってモデルにプロンプトを送信
resp = client.responses.create(
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
    # file_id を使って Responses API に渡す
    input=[{
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Extract the invoice details and return only valid JSON with these keys: invoice_number, invoice_date, vendor_name, total_amount, currency"
                },
                {
                    "type": "input_file",
                    "file_id":uploaded_file.id
                }
            ]
        }]
    )

# Responses API の出力テキストを表示はテキスト版と同様
print(resp.output_text)