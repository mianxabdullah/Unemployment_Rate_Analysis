"""
Data visualization module for unemployment analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.patches import Patch
from config import OUTPUT_DIR, MONTH_NAMES


def set_style():
    """Set visualization style."""
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (14, 6)


def plot_unemployment_trends(national_unemployment, covid_date):
    """Plot national unemployment rate trends over time."""
    set_style()
    fig, ax = plt.subplots(figsize=(15, 6))
    
    ax.plot(national_unemployment['Date'], national_unemployment['Estimated Unemployment Rate (%)'], 
            marker='o', linestyle='-', linewidth=1, markersize=4, alpha=0.6, label='Daily Rate', color='steelblue')
    ax.plot(national_unemployment['Date'], national_unemployment['MA_7'], 
            linestyle='-', linewidth=2, label='7-Day Moving Average', color='orange')
    ax.plot(national_unemployment['Date'], national_unemployment['MA_30'], 
            linestyle='-', linewidth=2, label='30-Day Moving Average', color='red')
    
    ax.axvline(x=covid_date, color='green', linestyle='--', linewidth=2, alpha=0.7, label='COVID-19 Start (Mar 2020)')
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_ylabel('Unemployment Rate (%)', fontsize=12, fontweight='bold')
    ax.set_title('National Unemployment Rate Trends in India Over Time', fontsize=14, fontweight='bold', pad=20)
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    fig.savefig(OUTPUT_DIR / '01_unemployment_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Unemployment trends visualization saved: 01_unemployment_trends.png")


def plot_covid_impact(pre_covid, covid_period, covid_national, avg_increase, percent_change):
    """Plot COVID-19 impact visualizations."""
    set_style()
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # Plot 1: Box plot comparison
    ax1 = axes[0, 0]
    data_to_plot = [pre_covid['Estimated Unemployment Rate (%)'], 
                    covid_period['Estimated Unemployment Rate (%)']]
    bp = ax1.boxplot(data_to_plot, labels=['Pre-COVID\n(Before Mar 2020)', 'COVID Period\n(Mar 2020 onwards)'],
                      patch_artist=True)
    for patch, color in zip(bp['boxes'], ['lightblue', 'lightcoral']):
        patch.set_facecolor(color)
    ax1.set_ylabel('Unemployment Rate (%)', fontweight='bold')
    ax1.set_title('Unemployment Rate Distribution: Pre-COVID vs COVID Period', fontweight='bold')
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Plot 2: Timeline comparison
    ax2 = axes[0, 1]
    pre_covid_dates = pre_covid.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()
    covid_date = pd.Timestamp('2020-03-01')
    ax2.plot(pre_covid_dates['Date'], pre_covid_dates['Estimated Unemployment Rate (%)'], 
             marker='o', linestyle='-', linewidth=1, markersize=3, alpha=0.7, label='Pre-COVID', color='blue')
    ax2.plot(covid_national['Date'], covid_national['Estimated Unemployment Rate (%)'], 
             marker='s', linestyle='-', linewidth=1, markersize=3, alpha=0.7, label='COVID Period', color='red')
    ax2.axvline(x=covid_date, color='green', linestyle='--', linewidth=2, label='COVID Start')
    ax2.set_xlabel('Date', fontweight='bold')
    ax2.set_ylabel('Unemployment Rate (%)', fontweight='bold')
    ax2.set_title('Unemployment Trajectory: Pre-COVID vs COVID', fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
    
    # Plot 3: Monthly comparison
    ax3 = axes[1, 0]
    pre_covid_copy = pre_covid.copy()
    covid_period_copy = covid_period.copy()
    pre_covid_copy['Month'] = pre_covid_copy['Date'].dt.to_period('M')
    covid_period_copy['Month'] = covid_period_copy['Date'].dt.to_period('M')
    monthly_covid = covid_period_copy.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
    
    x_pos = np.arange(len(monthly_covid))
    ax3.bar(x_pos - 0.2, monthly_covid.values, width=0.4, label='COVID Period', color='coral', alpha=0.8)
    ax3.set_xlabel('Months in 2020', fontweight='bold')
    ax3.set_ylabel('Average Unemployment Rate (%)', fontweight='bold')
    ax3.set_title('Monthly Average Unemployment During COVID-19 (2020)', fontweight='bold')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels([str(m) for m in monthly_covid.index], rotation=45)
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Impact statistics
    ax4 = axes[1, 1]
    ax4.axis('off')
    impact_text = f"""
COVID-19 IMPACT SUMMARY

Pre-COVID Average (Before Mar 2020):
  {pre_covid['Estimated Unemployment Rate (%)'].mean():.2f}%

COVID Period Average (Mar 2020 onwards):
  {covid_period['Estimated Unemployment Rate (%)'].mean():.2f}%

Change in Average Unemployment:
  +{avg_increase:.2f} percentage points
  +{percent_change:.2f}% increase

Peak Unemployment During COVID:
  {covid_national['Estimated Unemployment Rate (%)'].max():.2f}% 

Impact Assessment:
  {'Significant negative impact' if percent_change > 50 else 'Moderate impact' if percent_change > 20 else 'Mild impact'}
  on employment rates
"""
    ax4.text(0.1, 0.9, impact_text, transform=ax4.transAxes, fontsize=11,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / '02_covid_impact.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ COVID-19 impact visualization saved: 02_covid_impact.png")


def plot_seasonal_patterns(national_data, df_combined):
    """Plot seasonal patterns and trends."""
    set_style()
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # Plot 1: Monthly average unemployment
    ax1 = axes[0, 0]
    monthly_avg = national_data.groupby('Month')['Estimated Unemployment Rate (%)'].mean()
    colors = plt.cm.viridis(np.linspace(0, 1, 12))
    bars = ax1.bar(range(1, 13), monthly_avg.values, color=colors, alpha=0.8, edgecolor='black')
    ax1.set_xlabel('Month', fontweight='bold', fontsize=11)
    ax1.set_ylabel('Average Unemployment Rate (%)', fontweight='bold', fontsize=11)
    ax1.set_title('Seasonal Pattern: Average Unemployment by Month', fontweight='bold', fontsize=12)
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])
    ax1.grid(True, alpha=0.3, axis='y')
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=9)
    
    # Plot 2: Box plot by month
    ax2 = axes[0, 1]
    monthly_data = [national_data[national_data['Month'] == m]['Estimated Unemployment Rate (%)'].values 
                     for m in range(1, 13)]
    bp = ax2.boxplot(monthly_data, labels=['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
                      patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')
    ax2.set_xlabel('Month', fontweight='bold', fontsize=11)
    ax2.set_ylabel('Unemployment Rate (%)', fontweight='bold', fontsize=11)
    ax2.set_title('Seasonal Variation: Unemployment Distribution by Month', fontweight='bold', fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Plot 3: Quarterly comparison
    ax3 = axes[1, 0]
    quarterly_avg = national_data.groupby('Quarter')['Estimated Unemployment Rate (%)'].mean()
    colors_q = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    bars_q = ax3.bar(range(1, 5), quarterly_avg.values, color=colors_q, alpha=0.8, edgecolor='black', width=0.6)
    ax3.set_xlabel('Quarter', fontweight='bold', fontsize=11)
    ax3.set_ylabel('Average Unemployment Rate (%)', fontweight='bold', fontsize=11)
    ax3.set_title('Seasonal Pattern: Average Unemployment by Quarter', fontweight='bold', fontsize=12)
    ax3.set_xticks(range(1, 5))
    ax3.set_xticklabels(['Q1\n(Jan-Mar)', 'Q2\n(Apr-Jun)', 'Q3\n(Jul-Sep)', 'Q4\n(Oct-Dec)'])
    ax3.grid(True, alpha=0.3, axis='y')
    
    for bar in bars_q:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    # Plot 4: Heatmap or summary
    ax4 = axes[1, 1]
    pivot_data = national_data.pivot_table(values='Estimated Unemployment Rate (%)', 
                                            index='Month', columns='Year', aggfunc='mean')
    if len(pivot_data.columns) > 1:
        sns.heatmap(pivot_data, annot=True, fmt='.2f', cmap='RdYlGn_r', ax=ax4, cbar_kws={'label': 'Unemployment Rate (%)'})
        ax4.set_title('Unemployment Heatmap: Monthly Trends Across Years', fontweight='bold', fontsize=12)
    else:
        ax4.text(0.5, 0.5, 'Limited multi-year data for heatmap analysis', 
                ha='center', va='center', transform=ax4.transAxes, fontsize=12)
        ax4.set_xticks([])
        ax4.set_yticks([])
    
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / '03_seasonal_patterns.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Seasonal patterns visualization saved: 03_seasonal_patterns.png")


def plot_regional_insights(df_combined, pre_covid, covid_period):
    """Plot regional unemployment analysis."""
    set_style()
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    
    # Plot 1: Average unemployment by region
    ax1 = axes[0, 0]
    regional_means = df_combined.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)
    colors_regional = plt.cm.Set3(np.linspace(0, 1, len(regional_means)))
    bars = ax1.barh(range(len(regional_means)), regional_means.values, color=colors_regional, edgecolor='black')
    ax1.set_yticks(range(len(regional_means)))
    ax1.set_yticklabels(regional_means.index)
    ax1.set_xlabel('Average Unemployment Rate (%)', fontweight='bold', fontsize=11)
    ax1.set_title('Average Unemployment Rate by Region (All Time)', fontweight='bold', fontsize=12)
    ax1.grid(True, alpha=0.3, axis='x')
    
    for i, (bar, val) in enumerate(zip(bars, regional_means.values)):
        ax1.text(val + 0.1, i, f'{val:.2f}%', va='center', fontsize=9)
    
    # Plot 2: COVID impact by region
    ax2 = axes[0, 1]
    covid_impacts = []
    regions_list = []
    for region in sorted(df_combined['Region'].unique()):
        region_covid = covid_period[covid_period['Region'] == region]['Estimated Unemployment Rate (%)']
        if len(region_covid) > 0:
            covid_impacts.append(region_covid.mean())
            regions_list.append(region)
    
    bars2 = ax2.bar(range(len(regions_list)), covid_impacts, color=colors_regional[:len(regions_list)], 
                    alpha=0.8, edgecolor='black')
    ax2.set_xticks(range(len(regions_list)))
    ax2.set_xticklabels(regions_list, rotation=45, ha='right')
    ax2.set_ylabel('Average Unemployment Rate (%)', fontweight='bold', fontsize=11)
    ax2.set_title('Average Unemployment During COVID-19 by Region', fontweight='bold', fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%', ha='center', va='bottom', fontsize=9)
    
    # Plot 3: Regional trends over time
    ax3 = axes[1, 0]
    covid_date = pd.Timestamp('2020-03-01')
    for region in df_combined['Region'].unique():
        region_data = df_combined[df_combined['Region'] == region].groupby('Date')['Estimated Unemployment Rate (%)'].mean()
        ax3.plot(region_data.index, region_data.values, marker='o', linestyle='-', 
                linewidth=2, markersize=3, label=region, alpha=0.7)
    
    ax3.axvline(x=covid_date, color='green', linestyle='--', linewidth=2, alpha=0.7, label='COVID Start')
    ax3.set_xlabel('Date', fontweight='bold', fontsize=11)
    ax3.set_ylabel('Unemployment Rate (%)', fontweight='bold', fontsize=11)
    ax3.set_title('Unemployment Trends by Region Over Time', fontweight='bold', fontsize=12)
    ax3.legend(loc='best', fontsize=9)
    ax3.grid(True, alpha=0.3)
    plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
    
    # Plot 4: Area-wise comparison
    ax4 = axes[1, 1]
    if 'Area' in df_combined.columns:
        area_data = df_combined.groupby(['Date', 'Area'])['Estimated Unemployment Rate (%)'].mean().reset_index()
        for area in df_combined['Area'].unique():
            area_subset = area_data[area_data['Area'] == area]
            ax4.plot(area_subset['Date'], area_subset['Estimated Unemployment Rate (%)'], 
                    marker='o', linestyle='-', linewidth=2, markersize=3, label=area, alpha=0.7)
        
        ax4.axvline(x=covid_date, color='green', linestyle='--', linewidth=2, alpha=0.7, label='COVID Start')
        ax4.set_xlabel('Date', fontweight='bold', fontsize=11)
        ax4.set_ylabel('Unemployment Rate (%)', fontweight='bold', fontsize=11)
        ax4.set_title('Unemployment Trends: Rural vs Urban Areas', fontweight='bold', fontsize=12)
        ax4.legend(loc='best', fontsize=10)
        ax4.grid(True, alpha=0.3)
        plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45)
    else:
        ax4.text(0.5, 0.5, 'Area data not available', 
                ha='center', va='center', transform=ax4.transAxes, fontsize=12)
        ax4.set_xticks([])
        ax4.set_yticks([])
    
    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / '04_regional_insights.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Regional insights visualization saved: 04_regional_insights.png")


def plot_comprehensive_dashboard(df_combined, national_unemployment, national_data, pre_covid, covid_period):
    """Create comprehensive summary dashboard."""
    set_style()
    fig = plt.figure(figsize=(18, 12))
    gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)
    
    covid_date = pd.Timestamp('2020-03-01')
    overall_avg = df_combined['Estimated Unemployment Rate (%)'].mean()
    overall_max = df_combined['Estimated Unemployment Rate (%)'].max()
    overall_min = df_combined['Estimated Unemployment Rate (%)'].min()
    pre_covid_avg = pre_covid['Estimated Unemployment Rate (%)'].mean()
    covid_avg = covid_period['Estimated Unemployment Rate (%)'].mean()
    
    # Plot 1: Main trend
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.plot(national_unemployment['Date'], national_unemployment['Estimated Unemployment Rate (%)'], 
            marker='o', linestyle='-', linewidth=1.5, markersize=4, alpha=0.6, color='steelblue')
    ax1.plot(national_unemployment['Date'], national_unemployment['MA_30'], 
            linestyle='-', linewidth=3, label='30-Day MA', color='red', alpha=0.8)
    ax1.axvline(x=covid_date, color='green', linestyle='--', linewidth=2.5, alpha=0.7, label='COVID Start')
    ax1.set_title('National Unemployment Rate - Overall Trend', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Unemployment Rate (%)', fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Key statistics
    ax2 = fig.add_subplot(gs[0, 2])
    ax2.axis('off')
    avg_increase = covid_avg - pre_covid_avg
    percent_change = (avg_increase / pre_covid_avg * 100) if pre_covid_avg != 0 else 0
    stats_text = f"""
KEY STATISTICS

Overall Avg: {overall_avg:.2f}%
Peak: {overall_max:.2f}%
Trough: {overall_min:.2f}%

Pre-COVID: {pre_covid_avg:.2f}%
COVID Avg: {covid_avg:.2f}%

Impact: +{avg_increase:.2f}pp
        +{percent_change:.1f}%

Data Period:
{df_combined['Date'].min().strftime('%b %Y')} to
{df_combined['Date'].max().strftime('%b %Y')}
"""
    ax2.text(0.05, 0.95, stats_text, transform=ax2.transAxes, fontsize=10,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    # Plot 3: Monthly seasonality
    ax3 = fig.add_subplot(gs[1, 0])
    monthly_avg_plot = df_combined.groupby(df_combined['Date'].dt.month)['Estimated Unemployment Rate (%)'].mean()
    ax3.bar(range(1, 13), monthly_avg_plot.values, color='skyblue', alpha=0.8, edgecolor='black')
    ax3.set_title('Seasonal Pattern by Month', fontweight='bold', fontsize=11)
    ax3.set_xlabel('Month')
    ax3.set_ylabel('Avg Rate (%)')
    ax3.set_xticks(range(1, 13))
    ax3.set_xticklabels(['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'])
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Regional comparison
    ax4 = fig.add_subplot(gs[1, 1])
    regional_avg = df_combined.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()
    ax4.barh(range(len(regional_avg)), regional_avg.values, color='lightcoral', alpha=0.8, edgecolor='black')
    ax4.set_yticks(range(len(regional_avg)))
    ax4.set_yticklabels(regional_avg.index, fontsize=9)
    ax4.set_title('Unemployment by Region', fontweight='bold', fontsize=11)
    ax4.set_xlabel('Avg Rate (%)')
    ax4.grid(True, alpha=0.3, axis='x')
    
    # Plot 5: Pre vs COVID
    ax5 = fig.add_subplot(gs[1, 2])
    box_data = [pre_covid['Estimated Unemployment Rate (%)'], covid_period['Estimated Unemployment Rate (%)']]
    bp = ax5.boxplot(box_data, labels=['Pre-COVID', 'COVID'], patch_artist=True)
    bp['boxes'][0].set_facecolor('lightgreen')
    bp['boxes'][1].set_facecolor('lightcoral')
    ax5.set_title('Pre-COVID vs COVID Comparison', fontweight='bold', fontsize=11)
    ax5.set_ylabel('Unemployment Rate (%)')
    ax5.grid(True, alpha=0.3, axis='y')
    
    # Plot 6: Monthly trend
    ax6 = fig.add_subplot(gs[2, :])
    monthly_trend = df_combined.groupby(df_combined['Date'].dt.to_period('M'))['Estimated Unemployment Rate (%)'].mean()
    months_x = range(len(monthly_trend))
    colors_monthly = ['red' if pd.Period(date, 'M') >= pd.Period(covid_date, 'M') else 'blue' 
                      for date in monthly_trend.index]
    ax6.bar(months_x, monthly_trend.values, color=colors_monthly, alpha=0.7, edgecolor='black')
    ax6.set_title('Monthly Average Unemployment Rate Trend', fontweight='bold', fontsize=12)
    ax6.set_xlabel('Month', fontweight='bold')
    ax6.set_ylabel('Unemployment Rate (%)', fontweight='bold')
    ax6.set_xticks(range(0, len(monthly_trend), max(1, len(monthly_trend)//12)))
    ax6.set_xticklabels([str(monthly_trend.index[i]) for i in range(0, len(monthly_trend), max(1, len(monthly_trend)//12))], 
                         rotation=45, ha='right', fontsize=9)
    legend_elements = [Patch(facecolor='blue', alpha=0.7, label='Pre-COVID'),
                       Patch(facecolor='red', alpha=0.7, label='COVID Period')]
    ax6.legend(handles=legend_elements, loc='upper left')
    ax6.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Unemployment Analysis Dashboard - India 2019-2020', 
                fontsize=15, fontweight='bold', y=0.995)
    fig.savefig(OUTPUT_DIR / '05_comprehensive_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Comprehensive dashboard saved: 05_comprehensive_dashboard.png")
