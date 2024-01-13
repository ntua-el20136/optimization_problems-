import numpy as np
from scipy.optimize import minimize

# Unit Price Data
r = 3.00  # Selling Price
c = 2.00   # Cost
w = 0.00  # Salvage value

# Uniform Distribution for Demand
lower_bound = 100  # Minimum demand
upper_bound = 1000  # Maximum demand
step = 100  # Step for discrete intervals
demands = np.arange(lower_bound, upper_bound + step, step)

# Probability for each demand scenario (uniform distribution)
probability = 1 / len(demands)

# Objective Function to Maximize Expected Profit
def expected_profit(order_quantity):
    profit_per_scenario = np.zeros_like(demands, dtype=float)

    for i, demand in enumerate(demands):
        sold = min(order_quantity, demand)
        unsold = max(order_quantity - demand, 0)
        profit_per_scenario[i] = (sold * r + unsold * w - order_quantity * c) * probability

    return -np.sum(profit_per_scenario)  # Negative for minimization

# Optimization
result = minimize(expected_profit, x0=np.mean(demands), bounds=[(0, None)])

# Results
optimal_order_quantity = result.x[0]
max_expected_profit = -result.fun
#what is the value of the stohastic solution

#what is the EVPI
#what is the value of the perfect information
#what is the value of the stochastic


print(f"Optimal Order Quantity: {optimal_order_quantity}")
print(f"Max Expected Profit: {max_expected_profit}")


# Calculate expected profit for deterministic model (demand = expected demand)
deterministic_demand = np.mean(demands)
deterministic_profit = expected_profit(deterministic_demand)

# Calculate expected profit for perfect information scenario
perfect_info_profits = [expected_profit(d) for d in demands]
#turn negative to positive
perfect_info_profits = [-p for p in perfect_info_profits]
perfect_info_expected_profit = np.mean(perfect_info_profits)

# Calculate VSS and EVPI
VSS = max_expected_profit - (-deterministic_profit)
EVPI = (perfect_info_expected_profit) - max_expected_profit

print(f"Value of Stochastic Solution (VSS): {VSS}")
print(f"Expected Value of Perfect Information (EVPI): {EVPI}")



