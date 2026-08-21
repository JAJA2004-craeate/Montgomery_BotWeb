import streamlit as st
from google import genai
from google.genai import types

# Konfigurácia stránky
st.set_page_config(page_title="Montgomery Edubot", page_icon="🩺", layout="centered")

# CSS pre zdravotnícky štýl
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f9fa;
        background-image: radial-gradient(#d1e7e7 1px, transparent 1px);
        background-size: 30px 30px;
    }
    .content-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #0891b2;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .title {
        color: #0891b2;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Hlavný box s úvodom
st.markdown("""
    <div class="content-box">
        <h1 class="title">🩺 Montgomery Edubot</h1>
        <p>Váš rýchly digitálny asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu.</p>
    </div>
""", unsafe_allow_html=True)

# Logika bota
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

query = st.text_input("🔍 Napíšte svoju otázku o MTT...")

if query:
    with st.spinner("Hľadám odpoveď..."):
        try:
            # Systémová inštrukcia už neobsahuje opakovanie upozornenia
            config = types.GenerateContentConfig(
                temperature=0.0,
                system_instruction="Si stručný a odborný asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu. Odpovedz vecne a odborne na otázku používateľa."
            )
            
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=query,
                config=config
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Nastala chyba: {e}")

# Disclaimer v samostatnom boxíku
st.markdown("""
    <div style="background-color: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #cbd5e1; font-size: 0.8em; color: #64748b; margin-top: 30px;">
        ⚠️ <strong>Upozornenie:</strong> Tento nástroj slúži výhradne na informačné účely. Nenahrádza odbornú lekársku konzultáciu.
    </div>
""", unsafe_allow_html=True)
