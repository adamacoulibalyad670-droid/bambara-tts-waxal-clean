import argparse
import yaml
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Train a Bambara ASR model")
    parser.add_argument("--config", type=str, default="configs/asr_config.yaml")
    parser.add_argument("--manifest", type=str, default="data/train_manifest.csv")
    return parser.parse_args()


def main():
    args = parse_args()
    config_path = Path(args.config)
    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    print("ASR training config loaded:")
    print(config)
    print(f"Manifest: {args.manifest}")
    print("This is a starter ASR training template for Bambara speech.")
    print("Replace this placeholder with Whisper, Wav2Vec2, or MMS fine-tuning.")


if __name__ == "__main__":
    main()
