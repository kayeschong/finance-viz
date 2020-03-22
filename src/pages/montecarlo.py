import streamlit as st
import time
import numpy as np


def run_montecarlo():
    st.subheader('Monte Carlo Simulation')
    n = st.slider('runs', min_value=100, max_value=1000, value=200, step=100)
    
    if st.button('Run simulation'):
        
        price_changes = np.random.randn(n)
        price = price_changes.cumsum()

        price_change_chart = st.line_chart(price_changes[:1])
        price_chart = st.line_chart(price_changes[:1])
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(1, n + 1):
            price_change_chart.add_rows(price_changes[i-1:i])
            price_chart.add_rows(price[i-1:i])
            
            if i % (n//100) == 0:
                status = i // (n//100)
                status_text.text(f"{status}% Complete")
                progress_bar.progress(status)
                
            time.sleep(0.001)

        progress_bar.empty()

        st.button("Clear charts")

        
if __name__ == "__main__":
    run_montecarlo()