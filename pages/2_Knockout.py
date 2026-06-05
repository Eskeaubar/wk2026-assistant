import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🏆 WK 2026 Knock-outfase")

# =====================================================
# GROEPSSTANDEN INLEZEN
# =====================================================

try:
    standen = pd.read_csv("data/groepsstanden.csv")
except:
    st.error("groepsstanden.csv niet gevonden.")
    st.stop()

# =====================================================
# KWALIFICATIE
# =====================================================

groepswinnaars = standen[standen["Pos"] == 1]
nummers2 = standen[standen["Pos"] == 2]

beste3 = (
    standen[standen["Pos"] == 3]
    .sort_values(
        by=["Punten", "Doelsaldo", "Voor"],
        ascending=False
    )
    .head(8)
)

st.info(
    "Overzicht van de gekwalificeerde landen op basis van de groepsfase."
)

st.subheader("🥇 Groepswinnaars")
st.dataframe(groepswinnaars, use_container_width=True, hide_index=True)

st.subheader("🥈 Nummers 2")
st.dataframe(nummers2, use_container_width=True, hide_index=True)

st.subheader("🥉 Beste nummers 3")
st.dataframe(beste3, use_container_width=True, hide_index=True)

# =====================================================
# ACHTSTE FINALES
# =====================================================

st.divider()
st.header("⚔️ Achtste Finales")

winnaars_achtste = []

landen_1 = groepswinnaars["Land"].tolist()
landen_2 = nummers2["Land"].tolist()

aantal = min(len(landen_1), len(landen_2))

for i in range(aantal):

    team1 = landen_1[i]
    team2 = landen_2[-(i + 1)]

    st.subheader(f"{team1} - {team2}")

    col1, col2 = st.columns(2)

    with col1:
        score1 = st.number_input(
            team1,
            min_value=0,
            key=f"a1_{i}"
        )

    with col2:
        score2 = st.number_input(
            team2,
            min_value=0,
            key=f"a2_{i}"
        )

    winnaar = None

    if score1 > score2:
        winnaar = team1

    elif score2 > score1:
        winnaar = team2

    else:

        st.warning("Gelijkspel. Strafschoppen invullen.")

        col3, col4 = st.columns(2)

        with col3:
            pens1 = st.number_input(
                f"Strafschoppen {team1}",
                min_value=0,
                key=f"ap1_{i}"
            )

        with col4:
            pens2 = st.number_input(
                f"Strafschoppen {team2}",
                min_value=0,
                key=f"ap2_{i}"
            )

        if pens1 > pens2:
            winnaar = team1

        elif pens2 > pens1:
            winnaar = team2

    if winnaar:
        st.success(f"Winnaar: {winnaar}")
        winnaars_achtste.append(winnaar)

# =====================================================
# KWARTFINALES
# =====================================================

st.divider()
st.header("⚔️ Kwartfinales")

winnaars_kwart = []

for i in range(0, len(winnaars_achtste), 2):

    if i + 1 >= len(winnaars_achtste):
        break

    team1 = winnaars_achtste[i]
    team2 = winnaars_achtste[i + 1]

    st.subheader(f"{team1} - {team2}")

    col1, col2 = st.columns(2)

    with col1:
        score1 = st.number_input(
            team1,
            min_value=0,
            key=f"k1_{i}"
        )

    with col2:
        score2 = st.number_input(
            team2,
            min_value=0,
            key=f"k2_{i}"
        )

    winnaar = None

    if score1 > score2:
        winnaar = team1

    elif score2 > score1:
        winnaar = team2

    else:

        col3, col4 = st.columns(2)

        with col3:
            pens1 = st.number_input(
                f"Strafschoppen {team1}",
                min_value=0,
                key=f"kp1_{i}"
            )

        with col4:
            pens2 = st.number_input(
                f"Strafschoppen {team2}",
                min_value=0,
                key=f"kp2_{i}"
            )

        if pens1 > pens2:
            winnaar = team1

        elif pens2 > pens1:
            winnaar = team2

    if winnaar:
        st.success(f"Winnaar: {winnaar}")
        winnaars_kwart.append(winnaar)

# =====================================================
# HALVE FINALES
# =====================================================

st.divider()
st.header("🥈 Halve Finales")

finalisten = []
troostfinalisten = []

for i in range(0, len(winnaars_kwart), 2):

    if i + 1 >= len(winnaars_kwart):
        break

    team1 = winnaars_kwart[i]
    team2 = winnaars_kwart[i + 1]

    st.subheader(f"{team1} - {team2}")

    col1, col2 = st.columns(2)

    with col1:
        score1 = st.number_input(
            team1,
            min_value=0,
            key=f"h1_{i}"
        )

    with col2:
        score2 = st.number_input(
            team2,
            min_value=0,
            key=f"h2_{i}"
        )

    winnaar = None
    verliezer = None

    if score1 > score2:
        winnaar = team1
        verliezer = team2

    elif score2 > score1:
        winnaar = team2
        verliezer = team1

    else:

        col3, col4 = st.columns(2)

        with col3:
            pens1 = st.number_input(
                f"Strafschoppen {team1}",
                min_value=0,
                key=f"hp1_{i}"
            )

        with col4:
            pens2 = st.number_input(
                f"Strafschoppen {team2}",
                min_value=0,
                key=f"hp2_{i}"
            )

        if pens1 > pens2:
            winnaar = team1
            verliezer = team2

        elif pens2 > pens1:
            winnaar = team2
            verliezer = team1

    if winnaar:
        st.success(f"Finalist: {winnaar}")
        finalisten.append(winnaar)

    if verliezer:
        troostfinalisten.append(verliezer)

# =====================================================
# TROOSTFINALE
# =====================================================

st.divider()
st.header("🥉 Troostfinale")

if len(troostfinalisten) == 2:

    team1 = troostfinalisten[0]
    team2 = troostfinalisten[1]

    st.subheader(f"{team1} - {team2}")

    col1, col2 = st.columns(2)

    with col1:
        score1 = st.number_input(
            team1,
            min_value=0,
            key="t1"
        )

    with col2:
        score2 = st.number_input(
            team2,
            min_value=0,
            key="t2"
        )

    derde = None

    if score1 > score2:
        derde = team1

    elif score2 > score1:
        derde = team2

    if derde:
        st.success(f"🥉 Derde plaats: {derde}")

# =====================================================
# FINALE
# =====================================================

st.divider()
st.header("🥇 Finale")

if len(finalisten) == 2:

    team1 = finalisten[0]
    team2 = finalisten[1]

    st.subheader(f"{team1} - {team2}")

    col1, col2 = st.columns(2)

    with col1:
        score1 = st.number_input(
            team1,
            min_value=0,
            key="f1"
        )

    with col2:
        score2 = st.number_input(
            team2,
            min_value=0,
            key="f2"
        )

    kampioen = None

    if score1 > score2:
        kampioen = team1

    elif score2 > score1:
        kampioen = team2

    else:

        col3, col4 = st.columns(2)

        with col3:
            pens1 = st.number_input(
                f"Strafschoppen {team1}",
                min_value=0,
                key="fp1"
            )

        with col4:
            pens2 = st.number_input(
                f"Strafschoppen {team2}",
                min_value=0,
                key="fp2"
            )

        if pens1 > pens2:
            kampioen = team1

        elif pens2 > pens1:
            kampioen = team2

    if kampioen:
        st.success(
            f"👑 Wereldkampioen WK 2026: {kampioen}"
        )