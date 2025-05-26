import streamlit as st
import time

st.title("Live Commentary Simulator")

# Sidebar control for delay
delay = st.sidebar.slider("Delay (sec)", 1, 10, 5)

# Placeholder for the commentary text
placeholder = st.empty()

# Load your comments
with open('commentary.txt', 'r', encoding='utf-8') as f:
    comments = [l.strip() for l in f if l.strip()]

if st.button("Start"):
    for c in comments:
        # Wrap in a styled <div> via HTML
        styled = f"""
          <div style="
            font-size: 24px;    /* adjust px size as you like */
            color: #0066CC;     /* any hex, name, or rgb() value */
            font-family: Arial, sans-serif;
            padding: 10px;
            background-color: #F0F8FF; /* optional highlight */
            border-radius: 8px;
          ">
            {c}
          </div>
        """
        # Render HTML with unsafe_allow_html=True
        placeholder.markdown(styled, unsafe_allow_html=True)
        time.sleep(delay)
    st.balloons()
