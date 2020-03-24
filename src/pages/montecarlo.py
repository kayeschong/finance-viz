import streamlit as st
import time
import numpy as np
import altair as alt
import pandas as pd


def run_montecarlo():
    st.subheader('Monte Carlo Simulation')
    periods = st.slider('Days to simulate', min_value=100, max_value=500, value=100, step=100)
    start_price = st.number_input('Start Price', min_value=50, value=50, step=10)
    simulations =  st.number_input('Number of futures', min_value=0, max_value=400, value=200, step=50)


    price_changes = np.random.randn(periods, simulations)
    price = start_price + price_changes.cumsum(axis=0)

    if st.button(f'Simulate 1 future over {periods} days'):
        
        st.markdown('Daily price changes')
        price_change_chart = st.line_chart(price_changes[:1, 0])

        st.markdown('Prices')
        price_chart = st.line_chart(price[:1, 0])
        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(1, periods + 1):
            price_change_chart.add_rows(price_changes[i-1:i, 0])
            price_chart.add_rows(price[i-1:i, 0])
            
            if i % (periods//100) == 0:
                status = i // (periods//100)
                status_text.text(f"{status}% Complete")
                progress_bar.progress(status)
                
            time.sleep(0.001)

        progress_bar.empty()

        st.button("Clear chart")



    if st.button(f'Simulate {simulations} futures over {periods} days'):
        price_changes = np.random.randn(periods, simulations)
        price = start_price + price_changes.cumsum(axis=0)

        price_chart = st.line_chart(price[:1, :])

        end_price = alt.Chart(pd.DataFrame(price[0, :], columns=["End Prices"])).mark_bar().encode(
                              alt.X("End Prices", bin=alt.Bin(step=5)),
                              y='count()',
                              )

        end_price_chart = st.altair_chart(end_price)

        progress_bar = st.progress(0)
        status_text = st.empty()

        for i in range(1, periods + 1):
            price_chart.add_rows(price[i-1:i, :])
            
            end_price = alt.Chart(pd.DataFrame(price[i-1, :], columns=["End Prices"])).mark_bar().encode(
                                  alt.X("End Prices", bin=alt.Bin(step=5)),
                                  y='count()',
                                  )
            end_price_chart.altair_chart(end_price)
            if i % (periods//100) == 0:
                status = i // (periods//100)
                status_text.text(f"{status}% Complete")
                progress_bar.progress(status)
            time.sleep(0.001)

        progress_bar.empty()

        if simulations == 0:
            st.write("I guess you've got no future.")


        
        st.button("Clear chart")
        
if __name__ == "__main__":
    run_montecarlo()