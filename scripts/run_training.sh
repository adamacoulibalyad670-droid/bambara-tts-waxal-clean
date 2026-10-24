#!/usr/bin/env bash
set -e

python -m src.preprocess --manifest data/train_manifest.csv --output_dir data/processed
python -m src.train_tts --config configs/tts_config.yaml --manifest data/train_manifest.csv
python -m src.train_asr --config configs/asr_config.yaml --manifest data/train_manifest.csv
