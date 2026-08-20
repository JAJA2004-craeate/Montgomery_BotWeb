import streamlit as st

# Úvodná stránka
st.title("Edukácia: Montgomery T-tubus")
st.write("Dobrý deň. Som Váš digitálny asistent pre ošetrovateľskú starostlivosť o Montgomery T-kanylu(MTT). Som tu, aby som Vám pomohol s otázkami týkajúcimi sa základných informácií aj ošetrovateľských postupov na základe odborných študijných materiálov. Ako Vám dnes môžem pomôcť?")

# Pole na otázku
user_query = st.text_input("Napíš svoju otázku...")

if user_query:
    # Tu bude neskôr logika pre čítanie z PDF
    st.info(f"Pýtaš sa: '{user_query}'. Práve analyzujem odborné materiály...")
    
    # Dočasná odpoveď (kým nastavíme model)
    st.success("Odpoveď: Táto funkcia sa práve aktivuje. O chvíľu bude bot čerpať priamo z tvojich nahraných PDF súborov.")

# Poznámka: Aby bot fungoval s tvojimi PDF, 
# musíme ešte pridať knižnicu na čítanie PDF (PyPDF2) a OpenAI kľúč.
