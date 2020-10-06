from scipy.optimize import minimize
import pandas as pd
import numpy as np


def gen_portfolios(expected_returns,tickers,cov,num_ports=5000,random_seed = 42,bias = None):
    num_stocks = len(tickers)
    np.random.seed(random_seed)
    all_weights = np.zeros((num_ports, num_stocks))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    sortino_arr = np.zeros(num_ports)

    for i in range(num_ports):
        # Weights
        weights = np.array(np.random.random(num_stocks))
        if bias:
            for wt,idx in bias:
                weights[idx] = np.random.uniform()*wt
        weights = weights/np.sum(weights)


        # Save weights
        all_weights[i] = weights

        # Expected return
        ret_arr[i] = sum([expected_returns[tick] * weight for tick,weight in zip(tickers,weights)])

        # Expected volatility
        vol_arr[i] = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))

        # Sortino Ratio
        sortino_arr[i] = (0.01*ret_arr[i]-0.011)/vol_arr[i]
        
    return vol_arr, ret_arr, sortino_arr, all_weights



def Optimise(cov,tickers,expected_returns):

    num_symbols = len(tickers)

    def get_portfolio_metrics(weights):
        weights = np.array(weights)
        portfolio_returns= sum([expected_returns[tick] * weight for tick,weight in zip(tickers,weights)])
        portfolio_stand = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
        sortino_ratio = 0.01*(portfolio_returns-1.1)/portfolio_stand
        return np.array([portfolio_returns, portfolio_stand, sortino_ratio])

    def check_sum(weights):
        #return 0 if sum of the weights is 1
        return np.sum(weights)-1




    # helper func
    def minimize_volatility(weights):
        return get_portfolio_metrics(weights)[1]

    def optimise_portfolio(constraints,optimising_func):

        # confine the weights to be between 0 and 1
        bounds = tuple([(0,1)for _ in range(num_symbols)])
        #an initial starting point for the regression function
        init_guess = [0.25 for _ in range(num_symbols)]

        optimal_metrics = minimize(optimising_func,init_guess,method = "SLSQP",bounds=bounds,constraints = constraints)
        
        return optimal_metrics



    frontier_y = np.linspace(0,expected_returns.max(),200)

    frontier_x = []
    frontier_weights = []

    for possible_return in frontier_y:
        cons = ({'type':'eq', 'fun':check_sum},
                {'type':'eq', 'fun': lambda wt: get_portfolio_metrics(wt)[0] - possible_return})
        
        result = optimise_portfolio(cons,minimize_volatility)
        frontier_weights.append(result.x)
        frontier_x.append(result['fun'])


    efficient_portfolios = pd.DataFrame({'Risks': frontier_x, 'Annual_Returns': frontier_y})

    # append weights columns
    for i,key in zip(range(num_symbols),tickers):
        efficient_portfolios[key] = pd.Series(np.array([wts[i] for wts in frontier_weights]))


    return efficient_portfolios