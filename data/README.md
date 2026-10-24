# Data directory

This folder is where you place:
- raw audio files
- transcripts
- manifest CSV files
- processed features

Example structure:

```text
data/
├── audio/
│   ├── train/
│   └── val/
├── transcripts/
│   ├── train.txt
│   └── val.txt
├── train_manifest.csv
├── test_manifest.csv
└── processed/
```

For Bambara work, make sure the text is normalized and cleaned before model training.
