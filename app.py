import streamlit as st
from google import genai

# Konfigurácia stránky
st.set_page_config(page_title="Montgomery Edubot", page_icon="🧬", layout="centered")

# Moderný medicínsky dizajn (Mint / Teal téma)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%);
    }
    
    .main-box {
        background: #ffffff;
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 12px 30px rgba(13, 148, 136, 0.08);
        border: 1px solid rgba(13, 148, 136, 0.1);
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .app-title {
        color: #0f766e;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 2.2rem;
        margin-bottom: 5px;
    }

    .app-subtitle {
        color: #64748b;
        text-align: center;
        font-size: 1rem;
        margin-bottom: 30px;
        font-weight: 400;
    }

    .disclaimer-box {
        font-size: 0.85rem;
        color: #475569;
        text-align: center;
        margin-top: 35px;
        padding: 15px;
        background-color: #f8fafc;
        border-radius: 12px;
        border-left: 4px solid #0f766e;
    }
    </style>
""", unsafe_allow_html=True)

# Vizuálny obal
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

st.markdown("<h1 class='app-title'>🧬 Montgomery Edubot</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Interaktívny edukačný asistent pre ošetrovateľskú starostlivosť o MTT</p>", unsafe_allow_html=True)

st.write("Dobrý deň. Som tu na to, aby som Vám poskytol odborné informácie a odpovedal na Vaše otázky týkajúce sa starostlivosti o Montgomery T-kanylu.")

# Logika bota
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
query = st.text_input("Napíšte svoju otázku...")

if query:
    with st.spinner("Vyhľadávam odborné informácie..."):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=f"Si odborný asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu (MTT). Odpovedz na otázku: {query}. Dôležité: Na konci odpovede vždy zdôrazni, že nie si náhradou lekára a slúžiš len na informovanosť."
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Nastala chyba: {e}")

# Disclaimer
st.markdown("<div class='disclaimer-box'>⚠️ <strong>UPOZORNENIE:</strong> Tento nástroj slúži výhradne na informačné účely a podporu vzdelávania. Nenahrádza odbornú lekársku konzultáciu, diagnostiku ani liečbu.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
