import streamlit as st

from src.pages.home import run_home
from src.pages.montecarlo import run_montecarlo

st.title("Finance visualizations")

PAGES = {
    "Home": run_home,
    "Monte Carlo": run_montecarlo,
}

def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))


    selected_page = PAGES.get(selection)
    selected_page()

    st.sidebar.title("About")
    st.sidebar.info(
        """
        The source code can be found
        [here](https://github.com/kayeschong/finance-viz).
        """
    )

if __name__ == "__main__":
    main()