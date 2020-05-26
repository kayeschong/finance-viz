# Visualizing numerical finance

## Objectives:

1. Monte carlo stock price, option payoff simulations

2. Binomial trees path

3. Interactive options payoff combination tool

4. Add follow along explanations

## Possible future visualizations:

* Margin level w.r.t stock price

* Complete portfolio, capital allocation line

* Efficient diversification, Sharpe ratio

* Optimal hedging animation

* Arbitrage conceptual demonstration

## Environment management

First time use:
```
conda env create -f environment.yml
```

Updating existing environment
```
conda env update -f environment.yml --prune
```

To use environment
```
conda activate finance-viz
```

## Running locally
```
streamlit run app.py
```

## Running with docker
```
docker-compose up
```