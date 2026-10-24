# Data directory

This folder is intended for Bambara speech data.
Place your raw audio files under `data/audio/train`, `data/audio/val`, and `data/audio/test`.
Each audio file should have a matching transcript in text form.

Example transcript file structure:

```text
data/transcripts/train.txt
# Each line: <relative_audio_path> <transcript>

train/001.wav Aw ka se ka baara duman min ye?
train/002.wav Mali la denw ka caya.
```

The project then creates manifest CSV files for training and evaluation.
