import streamlit as st
import time
import numpy as np
import altair as alt
import pandas as pd


def run_montecarlo():
    st.subheader('Monte Carlo Simulation')
    simulation_type = st.selectbox(
        "Simulation type",
        ("Prices", "Options")
    )
    periods = st.slider('Days to simulate', min_value=100, max_value=400, value=100, step=100)
    simulations =  st.number_input('Number of price paths', min_value=0, max_value=400, value=200, step=50)
    start_price = st.number_input('Start Price', min_value=50, value=50, step=10)

    if simulation_type == "Prices":
        plot_single_path = st.button(f'Simulate 1 price path over {periods} days')
        plot_multi_path = st.button(f'Simulate {simulations} price paths over {periods} days')

        if plot_single_path:

            price_changes = np.random.randn(1, 1)
            price = start_price + price_changes
            
            st.markdown('Daily price changes')
            price_change_chart = st.line_chart(price_changes)

            st.markdown('Prices')
            price_chart = st.line_chart(price)
            progress_bar = st.progress(0)
            status_text = st.empty()

            for i in range(1, periods + 1):
                price_changes = np.random.randn(1, 1)
                price = price + price_changes

                price_change_chart.add_rows(price_changes)
                price_chart.add_rows(price)
                
                if i % (periods//100) == 0:
                    status = i // (periods//100)
                    status_text.text(f"{status}% Complete")
                    progress_bar.progress(status)
                    
                time.sleep(0.001)

            progress_bar.empty()


        if plot_multi_path:
            price_changes = np.random.randn(1, simulations)
            price = start_price + price_changes

            price_chart = st.line_chart(price)

            end_price = alt.Chart(pd.DataFrame(price[0, :], columns=["End Prices"])).mark_bar().encode(
                                alt.X("End Prices", bin=alt.Bin(step=5)),
                                y='count()',
                                )

            end_price_chart = st.altair_chart(end_price)

            progress_bar = st.progress(0)
            status_text = st.empty()

            for i in range(1, periods + 1):
                price = price + np.random.randn(1, simulations)

                price_chart.add_rows(price)
                
                end_price = alt.Chart(pd.DataFrame(price[0, :], columns=["End Prices"])).mark_bar().encode(
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
                st.write("Try to simulate something.")

    if simulation_type == "Options":
        st.warning('Work in progress')
        option_type = st.selectbox(
            "Option type",
            ('Call', 'Put')
        )
        strike_price = st.number_input('Strike Price', min_value=0, value=50, step=5)
        plot_options = st.button(f'Simulate {simulations} price paths, strike price over {periods} days')
    
        if plot_options:
            price_changes = price_changes = np.random.randn(periods, simulations)
            price = start_price + price_changes.cumsum(axis=0)
            price_df = pd.DataFrame(price)
            price_df['strike'] = strike_price
            price_df_long = price_df.reset_index().melt(id_vars='index', var_name='stock_id', value_name='price')
            price_df_long['color'] = 0
            price_df_long.loc[price_df_long['stock_id'] == simulations - 1, 'color'] = 5
            price_df_long.loc[price_df_long['stock_id'] == 'strike', 'color'] = 4
            
            with st.spinner('Plotting...'):
                x = alt.Chart(price_df_long).mark_line(opacity=0.5).encode(
                    x='index:Q',
                    y='price:Q',
                    color=alt.Color('color:Q', legend=None, scale=alt.Scale(scheme='lightgreyred')),
                    detail='stock_id:N',
                )

                st.altair_chart(x, use_container_width=True)

            st.write('Payoff frequency vs payoff amount')
            last_day = price_df_long[price_df_long['index'] == periods-1]
            if option_type == 'Call':
                payoff = last_day[['price']].copy()
                payoff = payoff - strike_price
                payoff[payoff['price'] < 0] = 0
                payoff.columns = ['payoff']
                payoff_chart = alt.Chart(payoff).mark_bar().encode(
                                    x=alt.X('payoff', bin=alt.Bin(step=2)),
                                    y='count()'
                                )
                st.altair_chart(payoff_chart, use_container_width=True)

            if option_type == 'Put':
                payoff = last_day[['price']].copy()
                payoff = strike_price - payoff
                payoff[payoff['price'] < 0] = 0
                payoff.columns = ['payoff']
                payoff_chart = alt.Chart(payoff).mark_bar().encode(
                                    x=alt.X('payoff', bin=alt.Bin(step=2)),
                                    y='count()'
                                )
                st.altair_chart(payoff_chart, use_container_width=True)


            if simulations == 0:
                st.write("Try to simulate something.")


    st.button("Clear chart")
        
if __name__ == "__main__":
    run_montecarlo()