# Narratus ✨📜

> Extraia texto de qualquer parte da tela e ouça uma narração épica em segundos.

Narratus é um utilitário de acessibilidade pensado, inicialmente, para ler cartas, notas e outros documentos encontrados em jogos (RPG, aventura, mistério, etc.). Com alguns atalhos de teclado, o programa recorta uma região da tela, extrai todo o texto usando **GPT‑4o Vision** e o converte em fala com **GPT‑4o TTS** — perfeito para jogadores, criadores de conteúdo e pessoas com deficiência visual.

---

## ✨ Destaques

- **OCR de última geração** com o modelo *gpt‑4.1‑nano* (ou *gpt‑4o‑mini*).
- **Narração natural** via *gpt‑4o‑mini‑tts* (voz padrão: **ash**; tom nobre e heroico).
- **Atalhos globais** configuráveis (Ctrl + 1 para capturar, Ctrl + 2 para sair).
- **Integração nativa** com a Ferramenta de Recorte do Windows (Snipping Tool).
- **Assíncrono e leve** – roda em background sem travar o jogo.

---

## 📂 Estrutura

```text
Narratus/
├── main.py          # ponto de entrada; hotkeys & fluxo principal
├── config.py        # modelos, voz, instruções e constantes globais
├── utils.py         # clipboard, captura de tela e Snipping Tool
├── vision.py        # extração de texto (OCR)
└── speech.py        # síntese de fala (TTS)
```

---

## 🚀 Instalação

> **Requisitos**
> - Windows 10/11 (usamos APIs do Snipping Tool e win32clipboard)
> - Python 3.11 ou superior
> - Chave **OPENAI_API_KEY** com acesso aos modelos Vision & TTS

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
# Edite .env e adicione:
# OPENAI_API_KEY="sua‑chave‑aqui"

# 5. Rode o programa
$ python main.py
```

### Dependências principais

```
openai
numpy
mss
pillow
keyboard
pypiwin32  # win32clipboard
python‑dotenv
```

---

## 🎮 Uso rápido

| Ação | Atalho padrão |
|------|---------------|
| Capturar região da tela & ler | **Ctrl + 1** |
| Encerrar Narratus | **Ctrl + 2** |

1. Inicie **Narratus** (`python main.py`).
2. No jogo (ou qualquer app), pressione **Ctrl + 1**.
3. Selecione a área com texto com o mouse.
4. Aguarde alguns segundos: o texto será lido em voz alta.

> Se pressionar **Esc** durante o recorte, a captura é cancelada.

---

## ⚙️ Configurações

Todas as opções vivem em **`config.py`**.

| Chave | Descrição | Valor padrão |
|-------|-----------|--------------|
| `MODEL_VISION` | Modelo para OCR | `gpt‑4.1‑nano` |
| `MODEL_TTS` | Modelo para TTS | `gpt‑4o‑mini‑tts` |
| `VOICE` | Voz usada na narração | `ash` |
| `instructions_text` | Prompt enviado ao modelo Vision | "Transcreva todo o texto presente na imagem…" |
| `instructions_voice` | Tom/estilo da fala | "Tom: Nobre, heroico…" |
| `CLIP_TIMEOUT` | Tempo máximo (s) para aguardar a imagem no clipboard | `30` |
| `hotkey_start` | Atalho para capturar | `ctrl+1` |
| `hotkey_exit` | Atalho para sair | `ctrl+2` |

Sinta‑se à vontade para trocar a voz, ajustar o tom ou usar modelos diferentes.

---

## 💰 Custos & Limites

- A execução de **Vision** e **TTS** na API da OpenAI gera custos por chamada.
- Certifique‑se de monitorar seu uso no painel da OpenAI.

---

## 🤝 Contribuindo

1. **Fork** este repositório.
2. Crie uma *branch*: `git checkout -b feature/minha-feature`.
3. Faça *commit* das suas alterações: `git commit -m "feat: adiciona minha feature"`.
4. *Push* para a branch: `git push origin feature/minha-feature`.
5. Abra um **Pull Request**.

Contribuições de código, testes, tradução e feedback são muito bem‑vindas.

Sinta‑se convidado(a) a abrir *issues* ou *pull requests*!


---

## 📄 Licença

Distribuído sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
