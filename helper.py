import numpy as np
def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    Country = df['Country'].unique().tolist()
    Country.sort()
    Country.insert(0, 'Overall')

    return years,Country
