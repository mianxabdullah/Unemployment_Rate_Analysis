# Unemployment Analysis in India

Comprehensive Python-based analysis of unemployment rate data in India, examining trends, COVID-19 impact, seasonal patterns, and regional variations to inform economic and social policies.

## Project Structure

```
d:\CodeAlpha\Task-Unemployment\
├── config.py                 # Configuration and constants
├── data_loader.py            # Data loading and exploration functions
├── data_cleaner.py           # Data cleaning and preprocessing functions
├── analyzer.py               # Analysis functions (trends, COVID, seasonal, regional)
├── visualizer.py             # Data visualization functions
├── main.py                   # Main orchestration script
├── README.md                 # This file
├── dataset/                  # Input data directory
│   ├── Unemployment in India.csv
│   └── Unemployment_Rate_upto_11_2020.csv
└── results/                  # Output directory for visualizations
    ├── 01_unemployment_trends.png
    ├── 02_covid_impact.png
    ├── 03_seasonal_patterns.png
    ├── 04_regional_insights.png
    └── 05_comprehensive_dashboard.png
```

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels

Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
```

## Running the Analysis

Execute the main analysis script:
```bash
python main.py
```

This will:
1. Load both CSV datasets
2. Explore and display basic statistics
3. Clean and preprocess the data
4. Perform comprehensive analysis including:
   - Overall unemployment trends
   - COVID-19 impact analysis
   - Seasonal pattern identification
   - Regional disparities
5. Generate 5 detailed visualizations
6. Display policy recommendations

## Module Descriptions

### config.py
Contains all configuration constants and paths:
- Data file paths
- COVID-19 reference date
- Month and quarter names
- Visualization settings

### data_loader.py
Functions for loading and exploring raw data:
- `load_data()` - Load both CSV files
- `explore_data()` - Display basic information and statistics

### data_cleaner.py
Functions for data cleaning and preprocessing:
- `clean_dataset1()` - Clean Unemployment in India.csv
- `clean_dataset2()` - Clean Unemployment_Rate_upto_11_2020.csv
- `merge_datasets()` - Combine both datasets

### analyzer.py
Core analysis functions:
- `analyze_trends()` - Overall unemployment trends
- `analyze_covid_impact()` - COVID-19 period analysis
- `analyze_seasonal_patterns()` - Seasonal trend identification
- `analyze_regional_insights()` - Regional comparison
- `summarize_key_findings()` - Key insights summary

### visualizer.py
Visualization functions:
- `plot_unemployment_trends()` - National trend visualization
- `plot_covid_impact()` - COVID-19 impact charts
- `plot_seasonal_patterns()` - Seasonal analysis plots
- `plot_regional_insights()` - Regional analysis charts
- `plot_comprehensive_dashboard()` - Complete analysis dashboard

### main.py
Main orchestration script that:
- Coordinates all analysis steps
- Executes the complete pipeline
- Generates output visualizations
- Displays policy recommendations

## Key Findings

### Overall Trends
- Unemployment rates tracked from May 2019 to November 2020
- Multiple Indian regions covered in analysis
- Clear peaks and troughs identified

### COVID-19 Impact
- Significant spike in unemployment during March-May 2020 lockdown
- Pre-COVID average vs COVID period average comparison
- Regional variation in COVID impact

### Seasonal Patterns
- Cyclical variations observed throughout the year
- Highest unemployment in certain months
- Quarterly analysis provided

### Regional Disparities
- Significant regional inequality in employment opportunities
- Rural vs Urban differences (if available in data)
- Regional recovery patterns

## Policy Recommendations

Based on analysis findings, recommendations include:

1. **Emergency Crisis Response** - Support for affected workers
2. **Seasonal Employment Programs** - Off-season employment initiatives
3. **Regional Development** - Targeted industrial investment
4. **Rural-Urban Balance** - Infrastructure and entrepreneurship support
5. **Structural Reforms** - Long-term system resilience
6. **Priority Population Focus** - Support for vulnerable groups

## Output Visualizations

### 01_unemployment_trends.png
- National unemployment rate over time
- 7-day and 30-day moving averages
- COVID-19 start date marker

### 02_covid_impact.png
- Pre-COVID vs COVID period comparison
- Box plot distribution analysis
- Monthly trends during lockdown
- Impact assessment summary

### 03_seasonal_patterns.png
- Monthly average unemployment
- Seasonal variation distribution
- Quarterly comparison
- Year-over-month heatmap (if available)

### 04_regional_insights.png
- Average unemployment by region
- Regional COVID-19 impact
- Regional trends over time
- Rural vs Urban comparison (if available)

### 05_comprehensive_dashboard.png
- Complete summary dashboard
- All key metrics at a glance
- Multiple perspectives on unemployment data

## Data Sources

- **Unemployment in India.csv** - Monthly unemployment data by region
- **Unemployment_Rate_upto_11_2020.csv** - Extended data through November 2020

Both datasets contain:
- Region/State information
- Date information
- Estimated unemployment rates (%)
- Employed population estimates
- Labour participation rates

## Author Notes

This modular Python structure provides:
- **Maintainability** - Easy to update individual components
- **Reusability** - Functions can be used independently
- **Scalability** - Simple to add new analysis functions
- **Documentation** - Clear function documentation and comments
- **Professional Structure** - Industry-standard Python project layout

## Future Enhancements

Possible improvements:
- Add predictive models for future unemployment trends
- Include additional demographic breakdowns
- Generate interactive dashboards with Plotly
- Add statistical significance testing
- Create PDF report generation
- Implement automated data validation

## License

This analysis is provided for educational and policy research purposes.
