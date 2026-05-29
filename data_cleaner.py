"""
Data cleaning and preprocessing module
"""
import pandas as pd


def clean_dataset1(df1):
    """Clean Dataset 1: Unemployment in India.csv"""
    print("\nCleaning Dataset 1...")
    
    df1_clean = df1.copy()
    
    # Remove leading/trailing spaces from column names
    df1_clean.columns = df1_clean.columns.str.strip()
    
    # Also strip spaces from data in the Date column
    df1_clean['Date'] = df1_clean['Date'].str.strip()
    
    # Convert Date column to datetime
    df1_clean['Date'] = pd.to_datetime(df1_clean['Date'], format='%d-%m-%Y')
    
    # Convert unemployment rate to numeric
    df1_clean['Estimated Unemployment Rate (%)'] = pd.to_numeric(
        df1_clean['Estimated Unemployment Rate (%)'], 
        errors='coerce'
    )
    
    # Remove duplicates
    df1_clean = df1_clean.drop_duplicates()
    
    # Handle missing values
    df1_clean = df1_clean.dropna(subset=['Date', 'Estimated Unemployment Rate (%)'])
    
    print(f"Dataset 1 Cleaned:")
    print(f"  Shape: {df1_clean.shape}")
    print(f"  Date Range: {df1_clean['Date'].min()} to {df1_clean['Date'].max()}")
    print(f"  Unemployment Rate Range: {df1_clean['Estimated Unemployment Rate (%)'].min():.2f}% to {df1_clean['Estimated Unemployment Rate (%)'].max():.2f}%")
    print(f"  Unique Regions: {df1_clean['Region'].nunique()}")
    print(f"  Regions: {sorted(df1_clean['Region'].unique())}")
    
    return df1_clean


def clean_dataset2(df2):
    """Clean Dataset 2: Unemployment_Rate_upto_11_2020.csv"""
    print("\nCleaning Dataset 2...")
    
    df2_clean = df2.copy()
    
    # Remove leading/trailing spaces from column names
    df2_clean.columns = df2_clean.columns.str.strip()
    
    # Also strip spaces from data in the Date column
    df2_clean['Date'] = df2_clean['Date'].str.strip()
    
    # Convert Date column to datetime
    df2_clean['Date'] = pd.to_datetime(df2_clean['Date'], format='%d-%m-%Y')
    
    # Convert unemployment rate to numeric
    df2_clean['Estimated Unemployment Rate (%)'] = pd.to_numeric(
        df2_clean['Estimated Unemployment Rate (%)'], 
        errors='coerce'
    )
    
    # Remove duplicates
    df2_clean = df2_clean.drop_duplicates()
    
    # Handle missing values
    df2_clean = df2_clean.dropna(subset=['Date', 'Estimated Unemployment Rate (%)'])
    
    print(f"Dataset 2 Cleaned:")
    print(f"  Shape: {df2_clean.shape}")
    print(f"  Date Range: {df2_clean['Date'].min()} to {df2_clean['Date'].max()}")
    print(f"  Unemployment Rate Range: {df2_clean['Estimated Unemployment Rate (%)'].min():.2f}% to {df2_clean['Estimated Unemployment Rate (%)'].max():.2f}%")
    print(f"  Unique Regions: {df2_clean['Region'].nunique()}")
    
    return df2_clean


def merge_datasets(df1_clean, df2_clean):
    """Merge both cleaned datasets for comprehensive analysis."""
    print("\nMerging datasets...")
    
    # Combine both datasets
    df_combined = pd.concat([df1_clean, df2_clean], ignore_index=True)
    
    # Sort by date and region
    df_combined = df_combined.sort_values(['Region', 'Date']).reset_index(drop=True)
    
    # Remove any resulting duplicates
    df_combined = df_combined.drop_duplicates(subset=['Region', 'Date'], keep='first')
    
    print(f"Combined Dataset:")
    print(f"  Total Shape: {df_combined.shape}")
    print(f"  Date Range: {df_combined['Date'].min()} to {df_combined['Date'].max()}")
    print(f"  Total Unique Regions: {df_combined['Region'].nunique()}")
    print(f"  Date range spans {(df_combined['Date'].max() - df_combined['Date'].min()).days} days")
    print(f"  From: {df_combined['Date'].min().strftime('%B %Y')} to {df_combined['Date'].max().strftime('%B %Y')}")
    
    return df_combined
