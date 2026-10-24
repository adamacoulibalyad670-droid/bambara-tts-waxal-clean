import argparse
from pathlib import Path
import pandas as pd

from src.utils import ensure_dir, normalize_text


def parse_args():
    parser = argparse.ArgumentParser(description="Preprocess Bambara speech manifest and audio metadata")
    parser.add_argument("--manifest", type=str, required=True, help="CSV manifest path")
    parser.add_argument("--output_dir", type=str, default="data/processed", help="Directory for processed data")
    return parser.parse_args()


def main():
    args = parse_args()
    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    df = pd.read_csv(manifest_path)
    required = {"text", "audio_path", "speaker_id", "language"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Manifest missing required columns: {sorted(missing)}")

    df["text"] = df["text"].apply(normalize_text)
    df = df[df["text"].str.len() > 0].copy()

    output_dir = ensure_dir(args.output_dir)
    out_path = output_dir / "manifest_processed.csv"
    df.to_csv(out_path, index=False)
    print(f"Processed manifest saved to: {out_path}")
    print(f"Rows kept: {len(df)}")


if __name__ == "__main__":
    main()
