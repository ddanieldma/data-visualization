from pathlib import Path

ROOT_DIR = Path().resolve().parent
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / 'raw'
INTERIM_DIR = DATA_DIR / 'interim'

df