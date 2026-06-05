import streamlit as st

st.set_page_config(layout="wide")

st.title("🧠 Bondscoach Esko's Advies")

st.success(
    "Persoonlijke WK 2026 Scorito-assistent"
)

st.header("🏆 Favorieten voor de wereldtitel")

favorieten = [
    "🇪🇸 Spanje",
    "🇫🇷 Frankrijk",
    "🇦🇷 Argentinië",
    "🇧🇷 Brazilië",
    "🏴 Engeland"
]

for land in favorieten:
    st.write(land)

st.header("🔥 Dark Horses")

dark_horses = [
    "🇺🇾 Uruguay",
    "🇯🇵 Japan",
    "🇲🇦 Marokko",
    "🇨🇴 Colombia"
]

for land in dark_horses:
    st.write(land)

st.header("⚠️ Risicovolle favorieten")

risico = [
    "🇧🇪 België",
    "🇵🇹 Portugal",
    "🇩🇪 Duitsland"
]

for land in risico:
    st.write(land)

st.header("🎯 Scorito Strategie")

st.markdown("""
### Veilig spelen
- Kies een topfavoriet als wereldkampioen.
- Vul logische groepswinnaars in.
- Vermijd te veel verrassingen.

### Gemiddeld risico
- Neem 1 of 2 verrassende groepswinnaars.
- Laat enkele favorieten eerder stranden.

### Hoog risico
- Kies een dark horse als finalist.
- Zet in op een verrassende topscorer.
- Kan veel punten opleveren als het goed valt.
""")

st.header("💡 Tip van Bondscoach Esko")

st.info(
    "Bij Scorito win je vaak niet door de finale goed te voorspellen, "
    "maar door veel groepswedstrijden en groepsstanden correct te hebben."
)