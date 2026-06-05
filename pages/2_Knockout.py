import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🏆 WK 2026 Knock-outfase")

st.info(
    "Overzicht van de gekwalificeerde landen op basis van de groepsfase."
)

# ---------------------------
# Standen laden
# ---------------------------

standen = pd.read_csv(
    "data/groepsstanden.csv"
)

# ---------------------------
# Groepswinnaars
# ---------------------------

groepswinnaars = standen[
    standen["Pos"] == 1
]

# ---------------------------
# Nummers 2
# ---------------------------

nummers2 = standen[
    standen["Pos"] == 2
]

# ---------------------------
# Nummers 3
# ---------------------------

nummers3 = standen[
    standen["Pos"] == 3
]

# Sorteer beste nummers 3

nummers3 = nummers3.sort_values(
    by=["Punten", "Doelsaldo", "Voor"],
    ascending=False
)

beste8 = nummers3.head(8)

# ---------------------------
# Tonen
# ---------------------------

st.header("🥇 Groepswinnaars")

st.dataframe(
    groepswinnaars,
    use_container_width=True,
    hide_index=True
)

st.header("🥈 Nummers 2")

st.dataframe(
    nummers2,
    use_container_width=True,
    hide_index=True
)

st.header("🥉 Beste nummers 3")

st.dataframe(
    beste8,
    use_container_width=True,
    hide_index=True
)

# ---------------------------
# Geplaatste landen
# ---------------------------

geplaatst = pd.concat(
    [
        groepswinnaars,
        nummers2,
        beste8
    ]
)

st.header("🌍 Laatste 32")

st.dataframe(
    geplaatst[
        [
            "Groep",
            "Land",
            "Pos"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

st.success(
    f"{len(geplaatst)} landen geplaatst voor de knock-outfase"
)