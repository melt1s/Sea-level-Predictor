import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    sea_data = pd.read_csv('epa-sea-level.csv')
    df = pd.DataFrame (data = sea_data)
    dfA = df.drop(df[df.Year < 2000].index)
    dfB = dfA['Year']
    dfC = dfA['CSIRO Adjusted Sea Level']
    dfX = df['Year']
    dfY = df['CSIRO Adjusted Sea Level']
    years_extended = np.arange(1880, 2051, 1)
    second_extended = np.arange(2000, 2051, 1)
    # Create scatter plot
    plt.scatter(x=dfX, y=dfY)

    # Create first line of best fit
    res = linregress(x=dfX, y=dfY)
    plt.plot(years_extended, res.intercept + res.slope * years_extended, 'b')

    # Create second line of best fit
    res1 = linregress(x=dfB, y=dfC)
    plt.plot(second_extended, res1.intercept + res1.slope * second_extended, 'y')
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()