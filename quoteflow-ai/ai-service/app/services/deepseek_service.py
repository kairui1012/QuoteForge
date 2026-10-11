import httpx

from app.core.config import settings


async def chat(message: str) -> str:
    # 1. 从 settings 读取 DeepSeek 配置
    url = settings.deepseek_base_url.rstrip("/") + "/chat/completions"

    # 2. 准备 Headers
    headers = {
        "Authorization": f"Bearer {settings.deepseek_api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # 3. 准备 JSON Payload
    payload = {
        "model": settings.deepseek_model,
        "messages": [
            {
                "role": "system",
                "content":
                    """
                        You are an AI assistant for QuoteForge, a smart quotation system.
                    
                        Your task is to extract structured product information from customer messages.
                    
                        Customers may use English, Chinese, Malay, or Manglish.
                    
                        Rules:
                        1. Identify all products mentioned in the message.
                        2. Extract the product name and quantity.
                        3. Extract any requested discount percentage.
                        4. Do not invent missing information.
                        5. If information is missing, use null.
                        6. If a product is ambiguous, mark it for review.
                        7. Do not calculate prices or generate quotations.
                        8. Return only valid JSON without Markdown formatting.
                    
                       Return the following JSON structure:
                        {
                            "items": [
                                {
                                    "product_name": "string",
                                    "quantity": 1,
                                    "requested_discount_percent": null
                                }
                            ],
                            "requires_review": false
                        }
                    """
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "stream": False,
        "thinking": {
            "type": "disabled"
        },
        "response_format": {
            "type": "json_object"
        }
    }

    # 4. 使用 httpx.AsyncClient 发送 POST
    async with httpx.AsyncClient(timeout=30.0) as deepSeekClient:
        response = await deepSeekClient.post(
            url,
            headers=headers,
            json=payload
        )
    # 5. 检查 HTTP Status
    print("DeepSeek Status:", response.status_code)

    if response.status_code >= 400:
        print("DeepSeek Error:", response.text)

    response.raise_for_status()
    # 6. 从 Response JSON 提取 AI 的回复
    data = response.json()
    choice = data["choices"][0]
    if choice["finish_reason"] != "stop":
        raise ValueError("AI response was not completed successfully")

    content = choice["message"]["content"]

    if not isinstance(content, str) or not content.strip():
        raise ValueError("AI returned empty content")

    # 7. 返回字符串
    return content