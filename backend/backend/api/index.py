# backend/api/index.py
"""
Vercel serverless entry: импортируем готовый FastAPI‑app из пакета openui
"""
from openui.server import app  # FastAPI instance → Vercel ищет переменную `app`
