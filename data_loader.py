"""
Data loading and exploration module
"""
import pandas as pd
from config import FILE1, FILE2


def load_data():
    """Load both unemployment datasets."""
    print("Loading unemployment datasets...")
    
    df1 = pd.read_csv(FILE1)
    df2 = pd.read_csv(FILE2)
    
    return df1, df2


def explore_data(df1, df2):
    """Explore and display basic information about datasets."""
    print("="*80)
    print("Dataset 1: Unemployment in India.csv")
    print("="*80)
    print(f"Shape: {df1.shape}")
    print(f"\nColumns: {df1.columns.tolist()}")
    print(f"\nFirst few rows:")
    print(df1.head())
    print(f"\nData types:\n{df1.dtypes}")
    print(f"\nMissing Values:\n{df1.isnull().sum()}")
    print(f"\nBasic Statistics:\n{df1.describe()}")
    
    print("\n" + "="*80)
    print("Dataset 2: Unemployment_Rate_upto_11_2020.csv")
    print("="*80)
    print(f"Shape: {df2.shape}")
    print(f"\nColumns: {df2.columns.tolist()}")
    print(f"\nFirst few rows:")
    print(df2.head())
    print(f"\nData types:\n{df2.dtypes}")
    print(f"\nMissing Values:\n{df2.isnull().sum()}")
    print(f"\nBasic Statistics:\n{df2.describe()}")
