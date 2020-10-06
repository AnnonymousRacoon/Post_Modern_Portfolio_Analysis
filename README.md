# Post-Modern Portfolio Analysis

<img src = "EF_hvr.png"><br>

In this project we'll take a look 20 Stocks from NASDAQ index and select an optimal portfolio. We'll start off by using modern portfolio theory (<a href = "https://www.investopedia.com/terms/m/modernportfoliotheory.asp">MFT</a>) to find the efficient frontier, and switch to the post-modern varient (<a href = "https://www.investopedia.com/terms/p/pmpt.asp">MFT</a>) for improved results. To make for a more holistic approach we then look at some of the outliers and do some some real world research to better understand them. Finally we will consider diversification and then select our portfolio accordingly.

## Prerequisites

If you're relatively new to Python or data analysis, to do this on your own machine you'll need to install numpy, pandas and pandas-datareader. We'll also be using <a href = "https://plotly.com/python/">Plotly</a> to make interactive plots. For some of the extra graphs in the appendix, we also require Matplotlib and seaborn(for styling). All these libraries are available using pip or conda (if you're using an anaconda environment).

#### Pip:

```
$ pip install numpy
```

```
$ pip install pandas
```

```
$ pip install pandas-datareader
```

```
$ pip install plotly==4.11.0
```

#### Anaconda:

```
$ conda install numpy
```

```
$ conda install pandas
```

```
$ conda install -c plotly plotly=4.11.0
```

```
$ conda install -c anaconda pandas-datareader 
```


## Doing your own analysis

The functions used find the efficient frontier can be found in the `Portfolio_Opt` Module. This project uses `pandas-datareader` to get financial data from [yahoo finance](https://uk.finance.yahoo.com), but you could also use an API such as [Tiingo](https://api.tiingo.com). Using an API such as this may be helpful if you want to get live information. For more information see the [pandas-datareader documentation](https://pandas-datareader.readthedocs.io/en/latest/).