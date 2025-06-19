# backend/api/index.py
"""
Vercel serverless entry: импортируем готовый FastAPI‑app из пакета openui
"""
from openui.server import app  # FastAPI instance → Vercel ищет переменную `app`

import json, os
from openai import OpenAI           # pip install openai>=1.14

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def handler(request):
    if request.method == "OPTIONS":
        return "", 204, _cors()

    if request.method == "POST":
        data = request.json()
        messages = data.get("messages", [])
        model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            temperature=data.get("temperature", 0.7),
            max_tokens=data.get("max_tokens", 1024),
        )
        return json.dumps(resp.dict()), 200, {
            "Content-Type": "application/json", **_cors()
        }

    return "Method not allowed", 405, {"Allow": "POST,OPTIONS", **_cors()}


def _cors():
    return {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "content-type",
        "Access-Control-Allow-Methods": "POST,OPTIONS",
    }

