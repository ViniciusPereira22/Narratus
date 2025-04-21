import os
from dotenv import load_dotenv


load_dotenv(override=True)

# Modelos OpenAI
MODEL_VISION = "gpt-4.1-nano"  # or "gpt-4o-mini"
MODEL_TTS = "gpt-4o-mini-tts"

# Configuração de áudio
VOICE = "ash"
instructions_text = "Transcreva todo o texto presente na imagem. Apenas texto sem formatação."
instructions_voice = "Tom: Nobre, heroico e formal, capturando a essência dos cavaleiros medievais e das jornadas épicas."

# Constantes gerais
CLIP_TIMEOUT = 30  # segundos

# Hotkeys
hotkey_start = "ctrl+1"
hotkey_exit = "ctrl+2"

# OpenAI client setup
from openai import AsyncOpenAI
openai = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY não definida! Verifique o arquivo .env")
