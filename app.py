import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="WK 2026 Assistent Bondscoach Esko",
    layout="wide"
)

st.title("🏆 WK 2026 Assistent Bondscoach Esko")

teams = [
    "Nederland",
    "Argentinië",
    "Brazilië",
    "Frankrijk",
    "Engeland",
    "Spanje",
    "Duitsland",
    "Portugal",
    "België",
    "Japan",
    "Mexico",
    "Verenigde Staten"
]

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Land 1", teams)

with col2:
    team2 = st.selectbox("Land 2", teams, index=1)

st.divider()

col3, col4 = st.columns(2)

with col3:
    score1 = st.number_input(
        f"Doelpunten {team1}",
        min_value=0,
        max_value=15,
        value=1
    )

with col4:
    score2 = st.number_input(
        f"Doelpunten {team2}",
        min_value=0,
        max_value=15,
        value=0
    )

if st.button("Opslaan voorspelling"):

    nieuwe_voorspelling = pd.DataFrame([
        {
            "team1": team1,
            "score1": score1,
            "score2": score2,
            "team2": team2
        }
    ])

    bestand = "data/predictions.csv"

    bestaande_data = pd.read_csv(bestand)

    alle_data = pd.concat(
        [bestaande_data, nieuwe_voorspelling],
        ignore_index=True
    )

    alle_data.to_csv(
        bestand,
        index=False
    )

    st.success(
        f"Voorspelling opgeslagen: {team1} {score1}-{score2} {team2}"
    )

st.subheader("Opgeslagen voorspellingen")

voorspellingen = pd.read_csv(
    "data/predictions.csv"
)

st.dataframe(voorspellingen)