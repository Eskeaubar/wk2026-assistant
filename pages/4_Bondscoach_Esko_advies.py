import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("🧠 Bondscoach Esko's Advies")

st.success(
    "Persoonlijke WK 2026 Assistent Esko"
)

# -----------------------------
# Groepsstanden laden
# -----------------------------

try:

    standen = pd.read_csv(
        "data/groepsstanden.csv"
    )

    groepswinnaars = standen[
        standen["Pos"] == 1
    ]

    nummers2 = standen[
        standen["Pos"] == 2
    ]

except:

    standen = pd.DataFrame()
    groepswinnaars = pd.DataFrame()
    nummers2 = pd.DataFrame()

# -----------------------------
# Huidige groepswinnaars
# -----------------------------

st.header("🥇 Huidige Groepswinnaars")

if not groepswinnaars.empty:

    st.dataframe(
        groepswinnaars[
            ["Groep", "Land", "Punten"]
        ],
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning(
        "Nog geen groepsstanden beschikbaar."
    )

# -----------------------------
# Nummers 2
# -----------------------------

st.header("🥈 Huidige Nummers 2")

if not nummers2.empty:

    st.dataframe(
        nummers2[
            ["Groep", "Land", "Punten"]
        ],
        use_container_width=True,
        hide_index=True
    )

# -----------------------------
# Wereldkampioen advies
# -----------------------------

st.header("🏆 Kanshebbers Wereldtitel")

favorieten = [
    "🇪🇸 Spanje",
    "🇫🇷 Frankrijk",
    "🇦🇷 Argentinië",
    "🇧🇷 Brazilië",
    "🏴 Engeland"
]

for land in favorieten:
    st.write(f"• {land}")

# -----------------------------
# Dark Horses
# -----------------------------

st.header("🔥 Dark Horses")

dark_horses = [
    "🇺🇾 Uruguay",
    "🇯🇵 Japan",
    "🇨🇴 Colombia",
    "🇲🇦 Marokko"
]

for land in dark_horses:
    st.write(f"• {land}")

# -----------------------------
# Risicovolle favorieten
# -----------------------------

st.header("⚠️ Risicovolle Favorieten")

risico = [
    "🇧🇪 België",
    "🇵🇹 Portugal",
    "🇩🇪 Duitsland"
]

for land in risico:
    st.write(f"• {land}")

# -----------------------------
# Esko's Strategie
# -----------------------------

st.header("🎯 Esko's Strategie")

st.markdown("""
### Veilige strategie
- Kies een topfavoriet als wereldkampioen
- Laat favorieten de groepsfase overleven
- Voorkom te veel verrassingen

### Gemiddeld risico
- Kies 1 verrassende groepswinnaar
- Laat 1 favoriet vroeg stranden
- Neem een onverwachte halve finalist

### Hoog risico
- Kies een dark horse voor de finale
- Verrassende topscorer
- Grote kans op veel bonuspunten
""")

# -----------------------------
# Persoonlijk advies
# -----------------------------

st.header("💡 Tip van Bondscoach Esko")

st.info(
    "Bij Scorito worden de meeste punten verdiend in de groepsfase. "
    "Richt je niet alleen op de finale, maar vooral op correcte groepsstanden "
    "en veel juiste toto's tijdens de eerste speelrondes."
)

# -----------------------------
# Top 5 advies
# -----------------------------

st.header("🚀 Hoe eindig je in de Top 5?")

st.markdown("""
1. Kies niet exact dezelfde favorieten als iedereen.
2. Gebruik 1 of 2 verrassende halvefinalisten.
3. Vermijd teveel stuntuitslagen in de groepsfase.
4. Focus op juiste groepsstanden.
5. Kies topscorers uit landen die minimaal de kwartfinale halen.
""")

st.success(
    "Bondscoach Esko analyse gereed."
)