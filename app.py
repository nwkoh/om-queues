import time
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import sim

title = "Fun with Queues"

# footer text
footer_txt = '<div style="text-align: center"> &copy Koh Niak Wu, Ph.D.</div>'

st.set_page_config(
    page_title = "Operations Management",
    page_icon = '✅',
    layout = 'wide'
)


st.sidebar.title("About")
st.sidebar.subheader("Dr Koh Niak Wu's attempt to spice up his Operations Management classes")

st.sidebar.subheader("Enquiries: nwkoh@smu.edu.sg")


# dashboard title
st.title(title)

# u = p/am

a = st.slider('What is the average inter-arrival time, a (mins)?', 1, 50, 25)
p = st.slider('What is the average processing time, p (mins)?', 1, 50, 25)
m = st.slider('How many servers (m) are there?', 1, 5, 2)

u = p/(a*m)
st.markdown(f"#### Average utilisation, u = {round(u, 3) * 100}%")

if u > 1:
    st.markdown("##### Dis gonna go crazy")

counts = sim.run(a, p, m)

start_sim = st.button('Start')
stop_sim = st.button('Stop')

if stop_sim:
    placeholder = st.empty()

if start_sim:
    placeholder = st.empty()

    # near real-time / live feed simulation
    # time
    x = []
    # total number of customers in the system
    y = []

    for i, c in enumerate(counts):
        if stop_sim:
            break

        with placeholder.container():

            x.append(i)
            y.append(c)

            # for figures
            fig = make_subplots(rows=1, cols=1)
            fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="total number of customers", showlegend=True), row=1, col=1)

            st.write(fig)

            st.caption(footer_txt, unsafe_allow_html=True)

            time.sleep(0.5)
