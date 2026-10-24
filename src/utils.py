from pathlib import Path


def ensure_dir(path):
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def normalize_text(text):
    if text is None:
        return ""
    return " ".join(str(text).strip().split())


def safe_audio_path(path):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Audio file not found: {path}")
    return str(p)
