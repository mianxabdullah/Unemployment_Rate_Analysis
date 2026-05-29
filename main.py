"""
Main execution script for Unemployment Analysis in India

This script orchestrates the complete unemployment analysis pipeline including:
- Data loading and exploration
- Data cleaning and preprocessing
- Comprehensive analysis (trends, COVID impact, seasonal patterns, regional insights)
- Visualizations and dashboard creation
- Policy recommendations
"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data, explore_data
from data_cleaner import clean_dataset1, clean_dataset2, merge_datasets
from analyzer import (
    analyze_trends, analyze_covid_impact, analyze_seasonal_patterns,
    analyze_regional_insights, summarize_key_findings
)
from visualizer import (
    plot_unemployment_trends, plot_covid_impact, plot_seasonal_patterns,
    plot_regional_insights, plot_comprehensive_dashboard
)
from config import COVID_START_DATE, OUTPUT_DIR


def print_header(title):
    """Print formatted header."""
    print("\n" + "="*80)
    print(title.center(80))
    print("="*80)


def print_policy_recommendations():
    """Print policy recommendations and conclusions."""
    print_header("POLICY RECOMMENDATIONS AND CONCLUSIONS")
    
    recommendations = """
Based on the comprehensive analysis of unemployment data in India (2019-2020),
the following policy recommendations are proposed to address employment challenges:

1. IMMEDIATE CRISIS RESPONSE MEASURES
   ─────────────────────────────────────────────────────────────────────────
   Issue: COVID-19 led to a dramatic spike in unemployment rates
   
   Recommended Actions:
   • Emergency employment generation programs targeting affected sectors
   • Direct financial support/subsidies for affected workers
   • Accelerated skill development and vocational training programs
   • Support for micro, small & medium enterprises (MSMEs) to retain workforce
   • Enhanced unemployment insurance and social safety nets
   
   Expected Outcome: Cushion the impact on vulnerable populations and maintain
                    income levels during economic downturns

2. SEASONAL EMPLOYMENT MANAGEMENT
   ─────────────────────────────────────────────────────────────────────────
   Issue: Clear seasonal patterns show fluctuating unemployment across months
   
   Recommended Actions:
   • Develop off-season employment programs for seasonal workers
   • Create agricultural diversification initiatives
   • Establish flexible workforce programs aligned with seasonal demand
   • Promote inter-seasonal skill development
   • Create buffer employment programs during high unemployment months
   
   Expected Outcome: Smooth employment throughout the year and reduce
                    seasonal joblessness

3. REGIONAL DEVELOPMENT INITIATIVES
   ─────────────────────────────────────────────────────────────────────────
   Issue: Significant regional disparities in unemployment rates observed
   
   Recommended Actions:
   • Targeted industrial development in high unemployment regions
   • Infrastructure investment to attract manufacturing/service sectors
   • Regional skill training aligned with local industry needs
   • Decentralized business incubation and startup support
   • Regional labor market information systems for better job matching
   
   Expected Outcome: Reduce regional inequality and create local employment
                    opportunities

4. RURAL vs URBAN EMPLOYMENT BALANCE
   ─────────────────────────────────────────────────────────────────────────
   Issue: Potential disparities between rural and urban employment
   
   Recommended Actions:
   • Strengthen rural infrastructure and connectivity
   • Promote rural entrepreneurship and agro-business
   • Digital skilling for rural populations
   • Fair wages and labor standards in rural areas
   • Agriculture modernization for productivity and employment
   
   Expected Outcome: Create sustainable rural employment and reduce urban
                    migration pressure

5. STRUCTURAL REFORMS FOR LONG-TERM RESILIENCE
   ─────────────────────────────────────────────────────────────────────────
   Issue: System vulnerability exposed during pandemic
   
   Recommended Actions:
   • Labor market formalization to expand social security coverage
   • Digital transformation and automation training
   • Build diversified economy reducing sector dependency
   • Strengthen labor market information systems
   • Promote gig economy regulation and worker protection
   
   Expected Outcome: Build a resilient employment system prepared for
                    future shocks

6. PRIORITY POPULATION FOCUS
   ─────────────────────────────────────────────────────────────────────────
   Issue: Vulnerable populations typically more affected by economic shocks
   
   Recommended Actions:
   • Special employment programs for youth and first-time job seekers
   • Women empowerment through skill training and entrepreneurship
   • Support for disabled population integration into workforce
   • Minority community economic development initiatives
   • Disadvantaged community targeted employment programs
   
   Expected Outcome: Inclusive economic growth with equitable opportunities
"""
    print(recommendations)
    
    print("\n" + "="*80)
    print("CONCLUSION")
    print("="*80)
    
    conclusion = """
This analysis reveals that India faced significant unemployment challenges,
particularly due to the COVID-19 pandemic. The data shows:

• Unemployment spiked sharply during pandemic lockdowns (March-May 2020)
• Regional variations suggest unequal distribution of opportunities
• Seasonal patterns indicate cyclical employment challenges
• Recovery trends suggest gradual but ongoing improvement

The government must implement a comprehensive, multi-pronged approach combining:
   1. Immediate relief for pandemic-affected workers
   2. Structural reforms for long-term resilience
   3. Regional development to address disparities
   4. Social safety nets for vulnerable populations
   5. Skill development aligned with emerging sectors

By implementing these recommendations, India can build a more resilient,
inclusive employment system capable of weathering economic shocks while
providing opportunities for all citizens.

Implementation Timeline:
   • Short-term (0-6 months): Emergency response and relief measures
   • Medium-term (6-18 months): Program acceleration and scaling
   • Long-term (18+ months): Structural reforms and system building
"""
    print(conclusion)


def main():
    """Execute complete unemployment analysis pipeline."""
    
    print_header("UNEMPLOYMENT ANALYSIS IN INDIA")
    print("Analyzing Trends, COVID-19 Impact, and Policy Insights")
    
    # STEP 1: Load and Explore Data
    print_header("STEP 1: LOADING AND EXPLORING DATA")
    df1, df2 = load_data()
    explore_data(df1, df2)
    
    # STEP 2: Data Cleaning
    print_header("STEP 2: DATA CLEANING AND PREPROCESSING")
    df1_clean = clean_dataset1(df1)
    df2_clean = clean_dataset2(df2)
    df_combined = merge_datasets(df1_clean, df2_clean)
    
    # STEP 3: Analysis
    print_header("STEP 3: COMPREHENSIVE ANALYSIS")
    
    # Analyze trends
    national_unemployment = analyze_trends(df_combined)
    
    # Analyze COVID impact
    pre_covid, covid_period, covid_national, avg_increase, percent_change = analyze_covid_impact(df_combined)
    
    # Analyze seasonal patterns
    national_data = analyze_seasonal_patterns(df_combined)
    
    # Analyze regional insights
    regional_stats = analyze_regional_insights(df_combined, pre_covid, covid_period)
    
    # Summarize key findings
    summarize_key_findings(df_combined, pre_covid, covid_period, national_data, avg_increase, percent_change)
    
    # STEP 4: Visualizations
    print_header("STEP 4: CREATING VISUALIZATIONS")
    covid_date = pd.Timestamp(COVID_START_DATE)
    
    print("\nGenerating visualizations...")
    plot_unemployment_trends(national_unemployment, covid_date)
    plot_covid_impact(pre_covid, covid_period, covid_national, avg_increase, percent_change)
    plot_seasonal_patterns(national_data, df_combined)
    plot_regional_insights(df_combined, pre_covid, covid_period)
    plot_comprehensive_dashboard(df_combined, national_unemployment, national_data, pre_covid, covid_period)
    
    print(f"\n✓ All visualizations saved to: {OUTPUT_DIR}")
    
    # STEP 5: Policy Recommendations
    print_policy_recommendations()
    
    # Final Summary
    print_header("ANALYSIS COMPLETE")
    print(f"""
Summary of generated outputs:
  
Visualizations saved in '{OUTPUT_DIR}':
  1. 01_unemployment_trends.png - National unemployment trends over time
  2. 02_covid_impact.png - COVID-19 impact analysis
  3. 03_seasonal_patterns.png - Seasonal trends and patterns
  4. 04_regional_insights.png - Regional unemployment analysis
  5. 05_comprehensive_dashboard.png - Complete analysis dashboard

Next Steps:
  • Review visualizations for deeper insights
  • Share findings with policymakers
  • Implement recommended policy measures
  • Monitor unemployment rates regularly
  • Adjust policies based on economic conditions
""")


if __name__ == "__main__":
    main()
