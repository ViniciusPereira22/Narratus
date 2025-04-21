import time
import subprocess
from mss import mss
import win32clipboard
from PIL import ImageGrab, Image


def clear_clipboard():
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
    except Exception as e:
        print(f"[WARN] Falha ao limpar clipboard: {e}")

def wait_clip_image(timeout: int) -> Image.Image | None:
    t0 = time.time()
    while time.time() - t0 < timeout:
        img = ImageGrab.grabclipboard()
        if isinstance(img, Image.Image):
            return img
        time.sleep(0.2)
    return None

def grab_screen() -> Image.Image:
    with mss() as sct:
        monitor = sct.monitors[0]
        raw = sct.grab(monitor)
        img = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")
        return img

def open_snipping_tool():
    subprocess.Popen(["explorer", "ms-screenclip:"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
