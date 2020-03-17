# Visualizing numerical finance

## Objectives:

1. Monte carlo stock price simulation and distribution

2. Binomial Trees

3. Black Scholes

## Possible (future) visualizations:

* Margin level w.r.t stock price

* Complete portfolio, capital allocation line

* Efficient diversification, Sharpe ratio

* Arbitrage

## Environment management

First time use:
```
conda env create -f environment.yml
```

Updating existing environment
```
conda env update -f environment.yml
```

To use environment
```
conda activate finance-viz
```

## Running locally
```
streamlit run app.py
```