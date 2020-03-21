import streamlit as st
import time
import numpy as np

st.title("Finance visualizations")


last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.01)

progress_bar.empty()


rv = np.random.randn(101, 1)

chart = st.line_chart(rv[:1,:])

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(1, 101):
    chart.add_rows(rv[i-1:i,:])
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)
    time.sleep(0.01)

progress_bar.empty()


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
