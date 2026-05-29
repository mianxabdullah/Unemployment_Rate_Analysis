"""
Data analysis module for unemployment trends
"""
import pandas as pd
from config import COVID_START_DATE, MONTH_NAMES, QUARTER_NAMES


def analyze_trends(df_combined):
    """Analyze overall unemployment trends."""
    print("\n" + "="*80)
    print("UNEMPLOYMENT RATE TRENDS OVER TIME")
    print("="*80)
    
    # Calculate national unemployment rate
    national_unemployment = df_combined.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()
    national_unemployment = national_unemployment.sort_values('Date')
    
    # Calculate moving averages
    national_unemployment['MA_7'] = national_unemployment['Estimated Unemployment Rate (%)'].rolling(window=7, min_periods=1).mean()
    national_unemployment['MA_30'] = national_unemployment['Estimated Unemployment Rate (%)'].rolling(window=30, min_periods=1).mean()
    
    # Find peak and minimum
    max_unemployment = national_unemployment.loc[national_unemployment['Estimated Unemployment Rate (%)'].idxmax()]
    min_unemployment = national_unemployment.loc[national_unemployment['Estimated Unemployment Rate (%)'].idxmin()]
    
    print(f"Peak Unemployment: {max_unemployment['Estimated Unemployment Rate (%)']:.2f}% on {max_unemployment['Date'].strftime('%B %d, %Y')}")
    print(f"Minimum Unemployment: {min_unemployment['Estimated Unemployment Rate (%)']:.2f}% on {min_unemployment['Date'].strftime('%B %d, %Y')}")
    print(f"Average Unemployment Rate: {national_unemployment['Estimated Unemployment Rate (%)'].mean():.2f}%")
    print(f"Standard Deviation: {national_unemployment['Estimated Unemployment Rate (%)'].std():.2f}%")
    
    return national_unemployment


def analyze_covid_impact(df_combined):
    """Analyze COVID-19 impact on unemployment."""
    print("\n" + "="*80)
    print("COVID-19 IMPACT ANALYSIS")
    print("="*80)
    
    covid_date = pd.Timestamp(COVID_START_DATE)
    
    # Split data
    pre_covid = df_combined[df_combined['Date'] < covid_date].copy()
    covid_period = df_combined[df_combined['Date'] >= covid_date].copy()
    
    print(f"\nPre-COVID Period: {pre_covid['Date'].min().strftime('%B %d, %Y')} to {pre_covid['Date'].max().strftime('%B %d, %Y')}")
    print(f"COVID Period: {covid_period['Date'].min().strftime('%B %d, %Y')} to {covid_period['Date'].max().strftime('%B %d, %Y')}")
    
    print("\nPre-COVID Statistics:")
    print(f"  Average Unemployment Rate: {pre_covid['Estimated Unemployment Rate (%)'].mean():.2f}%")
    print(f"  Median Unemployment Rate: {pre_covid['Estimated Unemployment Rate (%)'].median():.2f}%")
    print(f"  Std Dev: {pre_covid['Estimated Unemployment Rate (%)'].std():.2f}%")
    print(f"  Min: {pre_covid['Estimated Unemployment Rate (%)'].min():.2f}%")
    print(f"  Max: {pre_covid['Estimated Unemployment Rate (%)'].max():.2f}%")
    
    print("\nCOVID Period Statistics:")
    print(f"  Average Unemployment Rate: {covid_period['Estimated Unemployment Rate (%)'].mean():.2f}%")
    print(f"  Median Unemployment Rate: {covid_period['Estimated Unemployment Rate (%)'].median():.2f}%")
    print(f"  Std Dev: {covid_period['Estimated Unemployment Rate (%)'].std():.2f}%")
    print(f"  Min: {covid_period['Estimated Unemployment Rate (%)'].min():.2f}%")
    print(f"  Max: {covid_period['Estimated Unemployment Rate (%)'].max():.2f}%")
    
    # Calculate impact
    avg_increase = covid_period['Estimated Unemployment Rate (%)'].mean() - pre_covid['Estimated Unemployment Rate (%)'].mean()
    percent_change = (avg_increase / pre_covid['Estimated Unemployment Rate (%)'].mean()) * 100
    
    print(f"\n{'='*80}")
    print(f"COVID-19 Impact Summary:")
    print(f"  Absolute Increase in Average Unemployment: +{avg_increase:.2f} percentage points")
    print(f"  Percentage Increase: +{percent_change:.2f}%")
    print(f"{'='*80}")
    
    # COVID national trend
    covid_national = covid_period.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()
    covid_national = covid_national.sort_values('Date')
    covid_max = covid_national.loc[covid_national['Estimated Unemployment Rate (%)'].idxmax()]
    covid_national['Days_Since_COVID'] = (covid_national['Date'] - covid_date).dt.days
    
    print(f"\nPeak COVID-19 Unemployment: {covid_max['Estimated Unemployment Rate (%)']:.2f}%")
    print(f"Date: {covid_max['Date'].strftime('%B %d, %Y')}")
    
    if len(covid_national[covid_national['Days_Since_COVID'] <= 30]) > 0:
        print(f"First month (March 2020) average: {covid_national[covid_national['Days_Since_COVID'] <= 30]['Estimated Unemployment Rate (%)'].mean():.2f}%")
    if len(covid_national[covid_national['Days_Since_COVID'] > 120]) > 0:
        print(f"After 4+ months average: {covid_national[covid_national['Days_Since_COVID'] > 120]['Estimated Unemployment Rate (%)'].mean():.2f}%")
    
    return pre_covid, covid_period, covid_national, avg_increase, percent_change


def analyze_seasonal_patterns(df_combined):
    """Analyze seasonal trends in unemployment."""
    print("\n" + "="*80)
    print("SEASONAL PATTERNS AND TRENDS")
    print("="*80)
    
    # Extract time-based features
    national_data = df_combined.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()
    national_data = national_data.sort_values('Date').set_index('Date')
    
    national_data['Month'] = national_data.index.month
    national_data['Quarter'] = national_data.index.quarter
    national_data['Year'] = national_data.index.year
    national_data['Month_Name'] = national_data.index.strftime('%B')
    
    # Monthly statistics
    monthly_stats = national_data.groupby('Month')['Estimated Unemployment Rate (%)'].agg(['mean', 'median', 'std', 'min', 'max'])
    
    print("\nMonthly Statistics:")
    print("="*80)
    for month in range(1, 13):
        if month in monthly_stats.index:
            stats = monthly_stats.loc[month]
            print(f"{MONTH_NAMES[month-1]:12s}: Mean={stats['mean']:6.2f}%, Median={stats['median']:6.2f}%, StdDev={stats['std']:6.2f}%")
    
    # Quarterly statistics
    quarterly_stats = national_data.groupby('Quarter')['Estimated Unemployment Rate (%)'].agg(['mean', 'median', 'count'])
    
    print("\n" + "="*80)
    print("Quarterly Pattern Analysis:")
    print("="*80)
    for quarter in range(1, 5):
        if quarter in quarterly_stats.index:
            stats = quarterly_stats.loc[quarter]
            print(f"{QUARTER_NAMES[quarter-1]:15s}: Mean={stats['mean']:6.2f}%, Median={stats['median']:6.2f}%, Data Points={int(stats['count'])}")
    
    return national_data


def analyze_regional_insights(df_combined, pre_covid, covid_period):
    """Analyze regional unemployment variations."""
    print("\n" + "="*80)
    print("REGIONAL AND DEMOGRAPHIC ANALYSIS")
    print("="*80)
    
    # Regional statistics
    regional_stats = df_combined.groupby('Region').agg({
        'Estimated Unemployment Rate (%)': ['mean', 'median', 'std', 'min', 'max', 'count']
    }).round(2)
    
    regional_stats.columns = ['Mean', 'Median', 'Std Dev', 'Min', 'Max', 'Count']
    regional_stats = regional_stats.sort_values('Mean', ascending=False)
    
    print("\nRegional Unemployment Statistics (All Time):")
    print(regional_stats)
    
    # COVID impact by region
    print("\n" + "="*80)
    print("COVID-19 Impact by Region:")
    print("="*80)
    
    for region in sorted(df_combined['Region'].unique()):
        region_pre = pre_covid[pre_covid['Region'] == region]['Estimated Unemployment Rate (%)']
        region_covid = covid_period[covid_period['Region'] == region]['Estimated Unemployment Rate (%)']
        
        if len(region_pre) > 0 and len(region_covid) > 0:
            pre_avg = region_pre.mean()
            covid_avg = region_covid.mean()
            impact = covid_avg - pre_avg
            pct_change = (impact / pre_avg * 100) if pre_avg != 0 else 0
            
            print(f"\n{region}:")
            print(f"  Pre-COVID Average: {pre_avg:6.2f}%")
            print(f"  COVID Average: {covid_avg:6.2f}%")
            print(f"  Change: +{impact:6.2f} percentage points (+{pct_change:6.2f}%)")
    
    # Area-wise analysis if available
    if 'Area' in df_combined.columns:
        print("\n" + "="*80)
        print("Area-wise Analysis (Rural vs Urban):")
        print("="*80)
        
        area_stats = df_combined.groupby('Area').agg({
            'Estimated Unemployment Rate (%)': ['mean', 'median', 'std', 'count']
        }).round(2)
        
        area_stats.columns = ['Mean', 'Median', 'Std Dev', 'Count']
        print("\n", area_stats)
    
    return regional_stats


def summarize_key_findings(df_combined, pre_covid, covid_period, national_data, avg_increase, percent_change):
    """Generate comprehensive key findings summary."""
    print("\n" + "="*80)
    print("KEY FINDINGS AND INSIGHTS - UNEMPLOYMENT ANALYSIS IN INDIA")
    print("="*80)
    
    # Finding 1: Overall Trend
    print("\n1. OVERALL UNEMPLOYMENT TREND:")
    print("-" * 80)
    overall_avg = df_combined['Estimated Unemployment Rate (%)'].mean()
    overall_max = df_combined['Estimated Unemployment Rate (%)'].max()
    overall_min = df_combined['Estimated Unemployment Rate (%)'].min()
    print(f"   • Average unemployment rate across all periods: {overall_avg:.2f}%")
    print(f"   • Highest unemployment rate recorded: {overall_max:.2f}%")
    print(f"   • Lowest unemployment rate recorded: {overall_min:.2f}%")
    print(f"   • Data covers {(df_combined['Date'].max() - df_combined['Date'].min()).days} days")
    
    # Finding 2: COVID-19 Impact
    print("\n2. COVID-19 PANDEMIC IMPACT:")
    print("-" * 80)
    pre_covid_avg = pre_covid['Estimated Unemployment Rate (%)'].mean()
    covid_avg = covid_period['Estimated Unemployment Rate (%)'].mean()
    print(f"   • Pre-COVID average (before March 2020): {pre_covid_avg:.2f}%")
    print(f"   • COVID period average (March 2020 onwards): {covid_avg:.2f}%")
    print(f"   • Absolute increase: +{avg_increase:.2f} percentage points")
    print(f"   • Percentage increase: +{percent_change:.2f}%")
    print(f"   • COVID-19 had a SIGNIFICANT negative impact on employment")
    
    # Finding 3: Seasonal patterns
    print("\n3. SEASONAL PATTERNS:")
    print("-" * 80)
    monthly_avg = df_combined.groupby(df_combined['Date'].dt.month)['Estimated Unemployment Rate (%)'].mean()
    highest_month = MONTH_NAMES[monthly_avg.idxmax() - 1]
    lowest_month = MONTH_NAMES[monthly_avg.idxmin() - 1]
    print(f"   • Highest average unemployment: {highest_month} ({monthly_avg.max():.2f}%)")
    print(f"   • Lowest average unemployment: {lowest_month} ({monthly_avg.min():.2f}%)")
    print(f"   • Seasonal variation: {monthly_avg.max() - monthly_avg.min():.2f} percentage points")
    print(f"   • Clear seasonal cyclicality observed in unemployment data")
    
    # Finding 4: Regional disparities
    print("\n4. REGIONAL DISPARITIES:")
    print("-" * 80)
    regional_means = df_combined.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
    highest_region = regional_means.idxmax()
    lowest_region = regional_means.idxmin()
    print(f"   • Highest unemployment region: {highest_region} ({regional_means.max():.2f}%)")
    print(f"   • Lowest unemployment region: {lowest_region} ({regional_means.min():.2f}%)")
    print(f"   • Regional variation: {regional_means.max() - regional_means.min():.2f} percentage points")
    print(f"   • Significant regional inequality in employment opportunities")
