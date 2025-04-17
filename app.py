import streamlit as st
from utils import get_tags

st.set_page_config(page_title="Sanskrit POS Tagger", layout="centered")

st.title("🕉️ Sanskrit Verb POS Tagger (Rule-Based)")
st.write("Enter any **conjugated Sanskrit verb form**, and we'll try to infer its grammatical tags.")

verb_input = st.text_input("🔍 Enter Sanskrit Verb", "")

if verb_input:
    results = get_tags(verb_input.strip())

    if results:
        st.success("✅ Match found!")
        for res in results:
            st.write(f"""
            - **Lakāra (Tense/Mood)**: {res["Lakāra (Tense/Mood)"]}
            - **Voice (Pāda)**: {res["Voice (Pāda)"]}
            - **Purusha (Person)**: {res["Purusha (Person)"]}
            - **Vachana (Number)**: {res['Vachana (Number)']}
            - **Matched Suffix**: `{res['Matched Suffix']}`
            """)
    else:
        st.error("❌ No match found. This verb form may be irregular or not covered in rules yet.")