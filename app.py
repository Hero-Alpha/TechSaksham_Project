import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

from queries import df
from visualize import *


# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["🏠 Home", "📊 Data Overview", "📈 Medal Analysis", "🔍 Athlete Insights"],
        # icons=["house", "table", "bar-chart", "person"],
        menu_icon="menu-button-wide",
        default_index=0,
    )

if selected == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>🏅 Olympic Data Analysis Dashboard</h1>", unsafe_allow_html=True)
    
    # Centered Images
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.image("https://drop.ndtv.com/albums/NEWS/Tokyo_Olympics__637639596689933819/637639596716903215.jpeg", use_container_width=True)
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/512px-Olympic_rings_without_rims.svg.png", use_container_width=True)
    with col3:
        st.image("https://img.olympics.com/images/image/private/t_s_16_9_g_auto/t_s_w960/f_auto/primary/q9ioivewyykjss2cugqq", use_container_width=True)

    st.markdown("""
    **Welcome to the Olympic Athlete Data Explorer!**  
    This interactive dashboard lets you analyze Olympic data from **1986 to 2025**, including medal trends, athlete stats, and country rankings.  
    """)
    
    st.subheader("✨ Features Available:")
    st.markdown("""
    - **📊 Data Overview** → Filter by year, sport, country, and explore trends.
    - **🏅 Medal Analysis** → See which countries and athletes dominated.
    - **📈 Performance Trends** → Analyze age distribution, gender representation, and more.
    - **🔍 Find Your Favorite Athlete** → Search for athletes and their Olympic journey.
    """)
    
    st.write("👈 **Use the sidebar to navigate between different sections.**")

elif selected == "📊 Data Overview":
    st.title("📋 Data Review")
    st.write("Explore raw data, filter by country or sport, and view statistical summaries.")

    st.markdown("### 📌 Available Actions:")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 Sport Trends Over Time"):
            plot_sport_trends(df)

        if st.button("📊 Compare Summer vs Winter Olympics"):
            plot_summer_vs_winter(df)

    with col2:
        if st.button("👩‍🎓 Gender Representation Over Time"):
            plot_gender_representation(df)

        if st.button("📏 Show Height vs Weight Correlation of Medalists"):
            plot_height_weight_correlation(df)
    with col3:
        if st.button("📈 Show Average Age of Medalists Over Time"):
            plot_average_age_medalists(df)
        
    
elif selected == "📈 Medal Analysis":
    st.header("🏅 Medal Analysis 🏅")
    st.write("Analyze Olympic medal trends across countries and host nation advantages.")

    st.markdown("### 📌 Available Actions:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌍 Total Medals by Country"):
            plot_medals_by_country(df)

        if st.button("🏆 Most Successful Countries"):
            plot_successful_countries(df)

    with col2:
        host_country = st.text_input("🏠 Enter Host Country Name")
        if st.button("🏅 Show Host Country Medal Performance") and host_country:
            plot_host_country_advantage(df, host_country)

        
        
elif selected == "🔍 Athlete Insights":
    st.title("🔍 Athlete Insights")
    
    athlete_images = [
    "https://media.newyorker.com/photos/5909794e1c7a8e33fb38fd5e/master/pass/Thomas-MichaelPhelps.jpg",  # Michael Phelps
    "https://media.gq-magazine.co.uk/photos/5fcf80e6f264d85bcbdfc09b/16:9/w_2560%2Cc_limit/GettyImages-1282551982.jpg",  # Usain Bolt
    "https://media-cldnry.s-nbcnews.com/image/upload/rockcms/2024-07/240730-Paris-olympics-simone-biles-gold-medal-ac-726p-b09dd7.jpg",  # Simone Biles
    "https://media.newyorker.com/photos/66a28a0bedabe6f6c17d6823/master/pass/Thomas-SportingScene-KatieLedecky.jpg",  # Katie Ledecky
    "https://ca-times.brightspotcdn.com/dims4/default/f27c17a/2147483647/strip/true/crop/1728x1152+160+0/resize/2000x1333!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F43%2F98%2Fd1cf186ffdf2fe215346bba89750%2Fla-1467409250-snap-photo"  # Serena Williams
    ]

    scrollable_code = f"""
    <style>
    /* Full-Width Scrollable Section */
    .scroll-container {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100vw;
        position: relative;
        margin: auto;
        overflow: hidden;
    }}

    /* Wrapper for Scrollable Cards */
    .scroll-wrapper {{
        display: flex;
        overflow-x: auto;
        width: 80vw;
        scroll-behavior: smooth;
        white-space: nowrap;
        justify-content: flex-start;
        scrollbar-width: none;
        padding: 10px;
        scroll-snap-type: x mandatory;
    }}

    .scroll-wrapper::-webkit-scrollbar {{
        display: none;
    }}

    /* Individual Scroll Cards */
    .scroll-item {{
        flex: 0 0 80vw;
        height: 70vh;
        margin: 0 5px;
        background: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        font-weight: bold;
        border-radius: 15px;
        scroll-snap-align: center;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }}

    /* Images Inside Scroll Items */
    .scroll-item img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}

    /* Left & Right Scroll Buttons */
    .scroll-button {{
        background: rgba(0, 0, 0, 0.7);
        color: white;
        border: none;
        padding: 15px 20px;
        font-size: 24px;
        cursor: pointer;
        border-radius: 50%;
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        z-index: 10;
    }}

    .scroll-left {{ left: 2%; }}
    .scroll-right {{ right: 2%; }}

    .scroll-button:hover {{
        background: rgba(0, 0, 0, 0.9);
    }}
    </style>

    <!-- Scrollable Section -->
    <div class="scroll-container">
        <button class="scroll-button scroll-left" onclick="document.getElementById('scroll-wrapper').scrollBy({{left: -window.innerWidth * 0.8, behavior: 'smooth'}})">
            ⬅️
        </button>
        <div class="scroll-wrapper" id="scroll-wrapper">
            <div class="scroll-item"><img src="{athlete_images[0]}" alt="Athlete 1"/></div>
            <div class="scroll-item"><img src="{athlete_images[1]}" alt="Athlete 2"/></div>
            <div class="scroll-item"><img src="{athlete_images[2]}" alt="Athlete 3"/></div>
            <div class="scroll-item"><img src="{athlete_images[3]}" alt="Athlete 4"/></div>
            <div class="scroll-item"><img src="{athlete_images[4]}" alt="Athlete 5"/></div>
        </div>
        <button class="scroll-button scroll-right" onclick="document.getElementById('scroll-wrapper').scrollBy({{left: window.innerWidth * 0.8, behavior: 'smooth'}})">
            ➡️
        </button>
    </div>
    """

    st.components.v1.html(scrollable_code, height=600)
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🏆 Show Top 10 Athletes by Medals"):
            plot_top_athletes(df)

    with col2:
        sport = st.text_input("🏅 Enter Sport Name")
        if st.button("🥇 Show Dominant Athletes in Sport") and sport:
            plot_dominant_athletes(df, sport)
