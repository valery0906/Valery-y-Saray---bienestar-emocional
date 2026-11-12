import pandas as pd
from pathlib import Path

#cargar datos
ruta="https://github.com/valery0906/Valery-y-Saray---bienestar-emocional/raw/refs/heads/main/EmoSPeech_phase_2_train_public.csv"
df = pd.read_csv(ruta)
archivo_descargado = Path(__file__).with_name("EmoSPeech_phase_2_train_public.csv")
df.to_csv(archivo_descargado, index=False)
print(f"CSV descargado en: {archivo_descargado}")

print("="*50)
print(df.head())
print("="*50)

print("="*50)
print(df.info())
print("="*50)

print("="*50)
print(df.describe())
print("-"*50)

print("="*50)
print(df.columns)
print("-"*50)

print("="*50)
print(df.isnull().sum())
print("-"*50)

print("="*50)
print(df.shape)  # filas columnas
print("-"*50)

print("="*50)
print(df['sentiment'])
print("-"*50)

print("="*50)
print(df[['sentiment','text']])
print("-"*50)

print("="*50)
print(df[df['sentiment'] == 'anger'])
print("-"*50)