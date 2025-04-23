from config import TTS_PROVIDER

if TTS_PROVIDER == "openai": 
    from openai.helpers import LocalAudioPlayer
    from config import openai, MODEL_TTS_OPENAI, VOICE_OPENAI, instructions_voice
elif TTS_PROVIDER == "elevenlabs": 
    from elevenlabs import play
    from config import elevenlabs, MODEL_TTS_ELEVENLABS, VOICE_ELEVENLABS
else: 
    raise ValueError(f"TTS_PROVIDER inválido: {TTS_PROVIDER}")


async def speak(text: str) -> None:
    if TTS_PROVIDER == "openai":
        async with openai.audio.speech.with_streaming_response.create(
            model=MODEL_TTS_OPENAI,
            voice=VOICE_OPENAI,
            input=text,
            instructions=instructions_voice,
            response_format="pcm",
        ) as response:
            await LocalAudioPlayer().play(response)

    elif TTS_PROVIDER == "elevenlabs":
        audio = elevenlabs.text_to_speech.convert(
            model_id=MODEL_TTS_ELEVENLABS,
            voice_id=VOICE_ELEVENLABS,
            text=text,
            voice_settings={
                "stability": 0.3,
                "similarity_boost": 0.2,
                "speed": 0.85
            }
        )
        play(audio, use_ffmpeg=False)
                    

