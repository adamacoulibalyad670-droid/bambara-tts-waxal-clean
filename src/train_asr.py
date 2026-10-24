import argparse
from pathlib import Path
import yaml


def parse_args():
    parser = argparse.ArgumentParser(description="Train a Bambara ASR model")
    parser.add_argument("--config", type=str, default="configs/asr_config.yaml", help="ASR config file")
    parser.add_argument("--manifest", type=str, default="data/train_manifest.csv", help="Training manifest CSV")
    return parser.parse_args()


def main():
    args = parse_args()
    cfg_path = Path(args.config)
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    print("ASR training configuration:")
    print(config)
    print(f"Manifest: {args.manifest}")
    print("This starter script prepares the training pipeline for Bambara ASR.")
    print("Use Whisper, Wav2Vec2, MMS, or HuBERT fine-tuning for actual training.")


if __name__ == "__main__":
    main()
