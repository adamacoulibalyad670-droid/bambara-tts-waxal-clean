import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Run ASR inference on a Bambara audio sample")
    parser.add_argument("--audio_path", type=str, required=True, help="Path to audio file")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"ASR inference input: {args.audio_path}")
    print("This is a placeholder. Connect this script to your trained Bambara ASR model.")


if __name__ == "__main__":
    main()
