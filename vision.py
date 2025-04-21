import io
import base64
from PIL import Image
from config import openai, MODEL_VISION, instructions_text


async def image_to_text(img: Image.Image) -> str | None:
    image_buffer = io.BytesIO()
    img.save(image_buffer, format="PNG")
    b64_image = base64.b64encode(image_buffer.getvalue()).decode()

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": instructions_text},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{b64_image}",
                        "detail": "low"
                    }
                },
            ],
        }
    ]
    try:
        response = await openai.chat.completions.create(
            model=MODEL_VISION,
            messages=messages,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] Falha ao extrair texto: {e}")
        return None
