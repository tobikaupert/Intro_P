# Data analysis project

This Project focuses on the Time Series analysis of USDCAD. Futhermore, 
how the price and return behavior of US 10 year Treasury bonds, Canadian
 10 year treasury bonds and WTI Crude oil impact the returns of USDCAD. 
In this data analysis project, we download monthly data from FRED API 
and conduct multiple linear regression and regime switching analysis to 
determine if there any specific relationship between the variables and 
if so, how do they change over time? The motivation for this study is 
that the canadian dollar is known to be a commodity currency. The price 
of WTI crude oil and other commodities can greatly impact the canadian 
economy. In this analysis, we will explore if the monthly returns of 
crude oil have a significant impact on the price behavior of USDCAD. We 
will also add interest rates of 10 year bonds to improve the regression 
and just for fun. 

The **results** of the project can be seen from running [dataproject.ipynb](TimeSeries_Analysis.ipynb).

We conclude:
This data analyis project was very insightful and shed light on the 
relationship between USDCAD exchange rate and the effect of interest 
rates and crude oil prices on USDCAD returns. In this project, we first 
analyzed the plots of each our variables both in their original levels 
and in percent change in order to observe the behavior of US/Canadian 
interest rates, USDCAD exchange rate and crude oil. There appeared to be
 shocks in Crude oil that translated over to USDCAD exchange rate and 
there was a strong relationship in US/Canadian interest rates. These 
relationships were further validated from our correlation matrix. 
However, it wasn't until we conducted our OLS regressions that we 
discovered crude oil returns and Canadian 10 year treasury yields have a
 highly significant effect on the returns of USDCAD. The effect of 
Canadian interest rates on USDCAD was in line with theory, while the 
effect of crude oil returns was in line with out expectations that a 
commodity currency like the Canadian dollar appreciates from rises in 
WTI crude oil price increases. The effects of crude oil and canadian 
interest rates were found to have multiple regime shifts. This was 
illustrated in our OLS windowed regressions, where we discovered that 
2008 and 2016 were key regime shifting points for the effect of crude 
oil returns on USDCAD returns. In the future, it would be insigntful to 
analyze in more detail how these regime shifts originated and why they 
had such a significant impact on our model. 


**Dependencies:** standard Anaconda Python 3 installation, the project requires the following installations:
statsmodels
arch

