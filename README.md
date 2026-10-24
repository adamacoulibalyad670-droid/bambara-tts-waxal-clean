# Bambara Speech AI

A practical starter project for Bambara speech processing with:
- TTS (Text-to-Speech)
- ASR (Automatic Speech Recognition)
- data preprocessing and manifest generation
- model training and inference entry points

This repository is designed to be extended with real Bambara datasets and then trained on GPU/Colab.

## Repository structure

```text
bambara-tts-waxal-clean/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── audio/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── transcripts/
│   │   ├── train.txt
│   │   ├── val.txt
│   │   └── test.txt
│   ├── train_manifest.csv
│   ├── val_manifest.csv
│   ├── test_manifest.csv
│   └── README.md
├── configs/
│   ├── tts_config.yaml
│   └── asr_config.yaml
├── scripts/
│   ├── build_manifest.py
│   └── run_training.sh
├── src/
│   ├── __init__.py
│   ├── dataset.py
│   ├── preprocess.py
│   ├── train_tts.py
│   ├── train_asr.py
│   ├── infer_tts.py
│   ├── infer_asr.py
│   └── utils.py
├── notebooks/
│   └── .gitkeep
├── models/
│   └── .gitkeep
└── outputs/
    └── .gitkeep
```

## Quick start

1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or .venv\Scripts\activate  # Windows
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Prepare dataset

Put WAV files in `data/audio/train` and corresponding transcripts in `data/transcripts/train.txt`.

Example transcript file:

```text
Aw ka bonya ka baara di.
Mali la denw ka caya.
```

4. Build manifest files

```bash
python scripts/build_manifest.py \
  --audio_dir data/audio/train \
  --transcript_file data/transcripts/train.txt \
  --output data/train_manifest.csv
```

5. Preprocess dataset

```bash
python -m src.preprocess --manifest data/train_manifest.csv --output_dir data/processed
```

6. Train TTS model

```bash
python -m src.train_tts --config configs/tts_config.yaml --manifest data/train_manifest.csv
```

7. Train ASR model

```bash
python -m src.train_asr --config configs/asr_config.yaml --manifest data/train_manifest.csv
```

8. Run inference

```bash
python -m src.infer_tts --text "Aw ka se ka baara duman min ye?"
python -m src.infer_asr --audio_path data/audio/test/example.wav
```

## Dataset schema

The manifest CSV should contain columns similar to this:

```csv
text,audio_path,speaker_id,language
"Aw ka denw ye","data/audio/train/001.wav","speaker_01","bm"
"Mali la bagan ye","data/audio/train/002.wav","speaker_01","bm"
```

## Recommended models

For Bambara speech tasks, good starting points are:

- TTS:
  - XTTS-v2
  - Coqui TTS
  - VITS
  - FastSpeech2

- ASR:
  - Whisper fine-tuning
  - Wav2Vec2
  - MMS
  - HuBERT

## Notes

This repository is a strong starter project for Bambara speech research. To train a production-ready model, you will need:
- a real Bambara dataset with audio + validated transcripts
- cleaned text normalization
- GPU or Colab with sufficient RAM and VRAM
- careful validation and evaluation

## License

This project is released as a starter template for research, experimentation, and local development.
