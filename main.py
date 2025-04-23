import asyncio
import threading
import keyboard

from config import CLIP_TIMEOUT, hotkey_start, hotkey_exit, MODEL_VISION
from utils import clear_clipboard, wait_clip_image, open_snipping_tool
from vision import image_to_text
from speech import speak


async def capture_and_read():
    await asyncio.to_thread(clear_clipboard)

    open_snipping_tool()
    print("[INFO] Arraste para recortar ou ESC para cancelar.")

    captured_image = await asyncio.to_thread(wait_clip_image, CLIP_TIMEOUT)
    if captured_image is None:
        print("[INFO] Snip cancelado.")
        return

    print(f"[INFO] Extraindo texto via {MODEL_VISION}…")
    extracted_text = await image_to_text(captured_image)

    if not extracted_text:
        print("[WARN] Nenhum texto reconhecido.")
        return

    print(f"[INFO] Texto extraído: {extracted_text}")
    print("[INFO] Sintetizando fala…")
    await speak(extracted_text)
    print("[INFO] Fala concluída.\n")
    print(f"→ Pressione [{hotkey_start}] para capturar uma região da tela e realizar a leitura.")
    print(f"→ Pressione [{hotkey_exit}] para encerrar.")

def start_hotkey_loop() -> None:
    keyboard.add_hotkey(hotkey_start, lambda: threading.Thread(target=lambda: asyncio.run(capture_and_read()), daemon=True).start())
    print("→ Narratus iniciado! 🧙‍📜")
    print(f"→ Pressione [{hotkey_start}] para capturar uma região da tela e realizar a leitura.")
    print(f"→ Pressione [{hotkey_exit}] para encerrar.")
    keyboard.wait(hotkey_exit)

if __name__ == "__main__":
    start_hotkey_loop()