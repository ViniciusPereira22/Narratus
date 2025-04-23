import os
from openai import AsyncOpenAI
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv(override=True)

# Provedor de TTS: "openai" (padrão) ou "elevenlabs"
TTS_PROVIDER = "openai"

# Modelos OpenAI
MODEL_VISION = "gpt-4.1-nano"  # "gpt-4.1-nano" (padrão) or "gpt-4o-mini"
VISION_IMAGE_DETAIL = "low" # "high" or "low"

# Configuração de áudio da OpenAI
VOICE_OPENAI = "ash"
MODEL_TTS_OPENAI = "gpt-4o-mini-tts"
instructions_text = "Transcreva todo o texto presente na imagem. Apenas texto sem formatação."
instructions_voice = "Tom: Nobre, heroico e formal, capturando a essência dos cavaleiros medievais e das jornadas épicas."

# Configuração de áudio da ElevenLabs
VOICE_ELEVENLABS = "NOpBlnGInO9m6vDvFkFC"
MODEL_TTS_ELEVENLABS = "eleven_flash_v2_5" # "eleven_flash_v2_5" or "eleven_multilingual_v2"

# Constantes gerais
CLIP_TIMEOUT = 30  # segundos

# Hotkeys
hotkey_start = "ctrl+1"
hotkey_exit = "ctrl+2"

if TTS_PROVIDER not in ["openai", "elevenlabs"]:
    raise ValueError(f"TTS_PROVIDER inválido: {TTS_PROVIDER}")

# OpenAI client setup
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY não definida! Verifique o arquivo .env")
openai = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
# ElevenLabs client setup
if TTS_PROVIDER == "elevenlabs":
    if not os.environ.get("ELEVENLABS_API_KEY"):
        raise ValueError("ELEVENLABS_API_KEY não definida! Verifique o arquivo .env")
    elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

