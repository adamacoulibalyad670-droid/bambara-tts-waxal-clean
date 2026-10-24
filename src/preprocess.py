import argparse
from pathlib import Path
import pandas as pd

from src import ensure_dir


def parse_args():
    parser = argparse.ArgumentParser(description="Preprocess Bambara speech data")
    parser.add_argument("--manifest", type=str, required=True, help="CSV manifest path")
    parser.add_argument("--output_dir", type=str, default="data/processed", help="Processed output directory")
    parser.add_argument("--min_duration", type=float, default=0.3, help="Minimum audio duration in seconds")
    return parser.parse_args()


def normalize_text(text):
    if text is None:
        return ""
    return " ".join(str(text).strip().split())


def main():
    args = parse_args()
    manifest_path = Path(args.manifest)
    output_dir = ensure_dir(args.output_dir)

    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest file not found: {manifest_path}")

    df = pd.read_csv(manifest_path)
    df["text"] = df["text"].apply(normalize_text)

    processed = df[["text", "audio_path", "speaker_id", "language"]].copy()
    processed.to_csv(output_dir / "manifest_processed.csv", index=False)
    print(f"Processed rows: {len(processed)}")
    print(f"Saved to: {output_dir / 'manifest_processed.csv'}")


if __name__ == "__main__":
    main()
