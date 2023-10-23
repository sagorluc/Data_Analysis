import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Task 1: Import data
def import_data():
    df = pd.read_csv('epa-sea-level.csv')
    return df

# Task 2: Create a scatter plot
def create_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, color='blue')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    return plt

# Task 3: Calculate and plot line of best fit through 2050
def plot_line_of_best_fit(df, start_year, end_year):
    # Use linregress to get slope and intercept
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Generate x values from start_year to end_year
    x_values = list(range(start_year, end_year + 1))
    
    # Generate y values using the slope and intercept
    y_values = [(slope * x + intercept) for x in x_values]
    
    # Plot the line of best fit
    plt.plot(x_values, y_values, color='red', label='Line of Best Fit')
    plt.legend()
    return plt

# Task 4: Predict sea level rise in 2050
def predict_sea_level_rise(df, year):
    # Use linregress to get slope and intercept for data from 2000 to most recent year
    recent_data = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    
    # Predict sea level rise in 2050
    predicted_sea_level = slope * year + intercept
    return predicted_sea_level

# Task 5: Save and return the image
def save_and_return_image(plt):
    plt.savefig('sea_level_rise_prediction.png')
    return plt

# Main script to perform the tasks
if __name__ == '__main__':
    # Task 1
    df = import_data()

    # Task 2
    scatter_plot = create_scatter_plot(df.copy())

    # Task 3
    line_of_best_fit = plot_line_of_best_fit(df.copy(), 1880, 2050)

    # Task 4
    predicted_sea_level = predict_sea_level_rise(df.copy(), 2050)
    print(f'Predicted sea level rise in 2050: {predicted_sea_level:.2f} inches')

    # Task 5
    saved_plot = save_and_return_image(plt)

    # Show the plots
    plt.show()
