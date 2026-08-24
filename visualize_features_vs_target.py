"""
visualize_features_vs_target.py

Script para: dado un archivo CSV (o un fichero NumPy .npy) que contiene una matriz
con la primera columna siendo la clase/target a predecir, seleccionar las primeras n
columnas de atributos y visualizarlas en correlación con la clase.

Uso:
    python visualize_features_vs_target.py --input datos.csv --n 5 --out_dir plots

Opciones principales:
    --input  : ruta a CSV (sin encabezados o con encabezados) o .npy con matriz
    --n      : número de atributos (columnas) a seleccionar (enteros >=1)
    --out_dir: carpeta donde guardar los gráficos y CSV resultante (por defecto: plots)
    --sep    : separador para CSV (por defecto ",")
    --header : indicar si el CSV tiene encabezado: yes/no/auto (por defecto auto)

Salida:
    - selected_attributes.csv en la carpeta out_dir
    - para cada atributo: un PNG con la visualización frente a la clase

Requisitos: pandas, numpy, matplotlib, seaborn

Autor: Copilot CLI runtime (AI assistant)
"""

import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional

sns.set(style="whitegrid")


def detect_header(csv_path: str, sep: str) -> Optional[bool]:
    """Intenta detectar si el CSV tiene header leyendo la primera 2 filas.
    Devuelve True (tiene header), False (no tiene), o None si no puede decidir.
    """
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            first = f.readline()
            second = f.readline()
        if not first or not second:
            return None
        # Si la primera fila contiene alguna letra en campos y la segunda fila es numérica,
        # asumir que hay header.
        f1 = first.strip().split(sep)
        f2 = second.strip().split(sep)
        def looks_numeric_list(lst):
            for x in lst:
                x = x.strip()
                if x == '':
                    continue
                try:
                    float(x)
                except Exception:
                    return False
            return True
        if any(not cell.replace('.', '', 1).replace('-', '', 1).isdigit() for cell in f1) and looks_numeric_list(f2):
            return True
        if looks_numeric_list(f1) and looks_numeric_list(f2):
            return False
        return None
    except Exception:
        return None


def load_matrix(input_path: str, sep: str = ',', header: str = 'auto') -> pd.DataFrame:
    p = Path(input_path)
    if p.suffix.lower() == '.npy':
        arr = np.load(str(p))
        df = pd.DataFrame(arr)
        return df
    # CSV path
    if header.lower() not in ('yes', 'no', 'auto'):
        header = 'auto'
    if header.lower() == 'auto':
        detected = detect_header(input_path, sep)
        if detected is True:
            df = pd.read_csv(input_path, sep=sep)
        elif detected is False:
            df = pd.read_csv(input_path, sep=sep, header=None)
        else:
            # fallback: try reading with header, otherwise without
            try:
                df = pd.read_csv(input_path, sep=sep)
            except Exception:
                df = pd.read_csv(input_path, sep=sep, header=None)
    elif header.lower() == 'yes':
        df = pd.read_csv(input_path, sep=sep)
    else:
        df = pd.read_csv(input_path, sep=sep, header=None)
    return df


def ensure_out_dir(path: str):
    os.makedirs(path, exist_ok=True)


def is_categorical(series: pd.Series, threshold_unique_ratio: float = 0.05) -> bool:
    """Determina si una serie es categórica: si es de tipo object o tiene pocos valores únicos
    en relación con su longitud.
    """
    if pd.api.types.is_categorical_dtype(series) or pd.api.types.is_object_dtype(series):
        return True
    nunique = series.nunique(dropna=True)
    if len(series) == 0:
        return True
    if nunique / len(series) < threshold_unique_ratio and nunique < 50:
        return True
    return False


def plot_attribute_vs_target(attr: pd.Series, target: pd.Series, attr_name: str, out_dir: str):
    """Crea y guarda una gráfica que muestre la relación entre attr y target.
    - Si target es categórico -> caja (boxplot) + stripplot
    - Si target es numérico -> scatter + regression line + hist marginal
    """
    plt.figure(figsize=(7, 5))
    combined = pd.DataFrame({"attr": attr, "target": target})
    # eliminar valores missing en ambos
    combined = combined.dropna()
    if combined.empty:
        print(f"Advertencia: no hay datos para {attr_name}")
        return

    if is_categorical(target):
        # target categórico: comparar distribución de attr por cada clase
        try:
            sns.boxplot(x='target', y='attr', data=combined, palette='vlag')
            sns.stripplot(x='target', y='attr', data=combined, color='0.2', size=3, jitter=True)
            plt.title(f"Distribución de {attr_name} por clase")
            plt.xlabel('Clase (target)')
            plt.ylabel(attr_name)
        except Exception as e:
            # fallback simple plot
            combined.boxplot(by='target', column=['attr'])
            plt.title(f"Distribución de {attr_name} por clase")
            plt.suptitle('')
            plt.xlabel('Clase (target)')
            plt.ylabel(attr_name)
    else:
        # target numérico: scatter + regplot
        try:
            sns.regplot(x='attr', y='target', data=combined, scatter_kws={'s': 20, 'alpha':0.6}, line_kws={'color':'red'})
            plt.xlabel(attr_name)
            plt.ylabel('target')
            plt.title(f"{attr_name} vs target (corr={combined['attr'].corr(combined['target']):.3f})")
        except Exception:
            plt.scatter(combined['attr'], combined['target'], s=8, alpha=0.6)
            plt.xlabel(attr_name)
            plt.ylabel('target')
            plt.title(f"{attr_name} vs target")

    fname = Path(out_dir) / f"{attr_name}_vs_target.png"
    plt.tight_layout()
    plt.savefig(str(fname), dpi=150)
    plt.close()

# function for get mutual information between two columns
def get_mutual_information(attr, target):
    if is_categorical(attr):
        attr = attr.astype('category').cat.codes
    if is_categorical(target):
        target = target.astype('category').cat.codes
    return mutual_info_score(attr, target)

def main():
    parser = argparse.ArgumentParser(description='Seleccionar primeras n columnas de atributos y visualizar correlación con la clase (primera columna).')
    parser.add_argument('--input', '-i', required=True, help='Ruta a CSV o .npy con la matriz. Primera columna = target.')
    parser.add_argument('--n', '-n', type=int, required=True, help='Número de atributos a tomar (columnas, empezando desde la segunda columna)')
    parser.add_argument('--out_dir', '-o', default='plots', help='Directorio de salida para gráficos y CSV (default: plots)')
    parser.add_argument('--sep', default=',', help='Separador CSV (por defecto ,)')
    parser.add_argument('--header', default='auto', choices=['yes', 'no', 'auto'], help='Si el CSV tiene header: yes/no/auto (default auto)')
    args = parser.parse_args()

    df = load_matrix(args.input, sep=args.sep, header=args.header)
    if df is None or df.shape[1] < 2:
        raise SystemExit('Error: Se necesita al menos 2 columnas (target + al menos 1 atributo).')

    # Asegurar n válido
    max_attrs_available = df.shape[1] - 1
    if args.n < 1:
        raise SystemExit('Error: --n debe ser >= 1')
    n = min(args.n, max_attrs_available)
    if n < args.n:
        print(f"Nota: solo hay {max_attrs_available} atributos disponibles; tomando {n}.")

    # Renombrar columnas si no hay header para facilitar manejo
    if list(df.columns) and any(isinstance(c, int) for c in df.columns):
        # columnas numéricas -> asignar nombres genéricos
        df = df.copy()
        df.columns = [f'col_{i}' for i in range(1, df.shape[1] + 1)]
    else:
        # mantener nombres; si hay solo nombres vacíos, también renombrar
        if any(pd.isna(c) or str(c).strip() == '' for c in df.columns):
            df = df.copy()
            df.columns = [f'col_{i}' for i in range(1, df.shape[1] + 1)]

    # primera columna = target
    target_col = df.columns[0]
    target = df.iloc[:, 0]
    attrs = df.iloc[:, 1:1 + n]

    ensure_out_dir(args.out_dir)

    # Guardar CSV con las columnas seleccionadas (target + atributos)
    out_csv = Path(args.out_dir) / 'selected_attributes.csv'
    pd.concat([target, attrs], axis=1).to_csv(str(out_csv), index=False)
    print(f"Guardado CSV con target y {n} atributos en: {out_csv}")

    # Para cada atributo, hacer la visualización frente a la clase
    for col in attrs.columns:
        print(f"Generando figura para: {col}")
        try:
            plot_attribute_vs_target(attrs[col], target, str(col), args.out_dir)
        except Exception as e:
            print(f"Error generando figura para {col}: {e}")

    print(f"Listo. Figuras guardadas en: {args.out_dir}")


if __name__ == '__main__':
    main()
