import streamlit as st
from google import genai

# Konfigurácia stránky
st.set_page_config(page_title="Montgomery Edubot", page_icon="🩺")

# CSS pre moderný dizajn
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #e3f2fd, #ffffff);
    }
    .main-title {
        color: #0d47a1;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .disclaimer {
        font-size: 0.9em;
        color: #555;
        text-align: center;
        margin-top: 30px;
        padding: 15px;
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 15px;
        border: 1px solid #bbdefb;
    }
    </style>
""", unsafe_allow_html=True)

# Obsah stránky
st.markdown("<h1 class='main-title'>🩺 Montgomery T-kanyla Asistent</h1>", unsafe_allow_html=True)

st.write("Dobrý deň. Som Váš digitálny asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu (MTT).")

# Disclaimer
st.markdown("<div class='disclaimer'>⚠️ <strong>UPOZORNENIE:</strong> Tento bot slúži výhradne na informačné účely. Nie je náhradou za odbornú lekársku konzultáciu, diagnostiku ani liečbu. V prípade zdravotných ťažkostí sa vždy poraďte s lekárom.</div>", unsafe_allow_html=True)

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
