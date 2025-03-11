import streamlit as st

st.title("🎈 My New App test")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("p2.py", title="Page 2", icon="❄️")
page_3 = st.Page("p3.py", title="Page 3", icon="🎉")

nav = st.navigation([main_page, page_2, page_3])

st.sidebar.write("This is a sidebar")

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

nav.run()

