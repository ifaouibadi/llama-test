import streamlit as st
from verse_bot import chat

text = st.text_area("enter some text")


if text:
    out = chat(
        text,
    )

    print("=======")
    print("out::", out)
    print("=======")

    st.json(out)
