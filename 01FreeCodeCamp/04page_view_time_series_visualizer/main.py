import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Import data and set date as index
def import_data():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    return df

# Task 2: Clean the data
def clean_data(df):
    # Calculate the lower and upper thresholds
    lower_threshold = df['value'].quantile(0.025)
    upper_threshold = df['value'].quantile(0.975)
    
    # Filter out days outside the thresholds
    df_cleaned = df[(df['value'] >= lower_threshold) & (df['value'] <= upper_threshold)]
    
    return df_cleaned

# Task 3: Draw line plot
def draw_line_plot(df_cleaned):
    plt.figure(figsize=(12, 6))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.grid(True)
    
    # Save the plot
    plt.savefig('line_plot.png')
    return plt

# Task 4: Draw bar plot
def draw_bar_plot(df_cleaned):
    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.month_name()
    df_grouped = df_cleaned.groupby(['year', 'month'])['value'].mean().unstack()
    
    ax = df_grouped.plot(kind='bar', figsize=(12, 6))
    plt.title("Average Daily Page Views for Each Month Grouped by Year")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.grid(axis='y')
    
    # Save the plot
    plt.savefig('bar_plot.png')
    return plt

# Task 5: Draw box plots
def draw_box_plot(df_cleaned):
    df_cleaned['year'] = df_cleaned.index.year
    df_cleaned['month'] = df_cleaned.index.month_name()
    
    # Year-wise box plot
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_cleaned)
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    
    # Month-wise box plot
    plt.subplot(1, 2, 2)
    df_cleaned['month'] = pd.Categorical(df_cleaned['month'], categories=[
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
        'September', 'October', 'November', 'December'], ordered=True)
    sns.boxplot(x='month', y='value', data=df_cleaned, )
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('box_plot.png')
    return plt


