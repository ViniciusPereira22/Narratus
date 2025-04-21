from config import openai, MODEL_TTS, VOICE, instructions_voice
from openai.helpers import LocalAudioPlayer

async def speak(text: str) -> None:
    async with openai.audio.speech.with_streaming_response.create(
        model=MODEL_TTS,
        voice=VOICE,
        input=text,
        instructions=instructions_voice,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)
