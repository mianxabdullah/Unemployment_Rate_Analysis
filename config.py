"""
Configuration and constants for Unemployment Analysis
"""
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "dataset"
OUTPUT_DIR = PROJECT_ROOT / "results"

# Data files
FILE1 = DATA_DIR / "Unemployment in India.csv"
FILE2 = DATA_DIR / "Unemployment_Rate_upto_11_2020.csv"

# COVID-19 reference date
COVID_START_DATE = "2020-03-01"

# Month names for reference
MONTH_NAMES = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Quarter names
QUARTER_NAMES = ['Q1 (Jan-Mar)', 'Q2 (Apr-Jun)', 'Q3 (Jul-Sep)', 'Q4 (Oct-Dec)']

# Visualization settings
FIGURE_STYLE = "whitegrid"
FIGURE_SIZE = (14, 6)
DPI = 100

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)
