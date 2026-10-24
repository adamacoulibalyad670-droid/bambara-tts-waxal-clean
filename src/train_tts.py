import argparse
from pathlib import Path
import yaml


def parse_args():
    parser = argparse.ArgumentParser(description="Train a Bambara TTS model")
    parser.add_argument("--config", type=str, default="configs/tts_config.yaml", help="TTS config file")
    parser.add_argument("--manifest", type=str, default="data/train_manifest.csv", help="Training manifest CSV")
    return parser.parse_args()


def main():
    args = parse_args()
    cfg_path = Path(args.config)
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    print("TTS training configuration:")
    print(config)
    print(f"Manifest: {args.manifest}")
    print("This starter script prepares the training pipeline for Bambara TTS.")
    print("Use a framework such as XTTS-v2, Coqui TTS, VITS, or FastSpeech2 for actual model training.")


if __name__ == "__main__":
    main()
