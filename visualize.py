import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from queries import *

def plot_medals_by_country(df):
    medal_counts = total_medals_by_country(df).head(10)  # Top 10
    fig, ax = plt.subplots(figsize=(10, 5))
    medal_counts.plot(kind='bar', color='gold', ax=ax)
    ax.set_title("Top 10 Countries by Total Medals")
    ax.set_xlabel("Country")
    ax.set_ylabel("Medal Count")
    ax.set_xticklabels(medal_counts.index, rotation=45)
    st.pyplot(fig)

def plot_top_athletes(df):
    top_athletes = top_athletes_by_medals(df, top_n=10)
    fig, ax = plt.subplots(figsize=(10, 5))
    top_athletes.plot(kind='barh', color='blue', ax=ax)
    ax.set_title("Top 10 Athletes by Medals Won")
    ax.set_xlabel("Medals Won")
    ax.set_ylabel("Athlete")
    st.pyplot(fig)

def plot_successful_countries(df):
    countries = most_successful_countries(df, top_n=10)
    fig, ax = plt.subplots(figsize=(10, 5))
    countries.plot(kind='bar', color='green', ax=ax)
    ax.set_title("Top 10 Most Successful Countries")
    ax.set_xlabel("Country")
    ax.set_ylabel("Total Medals")
    ax.set_xticklabels(countries.index, rotation=45)
    st.pyplot(fig)

def plot_sport_trends(df):
    sport_trends = sport_trends_over_time(df)
    fig, ax = plt.subplots(figsize=(10, 6))
    sport_trends.plot(ax=ax, linewidth=2)
    ax.set_title("Participation Trends in Different Sports Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Athletes")
    ax.legend(title="Sports", bbox_to_anchor=(1, 1), loc="upper left")
    st.pyplot(fig)

def plot_gender_representation(df):
    gender_data = gender_representation_over_time(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    gender_data.plot(ax=ax, marker='o')
    ax.set_title("Male vs Female Participation Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Athletes")
    ax.legend(["Male", "Female"])
    st.pyplot(fig)

def plot_average_age_medalists(df):
    age_trend = average_age_medalists(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    age_trend.plot(ax=ax, marker='s', color='purple')
    ax.set_title("Average Age of Medalists Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Age")
    st.pyplot(fig)

def plot_height_weight_correlation(df):
    correlation = height_weight_correlation(df)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title("Correlation Between Height & Weight of Medalists")
    st.pyplot(fig)

def plot_host_country_advantage(df, host_country):
    host_performance = host_country_advantage(df, host_country)
    fig, ax = plt.subplots(figsize=(10, 5))
    host_performance.plot(kind='bar', color='red', ax=ax)
    ax.set_title(f"Medal Performance of {host_country} When Hosting")
    ax.set_xlabel("Year")
    ax.set_ylabel("Medals Won")
    ax.set_xticklabels(host_performance.index, rotation=45)
    st.pyplot(fig)

def plot_summer_vs_winter(df):
    season_data = summer_vs_winter_performance(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    season_data.plot(ax=ax, marker='o')
    ax.set_title("Medals Won in Summer vs Winter Olympics")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total Medals")
    ax.legend(["Summer", "Winter"])
    st.pyplot(fig)

def plot_dominant_athletes(df, sport):
    top_athletes = dominant_athletes_in_sport(df, sport)
    st.write(top_athletes)  # Display as text in Streamlit
