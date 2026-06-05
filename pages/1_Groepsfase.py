import streamlit as st
import pandas as pd
from itertools import combinations

st.set_page_config(layout="wide")

st.title("🏆 WK 2026 Groepsfase")

st.info(
    "WK 2026: De nummers 1 en 2 van iedere groep gaan door. "
    "Daarnaast plaatsen ook de 8 beste nummers 3 zich voor de knock-outfase."
)

# --------------------------------
# Groepen laden
# --------------------------------

groepen_df = pd.read_csv("data/groepen.csv")

groepen = {}

for _, row in groepen_df.iterrows():

    groep = str(row["groep"]).strip()
    team = str(row["team"]).strip()

    if groep not in groepen:
        groepen[groep] = []

    groepen[groep].append(team)

# --------------------------------
# Alle standen verzamelen
# --------------------------------

alle_standen = []

# --------------------------------
# Groepen verwerken
# --------------------------------

for groep_naam in sorted(groepen.keys()):

    teams = groepen[groep_naam]

    st.header(f"Groep {groep_naam}")

    wedstrijden = list(combinations(teams, 2))

    resultaten = []

    # --------------------------------
    # Wedstrijden invoeren
    # --------------------------------

    for team1, team2 in wedstrijden:

        col1, col2, col3 = st.columns([4, 1, 1])

        with col1:
            st.write(f"**{team1} - {team2}**")

        with col2:

            score1 = st.number_input(
                label=team1,
                min_value=0,
                max_value=20,
                value=0,
                key=f"{groep_naam}_{team1}_{team2}_1"
            )

        with col3:

            score2 = st.number_input(
                label=team2,
                min_value=0,
                max_value=20,
                value=0,
                key=f"{groep_naam}_{team1}_{team2}_2"
            )

        resultaten.append([
            team1,
            score1,
            score2,
            team2
        ])

    # --------------------------------
    # Wedstrijd DataFrame
    # --------------------------------

    df = pd.DataFrame(
        resultaten,
        columns=[
            "Team1",
            "Score1",
            "Score2",
            "Team2"
        ]
    )

    # --------------------------------
    # Stand berekenen
    # --------------------------------

    stand = {}

    for team in teams:

        stand[team] = {
            "Punten": 0,
            "Voor": 0,
            "Tegen": 0
        }

    for _, row in df.iterrows():

        team1 = row["Team1"]
        team2 = row["Team2"]

        score1 = int(row["Score1"])
        score2 = int(row["Score2"])

        stand[team1]["Voor"] += score1
        stand[team1]["Tegen"] += score2

        stand[team2]["Voor"] += score2
        stand[team2]["Tegen"] += score1

        if score1 > score2:

            stand[team1]["Punten"] += 3

        elif score2 > score1:

            stand[team2]["Punten"] += 3

        else:

            stand[team1]["Punten"] += 1
            stand[team2]["Punten"] += 1

    # --------------------------------
    # Stand DataFrame
    # --------------------------------

    stand_df = pd.DataFrame(stand).T

    stand_df["Doelsaldo"] = (
        stand_df["Voor"] - stand_df["Tegen"]
    )

    stand_df = stand_df.sort_values(
        by=["Punten", "Doelsaldo", "Voor"],
        ascending=False
    )

    stand_df = stand_df.reset_index()

    stand_df.columns = [
        "Land",
        "Punten",
        "Voor",
        "Tegen",
        "Doelsaldo"
    ]

    stand_df.insert(
        0,
        "Pos",
        range(1, len(stand_df) + 1)
    )

    # --------------------------------
    # Opslaan voor knockoutfase
    # --------------------------------

    for _, row in stand_df.iterrows():

        alle_standen.append({
            "Groep": groep_naam,
            "Pos": row["Pos"],
            "Land": row["Land"],
            "Punten": row["Punten"],
            "Voor": row["Voor"],
            "Tegen": row["Tegen"],
            "Doelsaldo": row["Doelsaldo"]
        })

    # --------------------------------
    # Tonen
    # --------------------------------

    col_links, col_rechts = st.columns([2, 1])

    with col_links:

        st.subheader("Wedstrijden")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    with col_rechts:

        st.subheader("Stand")

        st.dataframe(
            stand_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

# --------------------------------
# Alle standen opslaan
# --------------------------------

standen_df = pd.DataFrame(alle_standen)

standen_df.to_csv(
    "data/groepsstanden.csv",
    index=False
)