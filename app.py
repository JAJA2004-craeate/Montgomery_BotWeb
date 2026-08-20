import streamlit as st
import os
from openai import OpenAI

# Načítanie OpenAI kľúča zo Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Edukácia: Montgomery T-tubus")
st.write("Dobrý deň. Som Váš digitálny asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu(MTT). Som tu, aby som Vám pomohol s otázkami týkajúcimi sa základných informácií aj ošetrovateľských postupov na základe odborných študijných materiálov. Ako Vám dnes môžem pomôcť?")

# Pole na otázku
query = st.text_input("Napíš svoju otázku...")

if query:
    with st.spinner("Pripravujem odpoveď..."):
        try:
            # Priame volanie OpenAI modelu pre maximálnu spoľahlivosť bez chýb
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Si odborný asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu (MTT). Poskytuj presné, odborné a empatiou vedené odpovede na základe medicínskych štandardov."},
                    {"role": "user", "content": query}
                ]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Nastala chyba: {e}")
