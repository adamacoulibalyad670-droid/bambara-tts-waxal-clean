#!/usr/bin/env python3
import argparse
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Build a CSV manifest for Bambara speech data")
    parser.add_argument("--audio_dir", type=str, required=True, help="Directory containing audio files")
    parser.add_argument("--transcript_file", type=str, required=True, help="Text file containing one transcript per line")
    parser.add_argument("--output", type=str, required=True, help="Output CSV manifest path")
    parser.add_argument("--delimiter", type=str, default="\t", help="Delimiter used in transcript file")
    return parser.parse_args()


def main():
    args = parse_args()
    audio_dir = Path(args.audio_dir)
    transcript_file = Path(args.transcript_file)
    output_file = Path(args.output)

    if not audio_dir.exists():
        raise FileNotFoundError(f"Audio directory not found: {audio_dir}")
    if not transcript_file.exists():
        raise FileNotFoundError(f"Transcript file not found: {transcript_file}")

    lines = transcript_file.read_text(encoding="utf-8").strip().splitlines()
    rows = []
    for line in lines:
        if not line.strip():
            continue
        if args.delimiter in line:
            left, right = line.split(args.delimiter, 1)
            audio_rel = left.strip()
            transcript = right.strip()
        else:
            audio_rel = line.strip()
            transcript = ""
        audio_path = (audio_dir / audio_rel).resolve()
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file missing: {audio_path}")
        rows.append({
            "text": transcript,
            "audio_path": str(audio_path),
            "speaker_id": "speaker_01",
            "language": "bm",
        })

    manifest = []
    for r in rows:
        manifest.append(r)

    if not manifest:
        raise ValueError("No rows found. Check transcript file format.")

    output_file.parent.mkdir(parents=True, exist_ok=True)
    import pandas as pd
    df = pd.DataFrame(manifest)
    df.to_csv(output_file, index=False)
    print(f"Wrote {len(df)} rows to {output_file}")


if __name__ == "__main__":
    main()
