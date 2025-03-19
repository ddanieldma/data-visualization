from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
RAW_DIR = DATA_DIR / 'raw'
INTERIM_DIR = DATA_DIR / 'interim'
DATA_MUNICIPIOS_NAME = RAW_DIR / 'data_municipios.csv.gz'
DATA_VIOLENCIA_MORTES_NAME = RAW_DIR / 'data_violencia_mortes.csv.gz'
DATA_POLICIA_NAME = RAW_DIR / 'data_policia.csv'
DATA_MUNICIPIOS_PARQUET = RAW_DIR / 'data_municipios.parquet'
DATA_VIOLENCIA_MORTES_PARQUET = RAW_DIR / 'data_violencia_mortes.parquet'
DATA_POLICIA_PARQUET = RAW_DIR / 'data_policia.parquet'

def save_dataframe_to_parquet(df: pd.DataFrame, file_path: Path):
    df.to_parquet(file_path)

def read_and_save_to_parquet(parquet_file_path: Path, csv_file_path, is_df_policia: bool = True):
    if parquet_file_path.exists():
        print(f"Reading parquet: {parquet_file_path}")
        return pd.read_parquet(parquet_file_path)
    else:
        print(f"Reading csv: {csv_file_path}")
        if is_df_policia:
            df = pd.read_csv(csv_file_path, sep=';', encoding='latin-1')
        else:
            df = pd.read_csv(csv_file_path)

    print(f"Writing: {parquet_file_path}")
    save_dataframe_to_parquet(df, parquet_file_path)
    return df

df_municipios = read_and_save_to_parquet(DATA_MUNICIPIOS_PARQUET, DATA_MUNICIPIOS_NAME)
df_violencia_mortes = read_and_save_to_parquet(DATA_VIOLENCIA_MORTES_PARQUET, DATA_VIOLENCIA_MORTES_NAME)
df_policia = read_and_save_to_parquet(DATA_POLICIA_PARQUET, DATA_POLICIA_NAME, True)