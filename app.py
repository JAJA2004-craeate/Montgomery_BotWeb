import streamlit as st
from google import genai

# Konfigurácia stránky
st.set_page_config(page_title="Montgomery Edubot", page_icon="🩺", layout="centered")

# Pokročilejší CSS dizajn
st.markdown("""
    <style>
    /* Pozadie celej stránky s jemným moderným prechodom */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Hlavný kontajner / karta pre obsah */
    .main-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
    }

    /* Hlavný nadpis */
    .main-title {
        color: #1e3c72;
        text-align: center;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Podnadpis / úvodný text */
    .subtitle {
        color: #4a5568;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }

    /* Disclaimer box */
    .disclaimer {
        font-size: 0.85rem;
        color: #718096;
        text-align: center;
        margin-top: 30px;
        padding: 15px;
        background-color: #fffaf0;
        border-radius: 12px;
        border: 1px solid #feebc8;
    }
    </style>
""", unsafe_allow_html=True)

# Vizuálny obal (karta)
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🩺 Montgomery Edubot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Váš digitálny sprievodca ošetrovateľskou starostlivosťou</p>", unsafe_allow_html=True)

st.write("Dobrý deň. Som tu, aby som Vám pomohol s odbornými informáciami týkajúcimi sa starostlivosti o MTT.")

# Logika bota
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
query = st.text_input("Napíš svoju otázku...")

if query:
    with st.spinner("Pripravujem odbornú odpoveď..."):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=f"Si odborný asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu (MTT). Odpovedz na otázku: {query}. Dôležité: Na konci odpovede vždy zdôrazni, že nie si náhradou lekára a slúžiš len na informovanosť."
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Nastala chyba: {e}")

# Disclaimer v spodnej časti karty
st.markdown("<div class='disclaimer'>⚠️ <strong>UPOZORNENIE:</strong> Tento bot slúži výhradne na informačné účely. Nie je náhradou za odbornú lekársku konzultáciu, diagnostiku ani liečbu. V prípade zdravotných ťažkostí sa vždy poraďte s lekárom.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
