# Real Time Global Inflation Tracker
This project uses real inflation data from the OECD API to explore and visualize inflation trends and economic volatility across countries in 2023.

## Objectives
- To pull live data from the OECD API.
- To analyze inflation and volatility rates per country/area.
- Identify economic outliers and show risk.
- Visualize these insights to highlight economic health and potential business risk and success zones.

## Questions
- Which countries had the most unstable or stable inflation?
- Which countries had the highest and lowest inflation rates in 2023?
- Can we spot "outliers" ? Essentially, countries with both high inflation and high volatilities?
- What are the potential implications for businesses and investors?

## Tools and libraries
Python
Pandas, seaborn, matplotlib
Jupyter notebook
OECD API

## Insights and key takeways
The 3 countries with the highest inflation rates are: Argentina, Costa Rica, Turkey. This show strong indicators of ongoing economic strain. Which is bad for business.

The 3 areas with the lowest inflation rates are: The Euro Area, Finland, Italy. This indicates relative price stability. Possibly strong purchasing power.

The 3 countries with the highest volatility rates are: Brazil, Turkey, Bulgaria. This shows that inflation trends are unpredictable and is risky for long-term business planning.

The 3 areas with the lowest volatility rates are: Potrugal, G20, Canada. This shows that they have very stable inflation, ideal conditions for investors and policy makers.

The evident outliers are Argentina and Brazil. This shows that they experience both high inflation and high volatility. Very bad for businesses. Businesses should avoid the two.

## Visualizations
Bar charts:
  2 showing Top 10 and bottom 10 countries by inflation
  2 showing Top 10 and bottom 10 countries by volatility rates
Annotated scatter plots: Inflation vs volatility rates used to show outliers
