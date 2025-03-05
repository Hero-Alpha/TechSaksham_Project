import pandas as pd

FILE_PATH = "./data/athletes.csv"

def load_olympics_data(file_path):
    """Load the Olympics dataset from CSV."""
    return pd.read_csv(file_path)

def total_medals_by_country(df):
    """Returns the total medals won by each country."""
    return df[df['Medal'].notna()].groupby('Country')['Medal'].count().sort_values(ascending=False)

def top_athletes_by_medals(df, top_n=10):
    """Finds the top athletes with the most medals."""
    return df[df['Medal'].notna()].groupby('Name')['Medal'].count().sort_values(ascending=False).head(top_n)

def most_successful_countries(df, top_n=10):
    """Finds the most successful countries based on total medal count."""
    return df[df['Medal'].notna()].groupby('Country')['Medal'].count().sort_values(ascending=False).head(top_n)

def sport_trends_over_time(df):
    """Shows participation trends in different sports over the years."""
    return df.groupby(['Year', 'Sport']).size().unstack().fillna(0)

def gender_representation_over_time(df):
    """Compares male vs. female participation over the years."""
    return df.groupby(['Year', 'Gender']).size().unstack().fillna(0)

def average_age_medalists(df):
    """Finds the average age of medalists over time."""
    return df[df['Medal'].notna()].groupby('Year')['Age'].mean()

def height_weight_correlation(df):
    """Analyzes correlation between height, weight, and winning medals."""
    return df[df['Medal'].notna()][['Height (cm)', 'Weight (kg)']].corr()

def host_country_advantage(df, host_country):
    """Checks if the host country won more medals when hosting."""
    return df[(df['Country'] == host_country) & (df['Medal'].notna())].groupby('Year')['Medal'].count()

def summer_vs_winter_performance(df):
    """Compares trends in Summer vs. Winter Olympics."""
    return df[df['Medal'].notna()].groupby(['Year', 'Season'])['Medal'].count().unstack().fillna(0)

def dominant_athletes_in_sport(df, sport, top_n=5):
    """Finds the most dominant athletes in a given sport."""
    return df[(df['Sport'] == sport) & (df['Medal'].notna())].groupby('Name')['Medal'].count().sort_values(ascending=False).head(top_n)

df = load_olympics_data(FILE_PATH)