# Narratus ✨📜

> Extraia texto de qualquer parte da tela e ouça uma narração épica em segundos.

Narratus é um utilitário de acessibilidade pensado, inicialmente, para ler cartas, notas e outros documentos encontrados em jogos (RPG, aventura, mistério etc.). Com alguns atalhos de teclado, o programa recorta uma região da tela, extrai todo o texto usando **GPT‑4o Vision** e o converte em fala usando via **OpenAI** ou **ElevenLabs** — perfeito para jogadores, criadores de conteúdo e pessoas com deficiência visual.

---

## ✨ Destaques

- **OCR de última geração** com o modelo *gpt‑4.1‑nano* (ou *gpt‑4o‑mini*).
- **Narração natural** via:
  - **OpenAI TTS** (*gpt‑4o‑mini‑tts*, voz padrão: **ash**, tom nobre e heroico)  
  - **ElevenLabs TTS** (*eleven_flash_v2_5* ou *eleven_multilingual_v2*)  
- **Provedor de TTS configurável** (`openai` ou `elevenlabs`).  
- **Atalhos globais** configuráveis (Ctrl + 1 para capturar, Ctrl + 2 para sair).
- **Integração nativa** com a Ferramenta de Recorte do Windows (Snipping Tool).
- **Assíncrono e leve** – roda em background sem travar o jogo.

---

## 📂 Estrutura

```
Narratus/
├── main.py          # ponto de entrada; hotkeys & fluxo principal
├── config.py        # modelos, voz, instruções e constantes globais
├── utils.py         # clipboard, captura de tela e Snipping Tool
├── vision.py        # extração de texto (OCR)
└── speech.py        # síntese de fala (TTS)
```

---

## 🚀 Instalação

> **Requisitos**
> - Windows 10/11 (usa APIs do Snipping Tool e win32clipboard)
> - Python 3.11 ou superior
> - Chaves de API: **OPENAI_API_KEY** (obrigatório) e **ELEVENLABS_API_KEY** (opcional, só se usar ElevenLabs para gerar a fala)

```bash
# 1. Clone o repositório
$ git clone https://github.com/seu‑usuario/Narratus.git
$ cd Narratus

# 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
$ python -m venv .venv
$ .venv\Scripts\activate      # PowerShell / CMD

# 3. Instale as dependências
$ pip install -r requirements.txt

# 4. Configure suas variáveis de ambiente
$ copy .env.example .env        # ou crie .env manualmente
# Edite .env e preencha as chaves:
# OPENAI_API_KEY="sua_chave_openai"
# (Opcional) ELEVENLABS_API_KEY="sua_chave_elevenlabs"  

# 5. Rode o programa
$ python main.py
```

### Exemplo de `.env`

```dotenv
# OpenAI API Key (Vision e TTS)
OPENAI_API_KEY="YOUR_OPENAI_KEY"

# (Opcional) ElevenLabs API Key para TTS via ElevenLabs
ELEVENLABS_API_KEY="YOUR_ELEVENLABS_KEY"
```

### Dependências principais

```
openai
elevenlabs
numpy
mss
pillow
keyboard
pypiwin32  # win32clipboard
python-dotenv
sounddevice
soundfile
pyaudio
```

---

## 🎮 Uso rápido

| Ação                                | Atalho padrão |
|-------------------------------------|---------------|
| Capturar região da tela & ler       | **Ctrl + 1**  |
| Encerrar Narratus                   | **Ctrl + 2**  |

1. Inicie **Narratus** (`python main.py`).  
2. No jogo (ou em qualquer aplicação), pressione **Ctrl + 1**.
3. Selecione a área com texto com o mouse.
4. Aguarde alguns segundos: o texto será lido em voz alta.

> Pressionar **Esc** durante o recorte cancela a captura.

---

## ⚙️ Configurações

Todas as opções ficam em `config.py`. Você pode trocar o provedor de TTS, voz, modelo e outros parâmetros.

| Chave                  | Descrição                                              | Valor padrão                |
|------------------------|--------------------------------------------------------|-----------------------------|
| TTS_PROVIDER           | Provedor de TTS (`"openai"` ou `"elevenlabs"`)         | `"elevenlabs"`              |
| MODEL_VISION           | Modelo para OCR                                        | `"gpt-4.1-nano"`            |
| VISION_IMAGE_DETAIL    | Nível de detalhe da imagem (`"low"` ou `"high"`)       | `"low"`                     |
| VOICE_OPENAI           | Voz usada no TTS da OpenAI                             | `"ash"`                     |
| MODEL_TTS_OPENAI       | Modelo para TTS da OpenAI                              | `"gpt-4o-mini-tts"`         |
| VOICE_ELEVENLABS       | Voice ID para TTS da ElevenLabs                        | (ID definido em config.py)  |
| MODEL_TTS_ELEVENLABS   | Modelo para TTS da ElevenLabs                          | `"eleven_flash_v2_5"`       |
| instructions_text      | Prompt enviado ao modelo Vision                        | Transcreve todo o texto...  |
| instructions_voice     | Estilo de narração (instruções ao modelo TTS)          | "Tom: Nobre, heroico..."    |
| CLIP_TIMEOUT           | Tempo máximo (s) para aguardar imagem no clipboard     | `30`                        |
| hotkey_start           | Atalho para iniciar captura                            | `"ctrl+1"`                  |
| hotkey_exit            | Atalho para encerrar aplicação                         | `"ctrl+2"`                  |

---

## 💰 Custos & Limites

- O uso dos serviços **OpenAI Vision** e **TTS** gera cobranças por chamada de API.  
- Se optar pelo ElevenLabs, também haverá custos conforme seu plano.  
- Monitore seu consumo nos painéis de controle das respectivas plataformas.

---

## 🤝 Contribuindo

1. **Fork** deste repositório.
2. Crie uma *branch*: `git checkout -b feature/minha-feature`.
3. Faça *commit* das suas alterações: `git commit -m "feat: descrição da feature"`.
4. *Push* para sua branch: `git push origin feature/minha-feature`.
5. Abra um **Pull Request**.

Bug reports, sugestões de melhoria, traduções e testes são muito bem‑vindos!
Sinta‑se convidado(a) a abrir *issues* ou *pull requests*!

---

## 📄 Licença

Distribuído sob a licença **MIT**. Consulte [LICENSE](LICENSE) para mais detalhes.