import streamlit as st
import time

st.title("Live Commentary Simulator")

# Sidebar controls
delay = st.sidebar.slider("Delay (sec)", 1, 10, 5)
font_size = st.sidebar.slider("Font size (px)", 36, 96, 48)  # Increased range, default 48px
text_color = st.sidebar.color_picker("Text color", "#FFFFFF")        # Default white for visibility
bg_color = st.sidebar.color_picker("Background color", "#00008B")    # Default dark blue
text_opacity = st.sidebar.slider("Text opacity (%)", 50, 100, 100)


# Placeholder for the commentary text
placeholder = st.empty()

# Load your comments
with open('commentary.txt', 'r', encoding='utf-8') as f:
    comments = [l.strip() for l in f if l.strip()]

if st.button("Start"):
    for c in comments:
        styled = f"""
        <div style="
            font-size: {font_size}px;
            color: {text_color};
            opacity: {text_opacity/100};
            font-family: Arial, sans-serif;
            padding: 14px;
            background-color: {bg_color};
            border-radius: 8px;
            margin-bottom: 10px;
        ">
            {c}
        </div>
        """
        placeholder.markdown(styled, unsafe_allow_html=True)
        time.sleep(delay)
    st.balloons()
