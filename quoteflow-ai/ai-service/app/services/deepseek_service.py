import httpx
from fastapi import FastAPI

FastAPI
# DeepSeekService
#
# Input:
#     message: str
#
# Process:
#     1. 读取 API Key
#     2. 构造 System Prompt
#     3. 构造 User Message
#     4. 使用 HTTPX 发送 POST 请求
#     5. 检查 HTTP Status Code
#     6. 获取 AI 返回的 Content
#     7. 返回结果
#
# Output:
#     str (暂时)