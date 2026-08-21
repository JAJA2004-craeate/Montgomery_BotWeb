import streamlit as st
import os
from google import genai

# Inicializácia klienta pomocou kľúča zo Secrets
client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

st.title("Edukácia: Montgomery T-tubus")
st.write("Dobrý deň. Som Váš digitálny asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu (MTT). Ako Vám dnes môžem pomôcť?")

query = st.text_input("Napíš svoju otázku...")

if query:
    with st.spinner("Pripravujem odpoveď..."):
        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"Si odborný asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu (MTT). Odpovedz na otázku: {query}"
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Nastala chyba: {e}")
