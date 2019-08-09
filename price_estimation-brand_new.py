import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#Opening the file with the input
file = open(r'C:\Users\Nuri\Desktop\The Project\1111.csv', 'r')
df = pd.read_csv(file)
 

#Number of Simulations
num_simulations = int(input('How many simulations do you want?: '))
num_days = 731

#creating dataframe to store estimated price
simulation_df = pd.DataFrame()

# Nested loop is stated
for x in range(num_simulations):
    price_series = []
    for y in range(num_days):
        if y == 730:
            break
        daily_vol = float(df.iloc[y, 3])
        last_price = float(df.iloc[y-1, 1])

        #Monte Carlo simulation. 0 is the mean since the numbers are random.
        price = last_price * (1 + np.random.normal(0, daily_vol))
        if y == 0:
            price = float(df.iloc[y, 1])
        price_series.append(price)


    simulation_df[x] = price_series

# Getting the maximum value of the all the simulations
simulation_df['max_value'] = simulation_df.max(axis=1)
#simulation_df['avg_values'], simulation_df['median'] =\
#simulation_df.mean(axis=1),simulation_df.median(axis=1)


# Saving maximum values to a CSV file
max_values = open(r'C:\Users\Nuri\Desktop\max_values.csv', 'w')
simulation_df.to_csv("max_values.csv", sep = ',')
max_values.close()


print(simulation_df)

# Getting the Graph
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: Price Estimation')
plt.plot(simulation_df)
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()