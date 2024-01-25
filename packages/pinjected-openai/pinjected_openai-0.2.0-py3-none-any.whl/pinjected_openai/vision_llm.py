"""
TODO impl
"""
import base64
import io
import os
from pathlib import Path

from PIL.Image import Image
from loguru import logger
from pinjected import injected, Injected, instances, instance
from openai import AsyncOpenAI


def to_content(img: Image):
    # convert Image into jpeg bytes
    jpg_bytes = io.BytesIO()
    img.convert('RGB').save(jpg_bytes, format='jpeg', quality=95)
    b64_image = base64.b64encode(jpg_bytes.getvalue()).decode('utf-8')
    mb_of_b64 = len(b64_image) / 1024 / 1024
    logger.info(f"image size: {mb_of_b64:.2f} MB in base64.")
    return {
        "type": 'image_url',
        "image_url": f"data:image/jpeg;base64,{b64_image}"
    }


@injected
async def a_vision_llm__gpt4(
        async_openai_client: AsyncOpenAI,
        a_repeat_for_rate_limit,
        /,
        text: str,
        images: list[Image]) -> str:
    assert isinstance(async_openai_client, AsyncOpenAI)

    for img in images:
        assert isinstance(img, Image), f"image is not Image, but {type(img)}"

    async def task():
        chat_completion = await async_openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": 'text',
                            "text": text
                        },
                        *[to_content(img) for img in images]
                    ]
                }
            ],
            model="gpt-4-vision-preview",
            max_tokens=2048
        )
        return chat_completion

    chat_completion = await a_repeat_for_rate_limit(task)
    res = chat_completion.choices[0].message.content
    assert isinstance(res, str)
    logger.info(f"vision_llm__gpt4 result:\n{res}")
    return res


@injected
async def a_llm__gpt4_turbo(
        async_openai_client: AsyncOpenAI,
        a_repeat_for_rate_limit,
        /,
        text: str,
        max_tokens=1024 * 128
) -> str:
    assert isinstance(async_openai_client, AsyncOpenAI)

    async def task():
        chat_completion = await async_openai_client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": 'text',
                            "text": text
                        },
                    ]
                }
            ],
            model="gpt-4-1106-peview",
            max_tokens=max_tokens
        )
        return chat_completion

    chat_completion = await a_repeat_for_rate_limit(task)
    res = chat_completion.choices[0].message.content
    assert isinstance(res, str)
    logger.info(f"vision_llm__gpt4 result:\n{res}")
    return res


@instance
def async_openai_client(openai_api_key) -> AsyncOpenAI:
    return AsyncOpenAI(
        api_key=openai_api_key,
    )


@instance
def openai_api_key() -> str:
    if (api_key := os.environ.get('OPENAI_API_KEY', None)) is None:
        api_key = Path(os.path.expanduser("~/.openai_api_key.txt")).read_text().strip()
    return api_key


test_vision_llm__gpt4 = a_vision_llm__gpt4(
    text="What are inside this image?",
    images=Injected.list(
    ),
)
"""
('The image appears to be an advertisement or an informational graphic about '
 'infant and newborn nutrition. It features a baby with light-colored hair who '
 'is lying down and holding onto a baby bottle, seemingly feeding themselves. '
 'The baby is looking directly towards the camera. The image uses a soft pink '
 'color palette, which is common for baby-related products or information. '
 'There are texts that read "Infant & Newborn Nutrition" and "Absolutely New," '
 'along with the word "PINGUIN" at the top, which could be a brand name or '
 "logo. The layout and design of this image suggest it's likely used for "
 'marketing purposes or as part of educational material regarding baby '
 'nutrition.')
"""

__meta_design__ = instances()
