#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:25:57 2025

@author: fcvmathieu
"""

import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import urllib.parse


# GitHub repository where images are stored (raw URL format)
GITHUB_BASE_URL = "https://raw.githubusercontent.com/FC-Versailles/jordan/main/"

# Function to fetch images from GitHub
def load_image_from_github(filename):
    url = GITHUB_BASE_URL + filename
    response = requests.get(url)
    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"⚠️ Could not load image: {filename}")
        return None

image = load_image_from_github("pic.png")
if image:
    st.image(image, width=100)
# Title & Player Overview
st.title("Jordan Mendes - 21(FR)")
# Button linking to Transfermarkt profile
st.link_button("Transfermarkt Profile", "https://www.transfermarkt.fr/jordan-mendes-correia/profil/spieler/1138156")

st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.header("🔍 Key Insights")
st.markdown(
    """
    xxx
    """
)

# Define the WhatsApp number (include country code, no '+' sign)
whatsapp_number = "33771730001"  # Example: +33 for France

# Message to send
message = "Hello, I am interested in Jordan Mendes. Can we discuss further?"

# Encode message for URL
encoded_message = urllib.parse.quote(message)

# WhatsApp URL
whatsapp_url = f"https://api.whatsapp.com/send?phone={whatsapp_number}&text={encoded_message}"

# Button to open WhatsApp chat
if st.button("📲 Contact Sport Director"):
    st.markdown(f'<a href="{whatsapp_url}" target="_blank">Send a whatsapp</a>', unsafe_allow_html=True)


st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

# Vertical Display with Expanders
with st.expander("👤 Player Career | Need a next for his development"):
    image = load_image_from_github("fiche.png")
    if image:
        st.image(image, use_container_width=True)
    
    # Career Analysis
    st.write("""
    ### 🛤 **Career Path Analysis:**
    - **Youth Development:** Trained at **FC Versailles' academy**, progressing through U19 and B teams.
    - **First-Team Integration:** Promoted to **FC Versailles first team in 2023**, showing steady development.
    - **Playing Position:** **Defensive midfielder**, with secondary capabilities as a **central midfielder**.
    
    
    - **Future Progression:**
      - Needs to **increase first-team minutes** to gain experience at National level.
      - Could **attract Ligue 2 or high-tier National teams** if he improves his consistency and physical presence.
    
    ✅ **Jordan has made steady progress through the ranks at FC Versailles. His next step is proving himself as a regular starter in National before targeting a move to a higher league.**
    """)
with st.expander("📍 Position Played | Advanced N°10 or False 9"):
    image = load_image_from_github("position.png")
    if image:
        st.image(image, use_container_width=True)
    # Positional Analysis
    st.write("""
    ### **Jordan Mendes Correia | Deep-Lying Midfielder**
    
    #### **📊 Positioning & Role**
    - **Primary Position:** Right Defensive Midfielder (RDM) - **4.5 appearances**
    - **Secondary Roles:** Left Defensive Midfielder (LDM) & Central Midfielder (LCM/RCM)
    - **Tactical Role:** Positioned as a **holding midfielder**, supporting both the defensive line and midfield transitions.


    ✅ **Jordan is a structured, intelligent midfielder who thrives in defensive midfield roles. With better passing penetration and physical intensity, he can develop into a key No.6 at a higher level.**
    """)
with st.expander("⏳ Minutes played | Need to get consistency in minutes played"):
    image = load_image_from_github("minutes_played.png")
    if image:
        st.image(image, use_container_width=True)
    # Performance Analysis
    st.write("""
    ### **📊 Match Involvement:**
    - **Appearances:** Featured in multiple games but with limited full-match performances.
    - **Substitution Pattern:** Frequently started but was often subbed off before full-time.
    - **Late-Season Drop:** Minutes decreased significantly in early 2025, possibly due to squad rotation or fitness concerns.
    - **Unused or Did Not Play Matches:** A mix of being on the bench or left out of the squad entirely.


    ✅ **Jordan is gaining first-team experience but needs more consistency to cement his place as a key starter.**
    """)

with st.expander("🛡 Player Profile | Defensive Midfield Enforcer"):
    image = load_image_from_github("leaugue_Comparison.png")
    if image:
        st.image(image, use_container_width=True)
# Player profile analysis
    st.write("""
    ### **Jordan Mendes Correia | Defensive Midfield Enforcer**
    
    #### **🔍 Strengths:**
    - **Defensive Awareness:** Excellent in **tackles and interceptions**, outperforming the league average.
    - **1v1 Defensive Duels:** Strong ability to win **duels when dribbled past**, making him a reliable defensive presence.
    - **Pressing & Pressure Resistance:** Above average in **pressures and defensive actions OBV**, helping the team recover possession effectively.
    - **Physical & Aggressive Playstyle:** Frequently **wins fouls**, disrupting opposition play.

    #### **📉 Areas for Improvement:**
    - **Passing Impact:** Below league average in **progressive passing and OBV**, limiting his ability to break lines.
    - **Offensive Contributions:** Needs improvement in **open play xG assisted** and **dribble carry OBV** to support attacks more efficiently.
    - **Turnovers:** Slightly higher than the league average, indicating that he sometimes loses possession in key areas.

    #### **📊 Tactical Fit:**
    - Best suited as a **No.6 (defensive midfielder)** in a **pressing system** where his ball-winning skills can shine.
    - Could be utilized as a **box-to-box midfielder (No.8)** in a **double pivot**, provided he improves his passing range.
    - Ideal for a **counter-attacking setup**, where he disrupts opposition play and quickly transitions the ball forward.

    ### **🚀 Next Steps in Development:**
    - **Improve progressive passing & transitions** to become a more complete deep-lying playmaker.
    - **Reduce turnovers** by refining decision-making under pressure.
    - **Enhance ball-carrying ability** to be more involved in build-up play.

    ✅ **Jordan is a strong, defensively solid midfielder with great tackling and pressing ability. If he refines his passing and offensive impact, he could develop into a high-level midfield anchor.**
    """)


with st.expander("🏋️ Physical Performance | Global Athlete"):
    image = load_image_from_github("physique.png")
    if image:
        st.image(image, use_container_width=True)
    # Physical Profile Analysis
    st.write("""
    ### **Jordan Mendes Correia | Energetic & High-Work-Rate Midfielder**
    
    #### **📊 Key Physical Metrics:**
    - **Total Distance Covered:** Averages **12,449 meters per game**, showcasing his endurance.
    - **High-Speed Running (HSR 16-24 km/h):** **2,524 meters per game**, proving strong ability to maintain high-intensity efforts.
    - **Sprints (>24 km/h):** Covers **263 meters per game**, showing short-burst acceleration ability.
    - **Acceleration & Deceleration:**
      - **41 high-intensity accelerations (>4m/s²)** per game.
      - **27 decelerations per game**, showing good control in transitional play.
    - **Max Speed (VMAX):** Peaks at **29.7 km/h**, indicating solid pace for a midfielder.

    #### **🔍 Strengths:**
    - **High stamina & endurance**, allowing him to cover large distances effectively.
    - **Strong acceleration profile**, helping him press and recover quickly.
    - **Efficient in high-intensity runs**, useful for counter-pressing and tracking back defensively.
    - **Consistently involved in transitional phases**, making him a box-to-box style midfielder.

    #### **📉 Areas for Improvement:**
    - **Sprint explosiveness** can be improved to enhance quick transitions.
    - **Deceleration control** can be refined to maintain stability in defensive recoveries.
    - **Increase short-burst power** to improve pressing efficiency in tight areas.

    #### **📌 Tactical Fit:**
    - Suited for a **high-energy pressing team** where his work rate and stamina are key.
    - Can thrive in a **box-to-box (No.8) role** or as a **defensive midfielder (No.6)** in a high-intensity system.
    - Ideal for **transition-based teams**, where his physical ability can shine in counter-attacks and recoveries.

    ### **🚀 Next Steps in Development:**
    - **Improve top-speed sprinting** to add dynamism to his offensive runs.
    - **Enhance agility & quick turns** to optimize ball recoveries.
    - **Increase acceleration efficiency** to maximize pressing impact.

    ✅ **Jordan is a physically dominant midfielder with great endurance, pressing intensity, and work rate. If he enhances his explosiveness and decision-making under pressure, he could become an elite box-to-box midfielder.**
    """)

    
with st.expander("⚖️ Weight Evolution | Professional player"):
    image = load_image_from_github("poids.png")
    if image:
        st.image(image, use_container_width=True)
    st.write("Monitoring body composition is key to performance optimization.Jordan show a good body composition")

# with st.expander("🔥 Personnality & Motivation | Real passion for football & competitor"):
#     image = load_image_from_github("Happiness.png")
#     if image:
#         st.image(image, use_container_width=True)
#     st.write("Samy loves competition and fight for the win. He passionate about football and expect an interesting contract for his prime.")



st.markdown("<hr style='border:1px solid #ddd' />", unsafe_allow_html=True)

st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f8f9fa;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #333;
        }
    </style>
    <div class="footer">
        <p><strong>M.Feigean</strong> - Football Development</p>
    </div>
    """, unsafe_allow_html=True)

