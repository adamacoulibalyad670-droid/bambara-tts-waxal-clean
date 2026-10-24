# Bambara Speech AI

This repository is a starter project for Bambara speech processing tasks, including:
- TTS (text-to-speech)
- ASR (automatic speech recognition)
- dataset preprocessing for Bambara audio/text corpora

The project is designed to be extended with real Bambara datasets, GPU training, and model deployment.

## Structure

```text
bambara-tts-waxal-clean/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   ├── train_manifest.csv
│   └── test_manifest.csv
├── configs/
│   ├── tts_config.yaml
│   └── asr_config.yaml
├── src/
│   ├── __init__.py
│   ├── dataset.py
│   ├── preprocess.py
│   ├── train_tts.py
│   ├── train_asr.py
│   ├── infer_tts.py
│   └── infer_asr.py
└── models/
    └── .gitkeep
```

## Requirements

Python 3.10+

Install dependencies:

```bash
pip install -r requirements.txt
```

## Data format

Expected CSV manifest columns:

```csv
text,audio_path,speaker_id,language
"Saya ka denw ye" ,"data/audio/train/001.wav","speaker_01","bm"
```

- `text`: transcription in Bambara
- `audio_path`: path to WAV/MP3 audio file
- `speaker_id`: optional speaker label
- `language`: should be `bm`

## Quickstart

1. Put your Bambara audio and transcripts in `data/`
2. Create a manifest CSV using the format above
3. Run preprocessing:

```bash
python -m src.preprocess --manifest data/train_manifest.csv --output_dir data/processed
```

4. Train TTS:

```bash
python -m src.train_tts --config configs/tts_config.yaml
```

5. Train ASR:

```bash
python -m src.train_asr --config configs/asr_config.yaml
```

6. Run inference:

```bash
python -m src.infer_tts --text "Aw ka se ka baara duman min ye?"
python -m src.infer_asr --audio_path data/test.wav
```

## Recommended models

- TTS: XTTS-v2, Coqui TTS, VITS, FastSpeech2
- ASR: Whisper fine-tuning, Wav2Vec2, MMS, HuBERT

## Notes

This is an initial project template. To reach production quality for Bambara speech,
real annotated audio data, preprocessing cleanup, and GPU training are required.

## License

This project is a starter template for experimentation and research.
